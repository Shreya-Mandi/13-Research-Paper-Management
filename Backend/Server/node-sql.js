const express = require('express');
const mysql = require('mysql2');

const db = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'sql*db*admin',
    database: 'research_mgmt'
});

db.connect((err) => {
    if (err) {
        throw err;
    }
    console.log('Connected to database');
    db.query("select * from paper", function (err, result, fields) {
        if (err) throw err;
        console.log(result);
    });
});

const app = express();

app.get('/', (req, res) => {
    res.send('Hello World!');
});

const PORT = 3002;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
