# Creating a README.md file with the provided content

readme_content = """
# Assignment Submission Portal

This project is a backend system for an assignment submission portal that supports two types of users: **Admins** and **Users**. The system allows users to upload assignments and admins to accept or reject those assignments.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [Environment Variables](#environment-variables)
- [API Endpoints](#api-endpoints)
  - [User Endpoints](#user-endpoints)
  - [Admin Endpoints](#admin-endpoints)
- [Running the Application](#running-the-application)
- [Sample Requests](#sample-requests)
- [Future Improvements](#future-improvements)

## Features
- User registration and login
- Admin registration and login
- Assignment upload by users
- Viewing assignments tagged to specific admins
- Admins can accept or reject assignments
- JWT-based authentication for secure access
- Modular code structure for scalability

## Technologies Used
- **Python**: Programming language used for the backend
- **Flask**: Web framework for building the REST API
- **MongoDB**: NoSQL database used for storing user, admin, and assignment data
- **PyMongo**: Python library for interacting with MongoDB
- **Flask-JWT-Extended**: Library for JWT-based authentication
- **bcrypt**: For password hashing and verification

## Project Structure

## Install Dependencies
pip install -r requirements.txt

## Set up MongoDB
Make sure MongoDB is running locally or use a cloud-based MongoDB service like MongoDB Atlas.
Update the MONGO_URI in config.py if needed.

## Environment variables
Create a .env file in the root directory and set the following environment variables

# Run the application

python app.py

## User Endpoints

localhost url : " http://127.0.0.1:5000"
## Use postman for testing the apis
POST /user/register
POST /user/login
POST /user/upload
GET /user/admins

## Admin Endpoints
localhost url : " http://127.0.0.1:5000"
## Use postman for testing the apis
POST /admin/register
POST /admin/login
GET /admin/assignments
POST /admin/assignments/:id/accept
POST /admin/assignments/:id/reject