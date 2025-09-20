# 🏨 Hotel Reservation Cancellation Prediction

This project focuses on **predicting whether a hotel guest will cancel their reservation** based on various booking and customer-related factors. The goal is to build a machine learning model that helps hotels reduce revenue loss and optimize resource management by identifying high-risk bookings in advance.

---

## 🔍 Project Overview

Guest cancellations are a major challenge in the hospitality industry. This project uses a dataset containing booking details, customer demographics, and stay information to predict reservation cancellations. The project covers the full machine learning workflow, from data preprocessing and analysis to model evaluation and selection.

---

## 🛠️ Data Preprocessing

To ensure high-quality inputs for modeling, the following preprocessing steps were performed:  

- **Handling missing values:** Cleaned and imputed missing data.  
- **Encoding categorical variables:** Converted non-numeric features such as hotel type, meal plan, and customer type into numeric formats suitable for ML algorithms.  
- **Feature scaling:** Standardized numerical features like price, number of adults, and week nights for consistent model performance.  
- **Balancing the dataset:** Applied techniques to address class imbalance and ensure fair prediction of cancellations.  

---

## 📊 Exploratory Data Analysis (EDA)

EDA helped understand the data and identify key patterns affecting cancellations:  

- Visualizations of booking patterns and customer demographics  
- Analysis of correlations between features like room price, stay duration, number of adults, and cancellation likelihood  
- Insights into the most influential factors affecting guest behavior  

---

## 🧩 Feature Engineering

- Created new features to capture important relationships in the data (e.g., total stay nights, total number of guests)  
- Selected relevant features to reduce noise and improve model accuracy  

---

## 🤖 Machine Learning Models

Multiple machine learning models were trained and compared to identify the best approach:  

- Logistic Regression  
- Random Forest Classifier  
- Gradient Boosting / XGBoost  
- Support Vector Machine (SVM)  
- K-Nearest Neighbors (KNN)  

Each model was tuned and evaluated to maximize prediction performance.

---

## 📈 Model Evaluation

The models were evaluated using:  

- **Precision:** To measure the accuracy of predicted cancellations  
- **Recall:** To assess the model’s ability to identify actual cancellations  
- **F1-Score:** To balance precision and recall for overall performance  
- **Confusion Matrix:** To visualize true positives, true negatives, false positives, and false negatives  

The best-performing model was selected based on its performance across these metrics.

---

## ⚡ Conclusion

This project demonstrates an **end-to-end machine learning workflow** for predicting hotel reservation cancellations. It highlights the importance of thorough data preprocessing, feature engineering, and model evaluation to deliver accurate predictive solutions that can help hotels improve operational efficiency and revenue management.
