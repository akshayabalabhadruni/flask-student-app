# Flask Student Management API

A lightweight web application built with Python and Flask to manage and retrieve student records. This project demonstrates backend development fundamentals, RESTful API routing, and direct database interaction using SQLite.

## Features
* **Microframework Architecture:** Built entirely on Flask without heavy external ORMs.
* **Database Management:** Uses Python's built-in `sqlite3` library for raw SQL execution.
* **Automated Setup:** Includes a dedicated initialization script to build and seed the database instantly.
* **JSON Responses:** Fetches database rows and returns serialized JSON data for frontend consumption.

## Project Structure
* `app.py`: The main Flask server containing application configuration and API routing logic.
* `init_db.py`: A setup script that drops existing tables, creates the `students` table, and inserts sample data.
* `database.db`: The SQLite database file generated locally after running the initialization script.

## Setup Instructions

**1. Clone the repository**
```bash
git clone [https://github.com/akshayabalabhadruni/flask-student-app.git](https://github.com/akshayabalabhadruni/flask-student-app.git)
cd flask-student-app
