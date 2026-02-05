# Flipkart Review Sentiment Analysis

A Machine Learning–powered web application for real-time sentiment classification of Flipkart product reviews, built using Natural Language Processing (NLP) and deployed with Streamlit.

## Live Application

(Add after deployment)
https://your-app-name.streamlit.app

## Project Summary

Understanding customer feedback is critical for improving product quality and user satisfaction. This project implements an end-to-end Sentiment Analysis System that classifies Flipkart product reviews into Positive or Negative using Machine Learning and NLP techniques.

The solution includes:

Text preprocessing & feature engineering

ML pipeline (vectorization + model)

Real-time prediction interface using Streamlit

Production-ready deployment

## Objectives

Build a robust NLP-based sentiment classifier

Convert raw text into machine-understandable features

Select the best performing ML model using a pipeline

Deploy the trained model as an interactive web app

Enable real-time user review sentiment prediction

## Machine Learning Workflow

Data Collection – Flipkart Product Reviews Dataset

Text Preprocessing – Cleaning, normalization, noise removal

Feature Engineering – TF-IDF / Count Vectorization

Model Training – Multiple algorithms tested

Model Selection – Best performing model chosen using Pipeline

Model Evaluation – Accuracy, Precision, Recall, F1-Score

Deployment – Streamlit Web Application

## Model Performance
Metric	Value
Accuracy	88%
Model Type	Machine Learning Pipeline
Algorithms Tested	Logistic Regression, Naive Bayes, SVM
Final Model	Best performing classifier from pipeline
## Technology Stack

Programming Language: Python

Machine Learning: Scikit-learn

NLP Techniques: Text Cleaning, Tokenization, Vectorization

Data Handling: Pandas, NumPy

Visualization: Matplotlib, Seaborn (during analysis)

Deployment: Streamlit

Model Serialization: Pickle

## Project Structure
flipkart-sentiment-analysis/
│
├── app.py                 # Streamlit application
├── flipkart.pkl           # Trained ML Pipeline (Vectorizer + Model)
├── requirements.txt       # Project dependencies
├── README.md              # Project documentation

### Deployment

The application is deployed on Streamlit Cloud for real-time sentiment prediction.

## Future Enhancements

Multi-class sentiment classification (Positive / Neutral / Negative)

Bulk prediction via CSV upload

Interactive sentiment dashboard & visualization

Deep Learning models (LSTM / Transformers)

Hyperparameter tuning & accuracy improvement

Model monitoring and logging

# Author
Bathula Venu Gopal
Data Science Intern @ Innomatics Research Labs
Former Amazon ML Data Associate
Focus Areas: Machine Learning, Data Analytics & Model Deployment
