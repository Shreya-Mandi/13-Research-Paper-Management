const express = require('express');
const cors = require('cors');
const Joi = require('joi');
const mysql = require('mysql2/promise');

const PORT = 3002;
const SQLCONFIG = {
    host: 'localhost',
    user: 'root',
    password: 'sql*db*admin',
    database: 'research_mgmt'
};

StartService().then(r => r);

async function StartService() {
    try {

        console.log("Setting up express...")
        const app = express();

        app.use(cors());
        app.use(express.json());
        app.use(express.urlencoded({extended: true}));

        app.post('/Test/', handleTest);                        // working
        app.get('/NewDb/', handleTest);
        app.get('/InsDb/', handleTest);
        app.get('/ClsDb/', handleTest);
        app.get('/DelDb/', handleTest);

        app.post('/Login/', handleLogin);                      // working
        app.post('/Register/', handleRegister);                // working

        app.post('/GetProjects/', handleGetProjects);          // working - in-efficient

        app.post('/NewProject/', handleTest);
        app.post('/GetProject/', handleTest);
        app.post('/UpdProject/', handleTest);
        app.post('/DelProject/', handleTest);

        app.post('/NewMeeting/', handleTest);
        app.post('/GetMeetings/', handleTest);
        app.post('/UpdMeeting/', handleTest);

        app.post('/NewSuggestions/', handleTest);
        app.post('/GetSuggestions/', handleTest);

        console.log("Set up express.")

        app.listen(PORT, () => console.log(`Listening On Port ${PORT}...`))
    } catch (err) {
        console.log(err);
    }
}

async function handleLogin(req, res) {
    try {
        console.log("Got request", req.body);

        const schema = Joi.object({
            id: Joi.string().alphanum().custom((value, helper) => {
                if (value.length === 8 || value.length === 13) {
                    return value;
                } else {
                    return helper.message("invalid ID");
                }
            }).required(),
            pwd: Joi.string().min(5).required()
        });

        let check = schema.validate(req.body);
        if (check.hasOwnProperty("error")) {
            let response = {
                invalidRequest: true,
                status: false,
                errMsg: check.error.details[0].message
            };
            console.log("InvalidRequest, ", response);
            res.send(response);
            return;
        }

        let typeOfUsr = "student";
        let typeOfId = "srn";
        if (req.body.id.length === 8) {
            typeOfUsr = "faculty";
            typeOfId = "id";
        }

        let result, _, connection = await getConnection();
        const sqlQuery =
            `SELECT ${typeOfId}, password, first_name, last_name
             FROM ${typeOfUsr}
             WHERE ${typeOfId} = '${req.body.id}'`;
        [result, _] = await connection.query(sqlQuery);

        let valid = false;
        let name = "";
        if (result.length !== 0) {
            let actual_pwd = result[0].password;
            if (actual_pwd === req.body.pwd) {
                valid = true;
                name = result[0].first_name + " " + result[0].last_name;
            }
        }

        let response = {
            status: true,
            valid: valid,
            type: typeOfUsr,
            name: name
        };

        console.log("Success, ", response);
        res.send(response);

    } catch (err) {
        console.log(err, '- Error !!!!!!!!!!!!!!!!');
        res.send({invalidRequest: false, status: false, errMsg: err});
    }
}

async function handleRegister(req, res) {
    try {
        console.log("Got request", req.body);

        const schemaStudent = Joi.object({
            firstName: Joi.string().required(),
            lastName: Joi.string().required(),
            dept: Joi.string().valid('CSE', 'ECE', 'EEE', 'AIML', 'ME').insensitive().required(),
            sem: Joi.number().integer().options({convert: false}).min(1).max(8).required(),
            sec: Joi.string().length(1).insensitive().required()
        });

        const schemaFaculty = Joi.object({
            firstName: Joi.string().required(),
            lastName: Joi.string().required(),
            dept: Joi.string().valid('CSE', 'ECE', 'EEE', 'AIML', 'ME').insensitive().required(),
            domain: Joi.string().insensitive().required()
        })

        const schema = Joi.object({
            id: Joi.string().alphanum().custom((value, helper) => {
                if (value.length === 8 || value.length === 13) {
                    return value;
                } else {
                    return helper.message("invalid ID");
                }
            }).required(),
            pwd: Joi.string().min(5).required(),
            type: Joi.string().valid('student', 'faculty').required(),
            details: Joi.when('type', {
                is: 'student',
                then: schemaStudent.required(),
                otherwise: schemaFaculty.required()
            })
        });

        let check = schema.validate(req.body);
        if (check.hasOwnProperty("error")) {
            let response = {
                invalidRequest: true,
                status: false,
                errMsg: check.error.details[0].message
            };
            console.log("InvalidRequest, ", response);
            res.send(response);
            return;
        }

        let connection = await getConnection();

        const sqlQuery =
            `INSERT INTO ${req.body.type}
             VALUES ('${req.body.id}',
                     '${req.body.details.firstName}',
                     '${req.body.details.lastName}',
                     '${req.body.details.dept.toUpperCase()}',` + (
                (req.body.type === "student") ?
                    `${req.body.details.sem}, '${req.body.details.sec}',` :
                    `'${req.body.details.domain}',`
            ) + `'${req.body.pwd}')`;

        await connection.query(sqlQuery);
        let response = {status: true};

        console.log("Success, ", response);
        res.send(response);
    } catch
        (err) {
        console.log(err, '- Error !!!!!!!!!!!!!!!!');
        res.send({invalidRequest: false, status: false, errMsg: err});
    }
}

async function handleGetProjects(req, res) {
    try {
        console.log("Got request", req.body);

        const schema = Joi.object({
            type: Joi.string().valid("student", "faculty", "guest").required(),
            id: Joi.string().alphanum().custom((value, helper) => {
                if (value.length === 8 || value.length === 13) {
                    return value;
                } else {
                    return helper.message("invalid ID");
                }
            }).when('type', {
                is: 'guest',
                then: Joi.optional(),
                otherwise: Joi.required()
            })
        });

        let check = schema.validate(req.body);
        if (check.hasOwnProperty("error")) {
            let response = {
                invalidRequest: true,
                status: false,
                errMsg: check.error.details[0].message
            };
            console.log("InvalidRequest, ", response);
            res.send(response);
            return;
        }

        let sqlQuery, projects, students, faculty, _, connection = await getConnection();
        sqlQuery =
            `SELECT id AS projectID, topic AS projectTitle, status AS projectStatus
             FROM paper
             ORDER BY projectID`;
        [projects, _] = await connection.query(sqlQuery);

        projects.forEach((item) => {
            item.faculty = [];
            item.student = [];
        });

        sqlQuery =
            `SELECT t1.paper_id AS projectID, srn AS id, Concat(first_name, ' ', last_name) AS name
             FROM (SELECT id AS paper_id FROM paper) AS t1
                      NATURAL JOIN student_writes_paper
                      NATURAL JOIN student`;
        [students, _] = await connection.query(sqlQuery);

        students.forEach((item) => {
            let element = projects.find((element) => element.projectID === item.projectID);
            element.student.push({id: item.id, name: item.name});
        });

        sqlQuery =
            `SELECT DISTINCT t1.paper_id AS projectID, id, Concat(first_name, ' ', last_name) AS name
             FROM (SELECT id AS paper_id FROM paper) AS t1
                      NATURAL JOIN (SELECT faculty_id AS id, paper_id FROM faculty_advises_paper) AS t2
                      NATURAL JOIN faculty`;
        [faculty, _] = await connection.query(sqlQuery);

        faculty.forEach((item) => {
            let element = projects.find((element) => element.projectID === item.projectID);
            element.faculty.push({id: item.id, name: item.name});
        });

        let projectList = [];

        projects.forEach((item) => {
            switch (req.body.type) {
                case "student" :
                    if (item.student.find((element) => element.id === req.body.id) !== undefined){
                        projectList.push(item);
                    }
                    break;
                case "faculty":
                    if (item.faculty.find((element) => element.id === req.body.id) !== undefined){
                        projectList.push(item);
                    }
                    break;
                case "guest":
                    if (item.projectStatus === "Published"){
                        projectList.push(item);
                    }
                    break;
            }
        })

        let response = {status: true, projects: projectList};

        console.log("Success, ", response);
        res.send(response);
    } catch (err) {
        console.log(err, '- Error !!!!!!!!!!!!!!!!');
        res.send({invalidRequest: false, status: false, errMsg: err});
    }
}

async function handleTest(req, res) {
    try {
        console.log("Got request", req.body);

        // TODO validate request
        const schema = Joi.object({});

        let check = schema.validate(req.body);
        if (check.hasOwnProperty("error")) {
            let response = {
                invalidRequest: true,
                status: false,
                errMsg: check.error.details[0].message
            };
            console.log("InvalidRequest, ", response);
            res.send(response);
            return;
        }

        // TODO MySql interaction
        let result, _, connection = await getConnection();
        const sqlQuery =
            `SHOW TABLES`;
        [result, _] = await connection.query(sqlQuery);

        let response = {status: true, result: result};

        console.log("Success, ", response);
        res.send(response);
    } catch (err) {
        console.log(err, '- Error !!!!!!!!!!!!!!!!');
        res.send({invalidRequest: false, status: false, errMsg: err});
    }
}

async function getConnection() {
    return await mysql.createConnection(SQLCONFIG);
}