
## Project Setup Guide

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

http://localhost:8000

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