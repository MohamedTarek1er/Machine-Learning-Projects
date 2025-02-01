import numpy as np
import pandas as pd
import seaborn as sns
import string
import re
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from PreProcessing import preprocess
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm
import joblib

x_train_features, x_test_features, y_train, y_test, feature_extraction = preprocess('spam_ham_dataset.csv')

model = LogisticRegression()
model.fit(x_train_features, y_train)

prediction_on_training_data = model.predict(x_train_features)
accuracy_on_training_data = accuracy_score(y_train, prediction_on_training_data)

prediction_on_test_data = model.predict(x_test_features)
accuracy_on_test_data = accuracy_score(y_test, prediction_on_test_data)

# Confusion Matrix
conf_matrix = confusion_matrix(y_test,prediction_on_test_data)

TP = conf_matrix[0, 0]  # True Positives
FP = conf_matrix[0, 1]  # False Positives
FN = conf_matrix[1, 0]  # False Negatives

# Calculate Precision
precision = (TP / (TP + FP)) * 100

# Calculate Recall
recall = (TP / (TP + FN)) * 100


def checkSpam(email):

    # Transform the input email into features
    input_data_features = feature_extraction.transform([email])

    # Predict whether the email is spam or not
    prediction = model.predict(input_data_features)

    # Interpret the prediction
    if prediction[0] == 0:
        result = 'not spam mail'
    else:
        result = 'spam mail'

    return result



def display():
    result = 'accuracy_on_training_data: ' + str(accuracy_on_training_data * 100) + '\n\n'
    result += 'accuracy_on_test_data: ' + str(accuracy_on_test_data * 100) + '\n\n'
    result += "Confusion Matrix:\n" + str(conf_matrix) + '\n\n'
    result += f"Precision: {precision:.2f}%" + '\n\n'
    result += f"Recall: {recall:.2f}%" + '\n\n'
    return result

""""
def graph():
    plt.scatter(x_train_features, y_train)
    plt.title("training comparison")
    plt.show()

    plt.scatter(x_test_features,y_test)
    plt.title("testing comparison")
    plt.show()

graph()

"""


