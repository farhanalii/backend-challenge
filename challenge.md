
# Project Overview

The project aims to provide a RESTful API for managing tasks and labels. It allows users to perform CRUD operations on tasks and labels, with authentication provided by token-based authentication.

# Project Setup Guide and API Endpoints for Task and Label Management

Create python 3.11 virtual environment using the following command

```bash
python3 -m venv venv
```


Activate the virtual environment using the following command.

```bash
source venv/bin/activate
```

Install the requirements inside the virtual environment with the following command.

```bash
pip3 install -r requirements.txt
```

Execute the following commands for running the migraitons

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

Create django superusers with the following command

```bash
python3 manage.py createsuperuser
```

Start the development server using the following command.

```bash
python3 manage.py runserver
```

The server will be running and can be accessed at 
the following url

http://localhost:8000/admin

### User Credentials

This document contains credentials for accessing the system.

#### Admin User
- **Username:** farhanalise
- **Password:** admin

### Test Users
#### User 1
- **Username:** user1
- **Password:** password1

##### User 2
- **Username:** user2
- **Password:** password2

## API Endpoints for Task and Label Management

This guide provides an overview of the project's API endpoints for managing tasks and labels, including authentication via the `/api/token` endpoint.

## API Endpoints

### Authentication

- **Endpoint:** `/api/token`
  - **Method:** POST
  - **Description:** Obtain a token for authentication.
  - **Payload:** 
    - `username`: User's username
    - `password`: User's password
  - **Response:** 
    - `token`: JWT token for authentication

### Task Management

- **Endpoint:** `/api/tasks/`
  - **Method:** 
    - GET: Retrieve all tasks
    - POST: Create a new task
  - **Response (GET):** 
    - List of tasks with details
  - **Payload (POST):** 
    - `title`: Title of the task
    - `description`: Description of the task
    - `labels` (optional): List of labels associated with the task
  - **Response (POST):** 
    - Details of the created task

- **Endpoint:** `/api/tasks/<task_id>/`
  - **Method:** 
    - GET: Retrieve details of a specific task
    - PUT: Update details of a specific task
    - DELETE: Delete a specific task
  - **Response (GET/PUT):** 
    - Details of the task
  - **Payload (PUT):** 
    - Updated details of the task
  - **Response (DELETE):** 
    - Confirmation of task deletion

### Label Management

- **Endpoint:** `/api/labels/`
  - **Method:** 
    - GET: Retrieve all labels
    - POST: Create a new label
  - **Response (GET):** 
    - List of labels with details
  - **Payload (POST):** 
    - `name`: Name of the label
  - **Response (POST):** 
    - Details of the created label

- **Endpoint:** `/api/labels/<label_id>/`
  - **Method:** 
    - GET: Retrieve details of a specific label
    - PUT: Update details of a specific label
    - DELETE: Delete a specific label
  - **Response (GET/PUT):** 
    - Details of the label
  - **Payload (PUT):** 
    - Updated details of the label
  - **Response (DELETE):** 
    - Confirmation of label deletion

## Usage Instructions

1. **Authentication:**
   - Obtain a JWT token by sending a POST request to `/api/token` with valid credentials.

2. **Task Management:**
   - Use `/api/tasks/` endpoints for CRUD operations on tasks.

3. **Label Management:**
   - Use `/api/labels/` endpoints for CRUD operations on labels.