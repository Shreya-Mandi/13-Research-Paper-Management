const express = require('express');
const cors = require('cors');
const PORT = 3002;

StartService();

async function StartService() {
    try {

        console.log("Setting up express...")
        const app = express();

        app.use(cors());
        app.use(express.json());
        app.use(express.urlencoded({extended: true}));

        app.post('/Login/', handleLogin);
        app.post('/Register/', handleRegister);

        console.log("Set up express.")

        app.listen(PORT, () => console.log(`Listening On Port ${PORT}...`))
    } catch (err) {
        console.log(err);
    }
}

async function handleLogin(req, res) {
    try {
        console.log("Got request", req.body);
        if (!req.body.hasOwnProperty("id") ||
            !req.body.hasOwnProperty("pwd")) {
            res.send({invalidRequest: true, status: false, errMsg: "refer API properly"});
        }

        // TODO mysql read and validate
        let found = false;
        let valid = false;
        let typeOfUsr = "student";

        let response = {
            status: true,
            found: found,
            valid: valid,
            type: typeOfUsr
        };

        console.log("Sending, ", response);
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
