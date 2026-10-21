# python-machine-learning-assignment
## Name. 
Thomas Ochieng Osollo
## Project title. 

  Supervised vs Unsupervised Machine Learning

## Description of the supervised learning project.
   File: supervised_ml.py 

 ## Problem: 
 *** A school wants to predict a student's score in examination score from a number of hours they study.***
 ### Dataset

 | Hours Studied | Exam Score |
|---|---|
| 1 | 30 |
| 2 | 40 |
| 3 | 45 |
| 4 | 55 |
| 5 | 65 |
| 6 | 70 |
| 7 | 80 |
| 8 | 85 |
| 9 | 90 |
| 10 | 95 |
## Approach
 The dataset has 10 students each with hours studied as input and the exam scores as target

 A LinearRegression model from the scikit-learn is trained with fit() to learn the relationship between hours and score.

 The user enters the hours studied and predict() estimates the exam score displayed to 2 decimal places.

  A matplotlib module help with visualization by showing the data points, the fitted regression line and the user prediction.

## Description of the unsupervised learning project.

  File: unsupervised_ml.py
  ## Problem:
   A supermarket wants to understand the customers' shopping behaviour by grouping them automatically using monthly spending(KES) and monthly visits.
   ### Dataset

   | Customer | Monthly Spending (KES) | Monthly Visits |
|---|---:|---:|
| 1 | 1,000 | 2 |
| 2 | 1,500 | 3 |
| 3 | 2,000 | 2 |
| 4 | 5,000 | 6 |
| 5 | 6,000 | 7 |
| 6 | 5,500 | 5 |
| 7 | 12,000 | 12 |
| 8 | 15,000 | 14 |
| 9 | 13,000 | 11 |
| 10 | 3,000 | 4 |

   ## Approach
   The dataset has 10 customers, each with monthly spending and monthly visits(no labels)

   StandardScaler scales both features so that spending, which has much largers numbers does not dominate the clustering

   KMeans model(n_cluster=3), random_state=42 and n_init=10 groups the customers

   The terminal prints the cluster for each customer and the number of customers in the cluster

   Matplotlib scatterplot help show each customer group in different colors.
## Instructions for installing dependencies and running your code.
### 1. Installing dependencies 
   Open the terminal in the code editor. 
   
   Git clone the Github repository URL for the assignment.

   Git code .

   cd repository name/directory

   add files(supervised_ml.py and unsupervised_ml.py)
    
   create and activate a virtual environment

     code

      python3 -m venv venv

      venv/Scripts/Activate

     run code

   **pip install the dependencies (scikit-learn and Matplotlib)**

    pip install scikit-learn

    pip install matplotlib

    pip freeze > requirements.txt 

   *Installed libraries version  displayed requirements.txt file

### 2. Running the code.
   *For supervised machine learning

   run the file(code) in the terminal

       python supervised_ml.py

   Enter the number of hours when prompted. The program prints the predicted score to 2dp, then opens a graph.

   Close the graph window to end the program.

   *For unsupervised machine learning
    Run the file in the terminal or 
    code

         python unsupervised_ml.py
   
   The program prints the cluster assigned to each customer and the number of customers in each cluster, then opens a scatter plot of the groups.

   Close the plot window to end the program.

## PART C - THEORY QUESTIONS

### 1. What is supervised machine learning?

Supervised machine learning is a machine learning approach that uses labeled data sets

### 2. What is unsupervised machine learning?

Unsupervised machine learrning is a machine learning approach that uses unlabeled data sets

### 3. Explain the difference between supervised and unsupervised machine learning?

Supervised machine learning uses labelled data set; predicts an output through regression and classification; labelled data is trained through a model and tested to predict against known outcomes While unsupervised machine learning uses unlabelled data sets for input; from the data it discovers the pattern in the data set through clustering and association without predefined targets; model is trained using the KMeans algorithm

### 4. Why is Linear Regression considered supervised learning?

Linear regression is considered supervised learning because it  requires labeled output values

### 5. Why is K-Means considered unsupervised learning?

K-Means is considered unsupervised learning because the algorithm relies on unlabeled dataset and its prediction of outcomes depends on grouping/clustering of the provided data.

### 6. What is the difference between fit() and predict()?

*fit()* is used for training models while *predict()* is used for predicting the outcomes from a trained model and used to test the effectiveness of a trained model.

### 7. Give two real-world applications of supervised learning and two of unsupervised learning.

*Application of Supervised machine learning* 

Email spam detection

price prediction

*Application of unsupervised machine learning* 

-Customer segmentation; 

-Anormaly detection in network activity/unusual transactions such as fraud.