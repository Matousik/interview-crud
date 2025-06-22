# FastAPI Starter

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python main.py
```

Or with uvicorn:
```bash
uvicorn main:app --host 0.0.0.0 --port 8080 --reload
```

3. Open your browser:
Navigate to `http://localhost:8080`

4. API documentation:
Navigate to `http://localhost:8080/docs`

## What's included

- Basic FastAPI server setup
- SQLite database connection
- Simple HTML response
- Database initialization function

## Next steps

- Design your database schema in the `init_db()` function
- Create API endpoints for CRUD operations
- Build the frontend interface
- Add Pydantic models for data validation 