# Secure Authentication System

A secure authentication system built using Flask, JWT, bcrypt, and PostgreSQL.

## Features
- User Registration
- User Login
- JWT Authentication
- Protected Routes
- Password Hashing
- PostgreSQL Database

## Technologies Used
- Python
- Flask
- Flask-JWT-Extended
- bcrypt
- PostgreSQL
- SQLAlchemy

## API Routes

### Register
POST /register

### Login
POST /login

### Dashboard
GET /dashboard
Requires JWT Token

## Run Project

```bash
python3 app.py