const express = require('express');
const cors = require('cors');
const Joi = require('joi').extend(require('@joi/date'));
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

        app.post('/NewProject/', handleNewProject);            // working
        app.post('/GetProject/', handleGetProject);            // working - in-efficient
        app.post('/UpdProject/', handleUpdProject);            // working
        app.post('/DelProject/', handleDelProject);            // working

        app.post('/NewMeeting/', handleNewMeeting);            // working
        app.post('/GetMeetings/', handleGetMeetings);          // working
        app.post('/UpdMeeting/', handleUpdMeeting);            // working

        app.post('/NewSuggestion/', handleNewSuggestion);      // working
        app.post('/GetSuggestions/', handleGetSuggestions);    // working

        app.get('/GetUsers/', handleGetUsers);                      // working

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
            sem: Joi.number().integer().min(1).max(8).required(),
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
                    `${req.body.details.sem}, '${req.body.details.sec.toUpperCase()}',` :
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
                    if (item.student.find((element) => element.id === req.body.id) !== undefined) {
                        projectList.push(item);
                    }
                    break;
                case "faculty":
                    if (item.faculty.find((element) => element.id === req.body.id) !== undefined) {
                        projectList.push(item);
                    }
                    break;
                case "guest":
                    if (item.projectStatus === "Published") {
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

async function handleNewProject(req, res) {
    try {
        console.log("Got request", req.body);

        const schema = Joi.object({
            projectTitle: Joi.string().required(),
            projectStatus: Joi.string().valid("Published", "Ongoing").insensitive().required(),
            startDate: Joi.date().format('YYYY-MM-DD').required(),
            endDate: Joi.date().format('YYYY-MM-DD').min(Joi.ref('startDate')).optional(),
            facultyID: Joi.array().min(1).items(Joi.string().alphanum().length(8)).required(),
            studentID: Joi.array().min(1).items(Joi.string().alphanum().length(13)).required(),
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

        let sqlQuery, valuesQuery, projectID, _, connection = await getConnection();

        await connection.query(`START TRANSACTION`);

        sqlQuery =
            `INSERT INTO paper (topic, status, start_date, end_date)
             VALUES ('${req.body.projectTitle}',
                     '${req.body.projectStatus}',
                     '${req.body.startDate}',` +
            ((req.body.hasOwnProperty("endDate")) ? `'${req.body.endDate}'` : `NULL`) +
            `)`;
        await connection.query(sqlQuery);

        [projectID, _] = await connection.query(`SELECT id
                                                 FROM paper
                                                 ORDER BY id DESC
                                                 LIMIT 1`);
        projectID = projectID[0].id;

        valuesQuery = ``;
        req.body.studentID.forEach((item, index) => {
            if (index !== 0)
                valuesQuery += `,`;
            valuesQuery += `('${item}', '${projectID}')`;
        });
        sqlQuery = `INSERT INTO student_writes_paper
                    VALUES ` + valuesQuery;
        await connection.query(sqlQuery);

        valuesQuery = ``;
        req.body.facultyID.forEach((item, index) => {
            if (index !== 0)
                valuesQuery += `,`;
            valuesQuery += `('${item}', '${projectID}')`;
        });
        sqlQuery = `INSERT INTO faculty_advises_paper (Faculty_ID, Paper_ID)
                    VALUES ` + valuesQuery;
        await connection.query(sqlQuery);

        await connection.query(`COMMIT`);

        let response = {status: true};

        console.log("Success, ", response);
        res.send(response);
    } catch (err) {
        console.log(err, '- Error !!!!!!!!!!!!!!!!');
        res.send({invalidRequest: false, status: false, errMsg: err});
    }
}

async function handleGetProject(req, res) {
    try {
        console.log("Got request", req.body);

        const schema = Joi.object({
            projectID: Joi.number().integer().min(0).required()
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
            `SELECT id                                  AS projectID,
                    topic                               AS projectTitle,
                    status                              AS projectStatus,
                    Date_Format(start_date, '%Y-%m-%d') AS startDate,
                    Date_Format(end_date, '%Y-%m-%d')   AS endDate
             FROM paper
             WHERE id = ${req.body.projectID}`;
        [projects, _] = await connection.query(sqlQuery);

        console.log(projects);

        projects.forEach((item) => {
            item.faculty = [];
            item.student = [];
        });

        sqlQuery =
            `SELECT t1.paper_id AS projectID, srn AS id, Concat(first_name, ' ', last_name) AS name
             FROM (SELECT id AS paper_id FROM paper) AS t1
                      NATURAL JOIN student_writes_paper
                      NATURAL JOIN student
             HAVING projectID = ${req.body.projectID}`;
        [students, _] = await connection.query(sqlQuery);

        students.forEach((item) => {
            let element = projects.find((element) => element.projectID === item.projectID);
            element.student.push({id: item.id, name: item.name});
        });

        sqlQuery =
            `SELECT DISTINCT t1.paper_id AS projectID, id, Concat(first_name, ' ', last_name) AS name
             FROM (SELECT id AS paper_id FROM paper) AS t1
                      NATURAL JOIN (SELECT faculty_id AS id, paper_id FROM faculty_advises_paper) AS t2
                      NATURAL JOIN faculty
             HAVING projectID = ${req.body.projectID}`;
        [faculty, _] = await connection.query(sqlQuery);

        faculty.forEach((item) => {
            let element = projects.find((element) => element.projectID === item.projectID);
            element.faculty.push({id: item.id, name: item.name});
        });

        let response = {status: true, details: (projects[0] !== undefined) ? projects[0] : {}};

        console.log("Success, ", response);
        res.send(response);
    } catch (err) {
        console.log(err, '- Error !!!!!!!!!!!!!!!!');
        res.send({invalidRequest: false, status: false, errMsg: err});
    }
}

async function handleUpdProject(req, res) {
    try {
        console.log("Got request", req.body);

        const schema = Joi.object({
            projectID: Joi.number().integer().min(0).required(),
            projectTitle: Joi.string().optional(),
            projectStatus: Joi.string().valid("Published", "Ongoing").insensitive().optional(),
            startDate: Joi.date().format('YYYY-MM-DD').optional(),
            endDate: Joi.date().format('YYYY-MM-DD').optional(),
            facultyID: Joi.array().min(1).items(Joi.string().alphanum().length(8)).optional(),
            studentID: Joi.array().min(1).items(Joi.string().alphanum().length(13)).optional(),
            delEndDate: Joi.boolean().optional(),
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

        let sqlQuery, valuesQuery, connection = await getConnection();

        await connection.query(`START TRANSACTION`);

        if (req.body.hasOwnProperty("projectTitle")) {
            await connection.query(`UPDATE paper
                                    SET topic = '${req.body.projectTitle}'
                                    WHERE id = ${req.body.projectID}`);
        }
        if (req.body.hasOwnProperty("projectStatus")) {
            await connection.query(`UPDATE paper
                                    SET status = '${req.body.projectStatus}'
                                    WHERE id = ${req.body.projectID}`);
        }
        if (req.body.hasOwnProperty("startDate")) {
            await connection.query(`UPDATE paper
                                    SET start_date = '${req.body.startDate}'
                                    WHERE id = ${req.body.projectID}`);
        }
        if (req.body.hasOwnProperty("endDate")) {
            await connection.query(`UPDATE paper
                                    SET end_date = '${req.body.endDate}'
                                    WHERE id = ${req.body.projectID}`);
        }
        if (req.body.hasOwnProperty("delEndDate") && req.body.delEndDate) {
            await connection.query(`UPDATE paper
                                    SET end_date = NULL
                                    WHERE id = ${req.body.projectID}`);
        }
        if (req.body.hasOwnProperty("studentID")) {
            sqlQuery = `DELETE
                        FROM student_writes_paper
                        WHERE paper_id = ${req.body.projectID}`;
            await connection.query(sqlQuery);

            valuesQuery = ``;
            req.body.studentID.forEach((item, index) => {
                if (index !== 0)
                    valuesQuery += `,`;
                valuesQuery += `('${item}', '${req.body.projectID}')`;
            });
            sqlQuery = `INSERT INTO student_writes_paper
                        VALUES ` + valuesQuery;
            await connection.query(sqlQuery);
        }
        if (req.body.hasOwnProperty("facultyID")) {
            sqlQuery = `DELETE
                        FROM faculty_advises_paper
                        WHERE paper_id = ${req.body.projectID}`;
            await connection.query(sqlQuery);

            valuesQuery = ``;
            req.body.facultyID.forEach((item, index) => {
                if (index !== 0)
                    valuesQuery += `,`;
                valuesQuery += `('${item}', '${req.body.projectID}')`;
            });
            sqlQuery = `INSERT INTO faculty_advises_paper (faculty_id, paper_id)
                        VALUES ` + valuesQuery;
            await connection.query(sqlQuery);
        }

        await connection.query(`COMMIT`);

        let response = {status: true};

        console.log("Success, ", response);
        res.send(response);
    } catch (err) {
        console.log(err, '- Error !!!!!!!!!!!!!!!!');
        res.send({invalidRequest: false, status: false, errMsg: err});
    }
}

async function handleDelProject(req, res) {
    try {
        console.log("Got request", req.body);

        const schema = Joi.object({
            projectID: Joi.number().integer().min(0).required()
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

        let sqlQuery, connection = await getConnection();
        sqlQuery =
            `DELETE
             FROM paper
             WHERE id = ${req.body.projectID}`;
        await connection.query(sqlQuery);

        let response = {status: true};

        console.log("Success, ", response);
        res.send(response);
    } catch (err) {
        console.log(err, '- Error !!!!!!!!!!!!!!!!');
        res.send({invalidRequest: false, status: false, errMsg: err});
    }
}

async function handleNewMeeting(req, res) {
    try {
        console.log("Got request", req.body);

        const schema = Joi.object({
            projectID: Joi.number().integer().min(0).required(),
            startTime: Joi.date().format('YYYY-MM-DD HH:mm:ss').required(),
            endTime: Joi.date().format('YYYY-MM-DD HH:mm:ss').min(Joi.ref('startTime')).required(),
            link: Joi.string().required(),
            remarks: Joi.string().required(),
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

        let sqlQuery, connection = await getConnection();

        sqlQuery =
            `INSERT INTO meeting(paper_id, start_time, end_time, link, remarks)
             VALUES ('${req.body.projectID}',
                     '${req.body.startTime}',
                     '${req.body.endTime}',
                     '${req.body.link}',
                     '${req.body.remarks}')`;
        await connection.query(sqlQuery);

        let response = {status: true};

        console.log("Success, ", response);
        res.send(response);
    } catch (err) {
        console.log(err, '- Error !!!!!!!!!!!!!!!!');
        res.send({invalidRequest: false, status: false, errMsg: err});
    }
}

async function handleGetMeetings(req, res) {
    try {
        console.log("Got request", req.body);

        const schema = Joi.object({
            projectID: Joi.number().integer().min(0).required()
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

        let sqlQuery, meetingList, _, connection = await getConnection();
        sqlQuery =
            `SELECT id,
                    DATE_FORMAT(start_time, '%Y-%m-%d %H-%i-%s') AS startTime,
                    DATE_FORMAT(end_time, '%Y-%m-%d %H-%i-%s')   AS endTime,
                    link,
                    status,
                    remarks
             FROM meeting
             WHERE paper_id = ${req.body.projectID}`;
        [meetingList, _] = await connection.query(sqlQuery);

        let response = {status: true, meetings: meetingList};

        console.log("Success, ", response);
        res.send(response);
    } catch (err) {
        console.log(err, '- Error !!!!!!!!!!!!!!!!');
        res.send({invalidRequest: false, status: false, errMsg: err});
    }
}

async function handleUpdMeeting(req, res) {
    try {
        console.log("Got request", req.body);

        const schema = Joi.object({
            meetingID: Joi.number().integer().min(0).required(),
            status: Joi.string().valid('Accepted', 'Rejected', 'Requested').insensitive().optional(),
            startTime: Joi.date().format('YYYY-MM-DD HH:mm:ss').optional(),
            endTime: Joi.date().format('YYYY-MM-DD HH:mm:ss').optional(),
            link: Joi.string().optional(),
            remarks: Joi.string().optional(),
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

        await connection.query(`START TRANSACTION`);

        if (req.body.hasOwnProperty("status")) {
            await connection.query(`UPDATE meeting
                                    SET status = '${req.body.status}'
                                    WHERE id = ${req.body.meetingID}`);
        }
        if (req.body.hasOwnProperty("startTime")) {
            await connection.query(`UPDATE meeting
                                    SET start_time = '${req.body.startTime}',
                                        status     = 'Requested'
                                    WHERE id = ${req.body.meetingID}`);
        }
        if (req.body.hasOwnProperty("endTime")) {
            await connection.query(`UPDATE meeting
                                    SET end_time = '${req.body.endTime}',
                                        status   = 'Requested'
                                    WHERE id = ${req.body.meetingID}`);
        }
        if (req.body.hasOwnProperty("link")) {
            await connection.query(`UPDATE meeting
                                    SET link = '${req.body.link}'
                                    WHERE id = ${req.body.meetingID}`);
        }
        if (req.body.hasOwnProperty("remarks")) {
            await connection.query(`UPDATE meeting
                                    SET remarks = '${req.body.remarks}',
                                        status  = 'Requested'
                                    WHERE id = ${req.body.meetingID}`);
        }

        await connection.query(`COMMIT`);

        let response = {status: true};

        console.log("Success, ", response);
        res.send(response);
    } catch (err) {
        console.log(err, '- Error !!!!!!!!!!!!!!!!');
        res.send({invalidRequest: false, status: false, errMsg: err});
    }
}

async function handleNewSuggestion(req, res) {
    try {
        console.log("Got request", req.body);

        const schema = Joi.object({
            projectID: Joi.number().integer().min(0).required(),
            facultyID: Joi.string().alphanum().length(8).required(),
            suggestion: Joi.string().required()
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

        let sqlQuery, connection = await getConnection();
        sqlQuery =
            `INSERT INTO faculty_advises_paper
             VALUES ('${req.body.facultyID}',
                     '${req.body.projectID}',
                     '${req.body.suggestion}',
                     Now())`;
        await connection.query(sqlQuery);

        let response = {status: true};

        console.log("Success, ", response);
        res.send(response);
    } catch (err) {
        console.log(err, '- Error !!!!!!!!!!!!!!!!');
        res.send({invalidRequest: false, status: false, errMsg: err});
    }
}

async function handleGetSuggestions(req, res) {
    try {
        console.log("Got request", req.body);

        const schema = Joi.object({
            projectID: Joi.number().integer().min(0).required()
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

        let sqlQuery, suggestionsList, _, connection = await getConnection();
        sqlQuery =
            `SELECT t1.*, Concat(first_name, ' ', last_name) AS name
             FROM (SELECT faculty_id AS id, suggestions AS msg, DATE_FORMAT(timestamp, '%Y-%m-%d %H-%i-%s') AS time
                   FROM faculty_advises_paper
                   WHERE paper_id = ${req.body.projectID}
                     AND suggestions <> '') AS t1
                      NATURAL JOIN faculty`;
        [suggestionsList, _] = await connection.query(sqlQuery);

        let response = {status: true, suggestions: suggestionsList};

        console.log("Success, ", response);
        res.send(response);
    } catch (err) {
        console.log(err, '- Error !!!!!!!!!!!!!!!!');
        res.send({invalidRequest: false, status: false, errMsg: err});
    }
}

async function handleGetUsers(req, res) {
    try {
        let sqlQuery, students, faculty, _, connection = await getConnection();

        sqlQuery =
            `SELECT srn
             FROM student`;
        [students, _] = await connection.query(sqlQuery);

        sqlQuery =
            `SELECT id
             FROM faculty`;
        [faculty, _] = await connection.query(sqlQuery);

        let response = {status: true, facultyID: faculty, studentID: students};

        console.log("Success, ", response);
        res.send(response);
    } catch (err) {
        console.log(err, '- Error !!!!!!!!!!!!!!!!');
        res.send({status: false, errMsg: err});
    }
}

async function handleTest(req, res) {
    try {
        console.log("Got request", req.body);

        // TODO validate request
        const schema = Joi.object({});

        let check = schema.validate({});
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