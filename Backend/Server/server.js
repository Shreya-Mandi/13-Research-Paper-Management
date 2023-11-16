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

        app.get('/Test/', handleTest);                        // working
        app.get('/NewDb/', handleTemplate);
        app.get('/InsDb/', handleTemplate);
        app.get('/ClsDb/', handleTemplate);
        app.get('/DelDb/', handleTemplate);

        app.post('/Login/', handleLogin);                // working
        app.post('/Register/', handleRegister);

        app.post('/GetProjects/', handleTemplate);

        app.post('/NewProject/', handleTemplate);
        app.post('/GetProject/', handleTemplate);
        app.post('/UpdProject/', handleTemplate);
        app.post('/DelProject/', handleTemplate);

        app.post('/NewMeeting/', handleTemplate);
        app.post('/GetMeetings/', handleTemplate);
        app.post('/UpdMeeting/', handleTemplate);

        app.post('/NewSuggestions/', handleTemplate);
        app.post('/GetSuggestions/', handleTemplate);

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
                    return helper.message("invalid ID")
                }
            }).required(),
            pwd: Joi.string().min(5).required()
        })

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
        if (req.body.id.length === 8) {
            typeOfUsr = "faculty";
        }

        let result, _, connection = await getConnection();
        if (typeOfUsr === "student") {
            [result, _] = await connection.execute(
                "SELECT `srn`, `password` FROM `student` WHERE `srn` = ?",
                [req.body.id]
            );
        } else {
            [result, _] = await connection.execute(
                "SELECT `id`, `password` FROM `faculty` WHERE `id` = ?",
                [req.body.id]
            );
        }

        let found = false;
        let valid = false;
        if (result.length !== 0) {
            found = true;
            let actual_pwd = result[0].password;
            if (actual_pwd === req.body.pwd) {
                valid = true;
            }
        }

        let response = {
            status: true,
            found: found,
            valid: valid,
            type: typeOfUsr
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

        let invalid_request = false;
        if (!req.body.hasOwnProperty("id") ||
            !req.body.hasOwnProperty("pwd") ||
            !req.body.hasOwnProperty("type")) {
            // !(req.body.type.toLowerCase() in ['student', 'faculty'])
            // !req.body.hasOwnProperty("details") ||
            // !req.body.details.hasOwnProperty("firstName") ||
            // !req.body.details.hasOwnProperty("lastName") ||
            // !req.body.details.hasOwnProperty("dept") ||
            // !(req.body.details.dept.toLowerCase() in ['cse', 'ece', 'eee', 'aiml', 'me']) ||
            // (req.body.type === 'student' && (
            //     !req.body.details.hasOwnProperty("sem") ||
            //     !req.body.details.hasOwnProperty("sec")
            // )) ||
            // (req.body.type === 'faculty' && (
            //     !req.body.details.hasOwnProperty("domain")
            // ))) {
            invalid_request = true;
        }

        if (invalid_request) {
            let response = {invalidRequest: true, status: false, errMsg: "refer API properly"};
            console.log("InvalidRequest, ", response);
            res.send(response);
            return;
        }

        let result, _, connection = await getConnection();

        if (req.body.type === "student") {
            // [result, _] = await connection.execute(
            //     "INSERT INTO `student` VALUES (?, ?, ?, ?, ?, ?, ?)",
            //     [
            //         req.body.id,
            //         req.body.details.firstName,
            //         req.body.details.lastName,
            //         req.body.details.dept.toUpperCase(),
            //         req.body.details.sem,
            //         req.body.details.sec,
            //         req.body.pwd
            //     ]
            // );
            // console.log(result, _);
            console.log('passed')
        } else {
            [result, _] = await connection.execute(
                "INSERT INTO `faculty` VALUES (?, ?, ?, ?, ?, ?, ?)",
                [
                    req.body.id,
                    req.body.details.firstName,
                    req.body.details.lastName,
                    req.body.details.dept.toUpperCase(),
                    req.body.details.domain,
                    req.body.pwd
                ]
            );
            console.log(result, _);
        }

        let response = {status: true};

        console.log("Success, ", response);
        res.send(response);
    } catch
        (err) {
        console.log(err, '- Error !!!!!!!!!!!!!!!!');
        res.send({invalidRequest: false, status: false, errMsg: err});
    }
}

async function handleTest(req, res) {
    try {
        console.log("Got request", req.body);

        let invalid_request = false;
        // TODO Validate Request
        if (invalid_request) {
            let response = {invalidRequest: true, status: false, errMsg: "refer API properly"};
            console.log("InvalidRequest, ", response);
            res.send(response);
            return;
        }

        // TODO MySql interaction
        let result, _, connection = await getConnection();
        [result, _] = await connection.execute(
            "SHOW TABLES"
        );

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

async function handleTemplate(req, res) {
    try {
        console.log("Got request", req.body);

        let invalid_request = false;
        // TODO Validate Request
        if (invalid_request) {
            let response = {invalidRequest: true, status: false, errMsg: "refer API properly"};
            console.log("InvalidRequest, ", response);
            res.send(response);
            return;
        }

        // TODO MySql interaction
        let response = {status: true};

        console.log("Success, ", response);
        res.send(response);
    } catch (err) {
        console.log(err, '- Error !!!!!!!!!!!!!!!!');
        res.send({invalidRequest: false, status: false, errMsg: err});
    }
}