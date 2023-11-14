const express = require('express');
const cors = require('cors');
const PORT = 6969;

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
        app.post('/ProjectList/', handleProjectList);
        console.log("Set up express.")

        app.listen(PORT, () => console.log(`Listening On Port ${PORT}...`))
    } catch (err) {
        console.log(err);
    }
}

async function handleLogin(req, res) {
    try {
        console.log("Got request", req.body);
        if (!req.body.hasOwnProperty("usrName") ||
            !req.body.hasOwnProperty("usrPwd")) {
            throw new Error("Invalid Request");
        }
        let response = {
            valid: true,
            type: "student"
        }
        console.log("Sending, ", response);
        res.send(response);
    } catch (err) {
        console.log(err, '- Error :(');
        res.status(500).send();
    }
}

async function handleRegister(req, res) {
    try {
        console.log("Got request", req.body);
        if (!req.body.hasOwnProperty("usrName") ||
            !req.body.hasOwnProperty("usrPwd") ||
            !req.body.hasOwnProperty("type")) {
            throw new Error("Invalid Request");
        }
        let response = {
            status: true
        }
        console.log("Sending, ", response);
        res.send(response);
    } catch (err) {
        console.log(err, '- Error :(');
        res.status(500).send();
    }
}

async function handleProjectList(req, res) {
    try {
        console.log("Got request", req.body);
        if (!req.body.hasOwnProperty("usrName") ||
            !req.body.hasOwnProperty("type")) {
            throw new Error("Invalid Request");
        }
        let response = {
            ProjectList: [
                {
                    ProjectID: "123",
                    ProjectTitle: "hi",
                    ProjectStatus: "Ongoing",
                    FacultyID: "pescs32",
                    FacultyName: "Sudeepa"
                },
                {
                    ProjectID: "124",
                    ProjectTitle: "bye",
                    ProjectStatus: "never going to finish",
                    FacultyID: "pescs34",
                    FacultyName: "srinath"
                },
                {
                    ProjectID: "125",
                    ProjectTitle: "shit",
                    ProjectStatus: "done",
                    FacultyID: "pescs45",
                    FacultyName: "Niveditha"
                }
            ]
        }
        console.log("Sending, ", response);
        res.send(response);
    } catch (err) {
        console.log(err, '- Error :(');
        res.status(500).send();
    }
}