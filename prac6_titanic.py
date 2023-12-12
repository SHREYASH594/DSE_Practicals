import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Titanic dataset
titanic_df = pd.read_csv('titanic.csv')

# a. Clean the data by dropping the column with the largest number of missing values
column_with_most_missing = titanic_df.isnull().sum().idxmax()
titanic_df.drop(column_with_most_missing, axis=1, inplace=True)
print("Column dropped:", column_with_most_missing)

# b. Total number of passengers with age more than 30
passengers_age_more_than_30 = titanic_df[titanic_df['Age'] > 30]['PassengerId'].count()
print("Total passengers with age more than 30:", passengers_age_more_than_30)

# c. Total fare paid by passengers of second class
total_fare_second_class = titanic_df[titanic_df['Pclass'] == 2]['Fare'].sum()
print("Total fare paid by second class passengers:", total_fare_second_class)

# d. Comparison of survivors in each passenger class
survivors_by_class = titanic_df.groupby('Pclass')['Survived'].sum()
print("Number of survivors by passenger class:\n", survivors_by_class)

# e. Descriptive statistics for age attribute gender-wise
descriptive_stats_age_gender = titanic_df.groupby('Sex')['Age'].describe()
print("Descriptive statistics for age attribute gender-wise:\n", descriptive_stats_age_gender)

# f. Scatter plot for passenger fare paid by Female and Male passengers separately
plt.figure(figsize=(6, 4))
sns.scatterplot(x='Fare', y='Sex', data=titanic_df)
plt.title('Passenger Fare by Gender')
plt.xlabel('Fare')
plt.ylabel('Gender')
plt.show()

# g. Density distribution comparison for features age and passenger fare
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
sns.kdeplot(titanic_df['Age'], shade=True)
plt.title('Density Distribution of Age')
plt.xlabel('Age')
plt.ylabel('Density')

plt.subplot(1, 2, 2)
sns.kdeplot(titanic_df['Fare'], shade=True)
plt.title('Density Distribution of Fare')
plt.xlabel('Fare')
plt.ylabel('Density')

plt.tight_layout()
plt.show()

# h. Pie chart for passenger class distribution
class_counts = titanic_df['Pclass'].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(class_counts, labels=['Class 3', 'Class 1', 'Class 2'], autopct='%1.1f%%', startangle=90, colors=['gold', 'lightblue', 'lightgreen'])
plt.title('Passenger Class Distribution')
plt.show()

# i. Percentage of survived passengers for each class
survival_percentage_by_class = titanic_df.groupby('Pclass')['Survived'].mean() * 100
print("Percentage of survived passengers for each class:\n", survival_percentage_by_class)
