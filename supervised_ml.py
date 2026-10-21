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
# Making predictions
predicted_scores = model.predict(X)
# Displaying the predicted scores
for i, (hours, score) in enumerate(zip(Hours_studied, predicted_scores), start=1):
    print(f"Student {i}: Hours Studied = {hours[0]}, Predicted Exam Score = {score[0]:.2f}")
# Visualizing the results
plt.scatter(Hours_studied, Exam_scores, color='blue', label='Actual Scores')
plt.plot(Hours_studied, predicted_scores, color='red', label='Regression line')
plt.xlabel('Hours Studied')
plt.ylabel('Exam Scores')
plt.title('Hours Studied vs Exam Scores')
plt.legend()
plt.show()
