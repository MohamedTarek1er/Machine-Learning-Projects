from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.naive_bayes import MultinomialNB
from PreProcessing import preprocess
from sklearn.svm import SVC


x_train_features, x_test_features, y_train, y_test, feature_extraction = preprocess('spam_ham_dataset.csv')

#trainning using naive bayes classification
model = SVC()
model.fit(x_train_features,y_train)

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
