const express = require('express');
const cors = require('cors');
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

async function getConnection() {
    return await mysql.createConnection(SQLCONFIG);
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
        }

        // TODO MySql interaction
        let connection = await getConnection();
        let [result, fields] = await connection.execute(
            "select * from paper"
        );

        let response = {status: result};

        console.log("Success, ", response);
        res.send(response);
    } catch (err) {
        console.log(err, '- Error !!!!!!!!!!!!!!!!');
        res.send({invalidRequest: false, status: false, errMsg: err});
    }
}

async function handleLogin(req, res) {
    try {
        console.log("Got request", req.body);

        let invalid_request = false;
        if (!req.body.hasOwnProperty("id") ||
            !req.body.hasOwnProperty("pwd") ||
            (req.body.id.length !== 8 && req.body.id.length !== 13)) {
            invalid_request = true;
        }
        if (invalid_request) {
            let response = {invalidRequest: true, status: false, errMsg: "refer API properly"};
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
                "select `srn`, `password` from `student` where `srn` = ?",
                [req.body.id]
            );
        } else {
            [result, _] = await connection.execute(
                "select `id`, `password` from `faculty` where `id` = ?",
                [req.body.id]
            );
        }

        let found = false;
        let valid = false;

        if (result.length !== 0){
            found = true;
            let actual_pwd = result[0].password;
            if (actual_pwd === req.body.pwd){
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
        if (!req.body.hasOwnProperty("id") ||
            !req.body.hasOwnProperty("pwd") ||
            !req.body.hasOwnProperty("type") ||
            !(req.body.type.toLowerCase() in ['student', 'faculty']) ||
            !req.body.hasOwnProperty("details")) {
            res.send({invalidRequest: true, status: false, errMsg: "refer API properly"});
        }

        let user_details = req.body.details;
        if (!user_details.hasOwnProperty("firstName") ||
            !user_details.hasOwnProperty("lastName") ||
            !user_details.hasOwnProperty("dept") ||
            !(user_details.dept.toLowerCase() in ['cse', 'ece', 'eee', 'aiml', 'me'])) {
            res.send({invalidRequest: true, status: false, errMsg: "refer API properly"});
        }

        // TODO mysql create

        let response = {
            status: true
        }

        console.log("Sending, ", response);
        res.send(response);
    } catch (err) {
        console.log(err, '- Error !!!!!!!!!!!!!!!!');
        res.send({invalidRequest: false, status: false, errMsg: err});
    }
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