const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const path = require('path');

const app = express();
const port = 8080;

// Middleware
app.use(express.json());
app.use(express.static('public'));

// Database initialization
function initDb() {
    const db = new sqlite3.Database('people.db');
    // TODO: Create your database schema here
    // Example: db.run('CREATE TABLE IF NOT EXISTS people (...)');
    db.close();
}

// Initialize database
initDb();

// Serve the main page
app.get('/', (req, res) => {
    res.send(`
        <!DOCTYPE html>
        <html>
            <head>
                <title>People Directory</title>
            </head>
            <body>
                <h1>People Directory</h1>
                <p>Implement CRUD operations for people</p>
                <!-- TODO: Add your form and table here -->
            </body>
        </html>
    `);
});

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
}); 