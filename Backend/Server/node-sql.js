const express = require('express');
const mysql = require('mysql2/promise');
const PORT = 3002;
const mySqlConfig = {
    host: 'localhost',
    user: 'root',
    password: 'sql*db*admin',
    database: 'research_mgmt'
};

start_service().then(r => r);

async function start_service() {
    try {
        const app = express();

        app.get('/', handleGet);

        app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
    } catch (err) {
        console.log(err, '- Error !!!!!!!!!!!!!!!!');
    }

}

async function handleGet(req, res) {
    try {
        let connection = await getConnection();
        let [result, fields] = await connection.execute("show tables");
        console.log(result, fields);
        res.send('Hello World!');
    } catch (err) {
        res.send({fail: true});
    }
}

async function getConnection() {
    return await mysql.createConnection(mySqlConfig);
}