# Predictive Vehicle Health Maintenance

## Overview

Predictive Vehicle Health Maintenance is a machine learning-based system designed to predict the health status of vehicle components using service data. The system enables proactive maintenance by identifying potential failures before they occur.

## Abstract

The system analyzes vehicle usage patterns and predicts component health using machine learning models. It incorporates feature engineering techniques such as estimated usage and remaining life to model component degradation. The implementation combines dataset generation, model training, evaluation, and dashboard visualization.

## Problem Statement

Fleet operations depend on continuous vehicle availability. Unexpected component failures result in delays, increased operational costs, and reduced efficiency. Traditional maintenance approaches are reactive. This project aims to develop a predictive system that evaluates component usage and estimates remaining life to identify failures in advance.

## Proposed System

- Machine learning-based prediction of component health  
- Feature engineering using usage and lifecycle metrics  
- Comparison of multiple classification models  
- Selection of an optimal model for deployment  
- Interactive dashboard for real-time prediction  

## System Architecture

1. Data Layer  
   Synthetic dataset representing vehicle service records  

2. Processing Layer  
   Feature engineering and preprocessing using Python  

3. Model Layer  
   Machine learning models for classification  

4. Presentation Layer  
   Streamlit dashboard for user interaction  

## Technology Stack

### Programming Language
- Python  

### Data Processing and Machine Learning
- Pandas  
- NumPy  
- Scikit-learn  
- XGBoost  

### Exploratory Data Analysis
- Power BI  

### Dashboard Visualization
- Altair  
- Matplotlib  

### Dashboard and Deployment
- Streamlit  

### Development Tools
- Visual Studio Code  

## Dataset Design

A synthetic dataset was generated using Python to simulate real-world vehicle service records.

The dataset includes multiple entities such as vehicles, service records, components, and usage patterns. It was designed to reflect realistic maintenance scenarios and support feature engineering for predictive modeling.

## Exploratory Data Analysis

Exploratory Data Analysis was performed using Power BI to understand patterns in vehicle service data.

The analysis included:

- Service trends over time  
- Distribution of mileage and component usage  
- Remaining life analysis across components  
- Classification of component health status  
- Identification of patterns indicating potential failures  

Power BI dashboards were used to visualize relationships between features and support feature engineering decisions.
The Power BI dashboard file (.pbix) used for analysis is included in the repository.

### Attributes

- Vehicle Type  
- Component  
- Mileage  
- Quantity_Used  
- Estimated_Usage_km  
- Remaining_Life_km  
- Health_Status  

### Feature Engineering

Estimated_Usage_km = Mileage × Quantity_Used  

Remaining_Life_km = Expected_Life_km − Estimated_Usage_km  

## Machine Learning Models

- Logistic Regression  
- Random Forest  
- XGBoost  
- Naive Bayes  

These models were selected to provide a balanced comparison across baseline, ensemble, and probabilistic approaches.

## Model Performance

| Model               | Accuracy | Precision | Recall | F1 Score |
|---------------------|----------|-----------|--------|----------|
| Logistic Regression | 1.000    | 1.000     | 1.000  | 1.000    |
| Random Forest       | 1.000    | 1.000     | 1.000  | 1.000    |
| XGBoost             | 1.000    | 1.000     | 0.998  | 0.999    |
| Naive Bayes         | 0.966    | 0.937     | 0.953  | 0.945    |

## Results

The models demonstrated strong performance on the dataset.

- Random Forest and Logistic Regression achieved perfect scores across all metrics  
- XGBoost performed similarly with a minor variation in recall and F1 score  
- Naive Bayes showed comparatively lower performance  

These results indicate that ensemble models are more suitable for this structured dataset.

## Final Model Selection

Random Forest was selected as the final model because:

- Strong performance across evaluation metrics  
- Suitable for structured tabular data  
- Captures non-linear relationships  
- More robust than baseline models  
- Provides feature importance for interpretability  

## System Workflow

1. User selects vehicle type and component  
2. User inputs mileage and quantity used  
3. System calculates estimated usage and remaining life  
4. Data is passed to the trained model  
5. Model predicts component health status  
6. Results are displayed through the dashboard  

## Key Features

- Predictive analysis of vehicle component health  
- Feature engineering based on usage patterns  
- Comparison of multiple machine learning models  
- Interactive dashboard interface  
- Visualization of model performance and feature importance  

## Conclusion

This project demonstrates the application of machine learning for predictive maintenance. By combining structured data, feature engineering, model evaluation, and visualization, the system provides a practical approach to improving maintenance planning and reducing unexpected failures. The system can be extended further using real-world data and advanced predictive techniques for improved generalization.

## References

- Scikit-learn Documentation  
- XGBoost Documentation  
- Streamlit Documentation  
- Pandas Documentation  

## Contributing

Contributions are welcome. Suggestions, improvements, or issues can be submitted through pull requests or issue tracking.


## Live Application

[[Open RailServe on Streamlit](https://predictive-vehicle-health-maintenance.streamlit.app/)

## Author

Anvita Arun  
II Year B.Tech CSE  
VIT Chennai
