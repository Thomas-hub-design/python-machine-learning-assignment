# Importing necessary libraries
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Preparing the dataset (Monthly spending (KES), Monthly visits)
customers = [
    [1000, 2],
    [1500, 3],
    [2000, 2],
    [5000, 6],
    [6000, 7],
    [5500, 5],
    [12000, 12],
    [15000, 14],
    [13000, 11],
    [3000, 4],
]

# Scaling the spending and visiting features
scaler = StandardScaler()
customers_scaled = scaler.fit_transform(customers)

# Creating a KMeans clustering model
model = KMeans(n_clusters=3, random_state=42, n_init=10)

# Training the model
model.fit(customers_scaled)

# Labeling the clusters
labels = model.labels_

# Displaying the clusters assigned to each customer
for i, (customer, label) in enumerate(zip(customers, labels), start=1):
    print(f"Customer {i}:belongs to cluster {label}")

# Displaying the number of customers in each cluster
for cluster in range(3):
    count = sum(1 for label in labels if label == cluster)
    print(f"Cluster {cluster + 1}: {count} customers")

# Visualizing the clusters
spending = [customer[0] for customer in customers]
visits = [customer[1] for customer in customers]
plt.scatter(spending, visits, c=labels, cmap='viridis', s=100)
plt.xlabel('Monthly Spending (KES)')
plt.ylabel('Monthly Visits')
plt.title('Customer Segmentation using KMeans Clustering')
plt.show()