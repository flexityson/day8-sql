import pandas as pd
from sklearn.model_selection import train_test_split

data= {
    'study_hours': [2, 5, 1, 8, 3, 7, 4, 6, 2, 9],
    'attendance': [60, 80, 50, 95, 65, 90, 70, 85, 55, 98],
    'previous_grade': [50, 70, 40, 90, 55, 85, 65, 80, 45, 95],
    'passed_exam': [0, 1, 0, 1, 0, 1, 1, 1, 0, 1]
}

df=pd.DataFrame(data)

X=df[['study_hours', 'attendance', 'previous_grade']]
Y=df['passed_exam']

print(X.shape)
print(Y.shape)

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

print("Training size:", X_train.shape)
print("Testing size:", X_test.shape)

from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(X_train, y_train)

print("Model trained!")

predictions = model.predict(X_test)

print("Predictions:", predictions)
print("Actual:     ", y_test.values)

from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, predictions)
print("Accuracy:", accuracy)