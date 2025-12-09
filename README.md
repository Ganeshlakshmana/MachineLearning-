## END to END Machine Learning project
This project demonstrates a complete, production-grade Machine Learning pipeline, starting from data ingestion to final deployment on cloud platforms such as AWS Elastic Beanstalk, AWS EC2 (with ECR)
- It includes modularized Python code, reusable components, robust logging, exception handling, and automated model training pipelines.
## Project Structure
.
├── .ebextensions/              # AWS Beanstalk configuration files
├── artifacts/                  # Saved artifacts (models, transformers, data)
├── catboost_info/              # CatBoost training logs
├── notebook/                   # Notebooks for EDA and experimentation
├── src/                        # Main ML pipeline source code
│   ├── components/             # Data ingestion, transformation, training modules
│   ├── pipeline/               # Training and prediction pipelines
│   ├── utils/                  # Utility functions
│   ├── logger.py               # Logging configuration
│   ├── exception.py            # Custom Exception handler
│   ├── __init__.py
├── templates/                  # HTML templates for prediction app
├── app.py                      # Flask entrypoint for deployment
├── application.py              # Alternate entrypoint for AWS
├── requirements.txt            # Dependencies
├── setup.py                    # Package configuration
├── README.md                   # Project documentation
└── .gitignore

## Project Overview
This ML project covers the following steps:
# Data Ingestion
Reads raw dataset

Handles missing values

Splits into train/test

Stores artifacts in /artifacts/
# Data Transformation
Implements Scikit-learn Pipelines

Handles scaling, encoding, outliers

Generates transformation pickle files

# Model Training

Trains multiple models

Evaluates performance using metrics

Saves best model

# Hyperparameter Tuning

Implements GridSearch / RandomizedSearch

Optimizes best model parameters

# Prediction Pipeline

Loads saved model and transformer

Predicts on new data through UI or API

--------------------------------------------------------------------------------------------------------------
## Tech Stack
# Languages & Libraries

Python

NumPy

Pandas

Scikit-Learn

CatBoost

Flask

Logging, Exception Handling

Cloud & Deployment

AWS Elastic Beanstalk

AWS EC2 + Docker + Amazon ECR

## Deployment Steps
#  AWS Elastic Beanstalk Deployment

Added .ebextensions/ with config files

requirements.txt prepared

application.py used as entry point

Deployment via ZIP upload or EB CLI

# AWS EC2 + Docker + ECR

Created Docker image

Pushed to AWS ECR

Pulled image and deployed on EC2

Configured security groups & load balancing

# Azure Container Deployment

Built Docker image locally

Pushed to Azure Container Registry

Deployed using Azure Container Apps

## Running Project Locally
Clone repository
git clone https://github.com/Ganeshlakshmana/MachineLearning-.git
cd <repo-name>

Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

Install dependencies
pip install -r requirements.txt

Run application
python app.py

## Training Pipeline

Run the training pipeline manually:

python src/pipeline/training_pipeline.py
This will:
ingest data
transform data
train model
save artifacts

## Key Features

Fully modularized ML pipeline

Clean folder structure

Automatic logging & error handling

Docker-based deployment

Multi-cloud deployment (AWS + Azure)

HTML UI for user predictions

## Contributing

Feel free to fork the repo and submit pull requests.

# Contact

## Author: Ganeshlakshmana
For queries or improvements, open an issue or ping me on GitHub
or 
on Linkedin : https://www.linkedin.com/in/ganesh-lakshmana-71085b224/.
