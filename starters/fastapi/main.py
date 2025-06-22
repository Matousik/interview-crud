from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import sqlite3

app = FastAPI()

# Database initialization
def init_db():
    conn = sqlite3.connect('people.db')
    cursor = conn.cursor()
    # TODO: Create your database schema here
    conn.commit()
    conn.close()

# Initialize database on startup
@app.on_event("startup")
async def startup_event():
    init_db()

@app.get("/", response_class=HTMLResponse)
async def root():
    return """
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
    """