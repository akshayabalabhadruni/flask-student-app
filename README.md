# Flask Student Management API

A lightweight web application built with Python and Flask to manage and retrieve student records. This project demonstrates backend development fundamentals, RESTful API routing, and direct database interaction using SQLite.

## Core Technologies
* **Framework:** Flask (Python)
* **Database:** SQLite (built-in `sqlite3` library)
* **Architecture:** Microframework with direct SQL execution

## Project Structure
* `app.py`: The main Flask server containing application configuration and API routing logic.
* `init_db.py`: A setup script that drops existing tables, creates the `students` table, and inserts sample data.
* `database.db`: The SQLite database file generated locally after running the initialization script.

## Setup Instructions

**1. Clone the repository**
```bash
git clone [https://github.com/akshayabalabhadruni/flask-student-app.git](https://github.com/akshayabalabhadruni/flask-student-app.git)
cd flask-student-app
```

**2. Install dependencies**
Make sure Python is installed, then install Flask:
```bash
pip install flask
```

**3. Initialize the database**
Run the setup script to generate the `database.db` file with initial student records:
```bash
python init_db.py
```

**4. Start the server**
Launch the Flask development server:
```bash
python app.py
```

**5. Test the API**
Open your web browser and navigate to:
`http://127.0.0.1:5000/students`
