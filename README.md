# Loan Prediction Model Deployment using FastAPI

## Project Overview

This project demonstrates the deployment of a Machine Learning model using **FastAPI**.
The trained loan prediction model predicts whether a customer loan application will be **Approved or Rejected** based on user-provided details.

The project covers the complete ML deployment workflow:

* Data preprocessing
* Model training
* Model saving using Joblib
* API development using FastAPI
* Real-time prediction through REST API

---

# Features

* Machine Learning based loan approval prediction
* Fast and lightweight API using FastAPI
* REST API endpoints for prediction
* Input validation using Pydantic
* Trained model loading using Joblib
* Interactive API documentation using Swagger UI

---

# Technologies Used

## Programming Language

* Python

## Machine Learning

* Scikit-learn
* Pandas
* NumPy

## Model Deployment

* FastAPI
* Uvicorn

## Model Storage

* Joblib

## API Documentation

* Swagger UI
* ReDoc

---

# Project Structure

```
DAY8_TRAINING/
│
├── app.py                 # FastAPI application
├── train_model.py         # Model training script
├── dataset.csv            # Training dataset
├── loan_model.joblib      # Saved ML model
├── requirements.txt       # Required libraries
├── .gitignore             # Ignored files
└── README.md              # Project documentation
```

---

# Installation

## 1. Clone the Repository

```bash
git clone <repository-url>
```

## 2. Navigate to Project Folder

```bash
cd DAY8_TRAINING
```

## 3. Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

### Windows

```bash
venv\Scripts\activate
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Train the Model

Run the training file:

```bash
python train_model.py
```

This will generate:

```
loan_model.joblib
```

---

# Run the FastAPI Server

Start the API using Uvicorn:

```bash
uvicorn app:app --reload
```

Server will start at:

```
http://127.0.0.1:8000
```

---

# API Documentation

FastAPI automatically provides documentation.

## Swagger UI

```
http://127.0.0.1:8000/docs
```

## ReDoc

```
http://127.0.0.1:8000/redoc
```

---

# API Endpoints

## 1. Home Endpoint

### GET /

Checks whether the API is running.

### Request

```
GET /
```

### Response

```json
{
  "message": "Loan Prediction API is running"
}
```

---

# 2. Prediction Endpoint

### POST /predict

Predicts loan approval status.

### Request Example

```json
{
    "age": 30,
    "income": 50000,
    "loan_amount": 20000,
    "credit_score": 750
}
```

### Response Example

```json
{
    "prediction": "Loan Approved"
}
```

---

# How the API Works

```
Client
  |
  |
  ↓
FastAPI Server
  |
  |
  ↓
Pydantic Validation
  |
  |
  ↓
Machine Learning Model
  |
  |
  ↓
Prediction Response
```

---

# Future Improvements

* Deploy API on cloud platforms
* Add database integration
* Improve model accuracy
* Add authentication
* Create frontend interface

---

# Author

**Vidyanidhi G Shetty**

Computer Science Engineering
Data Science
