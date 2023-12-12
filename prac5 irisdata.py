import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Load Iris dataset from sklearn
iris_sklearn = load_iris()

# a. Load data into pandas data frame
iris_df = pd.DataFrame(data=iris_sklearn.data, columns=iris_sklearn.feature_names)
iris_df['target'] = iris_sklearn.target  # Adding target column
iris_df['species'] = iris_df['target'].map({i: species for i, species in enumerate(iris_sklearn.target_names)})
print("Info on data types:")
print(iris_df.info())

# b. Find the number of missing values in each column
missing_values = iris_df.isnull().sum()
print("\nNumber of missing values in each column:")
print(missing_values)

# c. Plot bar chart to show frequency of each class label
plt.figure(figsize=(6, 4))
sns.countplot(x='species', data=iris_df)
plt.xlabel('Species')
plt.ylabel('Frequency')
plt.title('Frequency of Each Class Label')
plt.show()

# d. Scatter plot for Petal Length vs Sepal Length with regression line
plt.figure(figsize=(6, 4))
sns.regplot(x='sepal length (cm)', y='petal length (cm)', data=iris_df)
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.title('Scatter Plot: Petal Length vs Sepal Length')
plt.show()

# e. Density distribution plot for feature Petal width
plt.figure(figsize=(6, 4))
sns.kdeplot(iris_df['petal width (cm)'], shade=True)
plt.xlabel('Petal Width (cm)')
plt.ylabel('Density')
plt.title('Density Distribution of Petal Width')
plt.show()

# f. Pair plot for pairwise bivariate distribution
sns.pairplot(iris_df, hue='species')
plt.suptitle('Pairwise Bivariate Distribution in Iris Dataset', y=1.02)
plt.show()

# g. Heatmap for any two numeric attributes
plt.figure(figsize=(6, 4))
sns.heatmap(iris_df[['sepal length (cm)', 'petal length (cm)']].corr(), annot=True, cmap='coolwarm')
plt.title('Heatmap for Sepal Length vs Petal Length')
plt.show()

# h. Compute descriptive statistics for each numeric feature
numeric_features = iris_df.drop(['target', 'species'], axis=1)
statistics = numeric_features.describe()
print("\nDescriptive statistics for each numeric feature:")
print(statistics)

# i. Compute correlation coefficients between each pair of features and plot heatmap
correlation_matrix = iris_df.corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Coefficients Between Features')
plt.show()
