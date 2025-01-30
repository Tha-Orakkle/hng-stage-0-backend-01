# SIMPLE REST API TO RETRIEVE BASIC INFORMATION

## Description

A basic REST API that returns basic information including the email, current datetime and the github url of project codebase.

### Set Up Instructions
1. Clone the repository:
```bash
git clone https://github.com/Tha-Orakkle/hng-stage-0-backend-01.git
cd hng-stage-0-backend-01
```
2. Create and activate virtual environment:
```bash
virtualenv venv
```
- Windows
```bash
.\venv\Scripts\activate.bat
```
- Linux
```bash
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations
```bash
python manage.py migrate
```

### Usage 
To start the server, run:
```bash
python manage.py runserver
```

The API will be available at ``.


## API Documentation

- Endpoint: `GET /api/users`
- Response Format:
```json
{
    "email": "adegbiranayinoluwa.paul@yahoo.com",
    "current_datetime": "2025-01-29T12:00:00Z",
    "github_url": "https://github.com/Tha-Orakkle/hng-stage-0-backend-01"
}
```

## Additional Information

[Hire Python Backend Developers](https://hng.tech/hire/python-developers)
