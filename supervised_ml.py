from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
#Creating a dataset
Hours_studied = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
Exam_scores = [[35], [40], [45], [55], [65], [70], [80], [85], [90], [95]]
# Separating the input features (X) and the target values (Y)
X = Hours_studied
Y = Exam_scores
#Creating a Linear Regression model
model = LinearRegression()
#Training the model
model.fit(X, Y)
# User input for prediction
user_hours = float(input("Enter the number of hours studied: "))
# Making predictions
predicted_score= model.predict([[user_hours]])
# Displaying the predicted scores
print(f"Predicted Exam Score: {predicted_score[0][0]:.2f}")
print(f"Predicted Score Shape: {predicted_score.shape}")
# Visualizing the results
plt.scatter(X, Y, color='blue', label='Actual Scores')
plt.plot(X, model.predict(X), color='red', label='Regression Line')
plt.xlabel('Hours Studied')
plt.ylabel('Exam Scores')
plt.title('Linear Regression: Hours Studied vs Exam Scores')
plt.legend()
plt.show()