"""
A small demonstration Machine Learning model.

The model is trained on generated example marks. It learns to classify
a student's average marks into a performance category. For a real
academic project, replace this sample training data with an approved,
real student dataset.
"""

from sklearn.tree import DecisionTreeClassifier
import numpy as np

# Create example training data: five subject marks for each student.
# The labels are based on the average mark.
X = []
y = []

for english in range(0, 101, 10):
    for maths in range(0, 101, 20):
        for computer in range(0, 101, 20):
            for science in range(0, 101, 20):
                for hindi in range(0, 101, 20):
                    marks = [english, maths, computer, science, hindi]
                    average = sum(marks) / len(marks)

                    if average >= 80:
                        label = "Excellent"
                    elif average >= 60:
                        label = "Good"
                    elif average >= 40:
                        label = "Average"
                    else:
                        label = "Needs Improvement"

                    X.append(marks)
                    y.append(label)

model = DecisionTreeClassifier(max_depth=4, random_state=42)
model.fit(np.array(X), np.array(y))


def predict_performance(marks):
    """Return the performance category predicted by the trained model."""
    prediction = model.predict([marks])
    return prediction[0]
