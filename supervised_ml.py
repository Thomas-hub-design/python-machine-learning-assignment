from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
#Creating a dataset
Hours_studied = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
Exam_scores = [[35], [40], [45], [55], [65], [70], [80], [85], [90], [95]]
#Creating a Linear Regression model
model = LinearRegression()
#Training the model
model.fit(Hours_studied, Exam_scores)
#Making predictions
predicted_scores = model.predict([[11]])
print("Predicted Exam Scores for hour of study:", predicted_scores,)

#Visualizing the results
plt.scatter(Hours_studied, Exam_scores, color='blue')
plt.plot(Hours_studied, model.predict(Hours_studied), color='red')
plt.xlabel('Hours Studied')
plt.ylabel('Exam Scores')
plt.title('Linear Regression')
plt.show()