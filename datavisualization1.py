import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'D:\CODEXINTERN\Python Internship\Data analysis\Data.csv'
df = pd.read_csv(file_path)

# Display basic information
print("Dataset Overview:\n")
print(df.head())
print("\nSummary Statistics:\n")
print(df.describe())

# Check for missing values
mv = df.isnull().sum()
print("\nMissing values in each column:\n", mv)

# Calculate average age
avg_age = df['Age'].mean()
print("\nAverage age of the people in the dataset is:", avg_age)

# Unique values in the 'Age' column
unique_ages = df['Age'].unique()
print("\nUnique ages in the dataset:", unique_ages)

# Filter employees from the Engineering department
eng_emp = df[df['Department'] == 'Engineering']
print("\nEmployees in the Engineering department:\n", eng_emp)

# Employee with the highest salary
max_salary = df['Salary'].max()
max_salary_emp = df[df['Salary'] == max_salary]
print("\nHighest paid employee:\n", max_salary_emp, "\nWith a salary of:", max_salary)

# Count of employees in each department
dep_count = df['Department'].value_counts()
print("\nDepartment count:\n", dep_count)

# Sort employees by age (senior to junior)
sorted_df = df.sort_values(by="Age", ascending=False)
print("\nEmployees sorted by age (Senior to Junior):\n", sorted_df)

# Add a new column categorizing employees as Senior or Junior based on age
df['Experience'] = df['Age'].apply(lambda x: 'Senior' if x > 30 else 'Junior')
print("\nDataset with Experience column:\n", df)

# Visualizations
plt.figure(figsize=(8, 6))
plt.pie(dep_count, labels=dep_count.index, autopct='%1.1f%%', startangle=140, colors=['skyblue', 'orange', 'lightgreen', 'pink'])
plt.title("Department Distribution", fontsize=16)
plt.show()

# Bar chart: Average salary by department
avg_salary_by_dep = df.groupby('Department')['Salary'].mean()
plt.figure(figsize=(8, 6))
avg_salary_by_dep.plot(kind='bar', color='teal')
plt.title("Average Salary by Department", fontsize=16)
plt.xlabel("Department", fontsize=12)
plt.ylabel("Average Salary", fontsize=12)
plt.xticks(rotation=45)
plt.show()

# Scatter plot: Age vs Salary
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='Age', y='Salary', hue='Department', style='Gender', palette='viridis', s=100)
plt.title("Age vs Salary", fontsize=16)
plt.xlabel("Age", fontsize=12)
plt.ylabel("Salary", fontsize=12)
plt.legend(title="Department & Gender")
plt.show()

# Heatmap: Correlation between numeric columns
plt.figure(figsize=(8, 6))
numeric_df = df.select_dtypes(include=['number'])  # Select only numeric columns
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title("Correlation Heatmap", fontsize=16)
plt.show()

# Insights:
print("\nInsights from the dataset:\n")
print("1. The average age of employees suggests a relatively young workforce.")
print("2. The highest-paid employee is in the Engineering department.")
print("3. Department distribution is evenly spread, with some departments having higher average salaries.")
print("4. Age and salary have a weak correlation based on the heatmap.")
