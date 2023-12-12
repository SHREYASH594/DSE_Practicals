import pandas as pd

# Creating the DataFrame
data = {
    'FamilyName': ['Shah', 'Vats', 'Vats', 'Kumar', 'Vats', 'Kumar', 'Shah', 'Shah', 'Kumar', 'Vats'],
    'Gender': ['Male', 'Male', 'Female', 'Female', 'Female', 'Male', 'Male', 'Female', 'Female', 'Male'],
    'MonthlyIncome': [44000.00, 65000.00, 43150.00, 66500.00, 255000.00, 103000.00, 55000.00, 112400.00, 81030.00, 71900.00]
}

df = pd.DataFrame(data)

# a. Calculate and display family-wise gross monthly income
familywise_income = df.groupby('FamilyName')['MonthlyIncome'].sum()
print("Family-wise gross monthly income:")
print(familywise_income)

# b. Display the highest and lowest monthly income for each family name
highest_income = df.groupby('FamilyName')['MonthlyIncome'].max()
lowest_income = df.groupby('FamilyName')['MonthlyIncome'].min()
print("\nHighest monthly income for each family name:")
print(highest_income)
print("\nLowest monthly income for each family name:")
print(lowest_income)

# c. Monthly income of all members earning less than Rs. 80000.00
income_less_than_80k = df[df['MonthlyIncome'] < 80000.00]['MonthlyIncome']
print("\nMonthly income of members earning less than Rs. 80000.00:")
print(income_less_than_80k)

# d. Total number of females along with their average monthly income
female_data = df[df['Gender'] == 'Female']
total_females = female_data.shape[0]
average_income_female = female_data['MonthlyIncome'].mean()
print("\nTotal number of females:", total_females)
print("Average monthly income of females:", average_income_female)

# e. Delete rows with monthly income less than the average income of all members
average_income_all = df['MonthlyIncome'].mean()
print("\nAverage monthly income of all members:", average_income_all)
df = df[df['MonthlyIncome'] >= average_income_all]
print("DataFrame after deleting rows with income less than average income of all members:")
print(df)
