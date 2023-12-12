import pandas as pd

# Load data from Excel files into dataframes
workshop1_df = pd.read_excel('workshop1.xlsx')
workshop2_df = pd.read_excel('workshop2.xlsx')

# a. Find names of students who attended both workshops
both_attendance = pd.merge(workshop1_df, workshop2_df, on=['Name', 'Date', 'duration'], how='inner')['Name'].unique()
print("Names of students who attended both workshops:", both_attendance)

# b. Find names of students who attended a single workshop only
single_attendance = pd.merge(workshop1_df, workshop2_df, on=['Name', 'Date', 'duration'], how='outer', indicator=True)
single_attendance = single_attendance[single_attendance['_merge'] != 'both']['Name'].unique()
print("Names of students who attended a single workshop only:", single_attendance)

# c. Merge two dataframes row-wise and find the total number of records
merged_df = pd.concat([workshop1_df, workshop2_df], ignore_index=True)
total_records = len(merged_df)
print("Total number of records after merging row-wise:", total_records)

# d. Merge two dataframes row-wise and create a hierarchical dataframe using names and dates as multi-row indexes
hierarchical_df = pd.concat([workshop1_df.set_index(['Name', 'Date']), workshop2_df.set_index(['Name', 'Date'])])
descriptive_stats = hierarchical_df.groupby(level=[0, 1]).describe()
print("Descriptive statistics for hierarchical dataframe:\n", descriptive_stats)
