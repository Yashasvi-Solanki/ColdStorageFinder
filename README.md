# ColdStorageFinder

A platform to find and manage agricultural cold storage facilities.

## Overview
This repository contains the backend and frontend components for the ColdStorageFinder platform. 

## 🚀 Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You will need the following installed on your machine:
* Python 3.8+
* PostgreSQL
* pgAdmin (or any PostgreSQL GUI/CLI)

### 1. Database Setup (The "Blueprint")

This project requires a PostgreSQL database to run locally. We have provided a SQL script to automatically create the necessary tables and populate initial seed data.

1. Open **pgAdmin** and connect to your local PostgreSQL server.
2. Create a new database named `agristorage` (or any name you prefer).
3. Open the Query Tool for your new database.
4. Open the `database_setup.sql` file included in this repository, copy its contents, and run it in the Query Tool.
   * *This will instantly recreate the exact database schema and insert the initial 10 storage records onto your machine.*

### 2. Environment Variables Configuration

For security reasons, database passwords and credentials are never uploaded to GitHub. You must create your own configuration file locally.

1. In the root directory of the project, locate the file named `.env.example`.
2. Duplicate this file and rename the copy to exactly `.env` (note the leading dot).
3. Open the new `.env` file and fill in your local PostgreSQL credentials:

```env
DB_HOST=localhost
DB_NAME=agristorage
DB_USER=postgres
DB_PASSWORD=your_actual_postgres_password_here
DB_PORT=5432
```

> **Note:** The `.env` file is ignored by Git (`.gitignore`) to ensure your personal passwords remain secure and are not pushed to the repository.

### 3. Running the Application

1. **Create and activate a virtual environment (recommended):**
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

2. **Install the dependencies:**
   *(If you have a requirements file, use the command below)*
   ```bash
   pip install -r requirements.txt
   ```

3. **Start the server:**
   ```bash
   python main.py
   ```

## Support
If you encounter any issues connecting to the database, double-check your `.env` credentials and ensure PostgreSQL is actively running on your machine.
