# CI/CD Pipeline Demo - Assignment 4

A complete CI/CD pipeline implementation for a Flask backend application with automated testing and deployment.

## Project Overview

This project demonstrates a full DevOps workflow including:

- **Build**: Automated dependency installation
- **Test**: Comprehensive unit tests with coverage reporting
- **Deploy**: Auto-deployment to Render on push to main branch
- **Automation**: GitHub Actions CI/CD pipeline

## Features

- Flask REST API with multiple endpoints
- Comprehensive unit tests using pytest
- Test coverage reporting
- GitHub Actions CI/CD workflow
- Render deployment configuration
- Professional project structure

## Project Structure

```
project/
├── app.py                 # Flask application
├── test_app.py           # Unit tests
├── requirements.txt      # Python dependencies
├── Procfile             # Render deployment config
├── .gitignore           # Git ignore rules
├── README.md            # This file
└── .github/
    └── workflows/
        └── ci.yml       # GitHub Actions workflow
```

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd project
```

2. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Running Tests Locally

```bash
# Run all tests
pytest test_app.py -v

# Run with coverage report
pytest test_app.py --cov=app --cov-report=term-missing
```

## Running the Application

```bash
python app.py
```

The application will start on `http://localhost:5000`

## API Endpoints

- `GET /` - Welcome message
- `GET /api/status` - Application status
- `GET /api/add/<a>/<b>` - Add two numbers

Example:

```bash
curl http://localhost:5000/api/add/5/3
# Response: {"result": 8}
```

## CI/CD Pipeline

The GitHub Actions workflow automatically:

1. Checks out the code
2. Sets up Python 3.9
3. Installs dependencies
4. Runs unit tests
5. Generates coverage reports
6. Deploys to Render (on push to main)

### Setting up GitHub Actions

The pipeline is configured in `.github/workflows/ci.yml` and runs automatically on:

- Push to `main` branch
- Pull requests to `main` branch

### Setting up Render Deployment

1. Push your code to GitHub
2. Create a new Web Service on Render
3. Connect your GitHub repository
4. Set the build command: `pip install -r requirements.txt`
5. Set the start command: `gunicorn app:app`
6. Deploy on every push to main

## Test Coverage

The pipeline includes comprehensive test coverage:

- Home endpoint tests
- Status endpoint tests
- Addition endpoint tests (positive, negative, zero values)
- Edge case testing

## Notes

- Update `requirements.txt` when adding new dependencies
- All tests must pass before deployment
- The pipeline runs on every push to the main branch
- Coverage reports are generated during CI/CD runs

## Assignment Completion

This project fulfills all requirements:
BACKEND app created (Flask)
UNIT tests implemented (pytest)
CI/CD pipeline configured (GitHub Actions)
AUTOMATED deployment ready (Render)
COMPLETE project structure

---

**Date Submitted:** 13th May
**Course:** DSO101 - Continuous Integration and Continuous Deployment
**Program:** Bachelor's of Engineering in Software Engineering (SWE)
