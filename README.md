# Student-Staff CRUD Operations

A Python-based command-line application for performing **CRUD (Create, Read, Update, Delete)** operations on `student` and `staff` databases. Built using **MySQL Connector** for seamless interaction with the MySQL database.

---

## Features

- **Dynamic Table Creation**: Automatically creates `student` and `staff` tables if they don't already exist.
- **CRUD Operations**:
  - **Create**: Add new records to the database.
  - **Read**: Retrieve and display all records from the database.
  - **Update**: Modify existing records based on a unique identifier.
  - **Delete**: Remove records using a unique identifier.
- **SQL Injection Prevention**: Uses parameterized queries for enhanced security.
- **User-Friendly Menu**: Intuitive CLI for seamless navigation.

---

## Technologies Used

- **Python**: Core programming language.
- **MySQL**: Database management system.
- **MySQL Connector**: Python library for interacting with MySQL.

---

## Prerequisites

1. **Python 3.x**: Ensure Python is installed. [Download Python](https://www.python.org/downloads/)
2. **MySQL Server**: Set up MySQL Server and ensure it's running.
3. **MySQL Connector**: Install the connector using pip:
   ```bash
   pip install mysql-connector-python
