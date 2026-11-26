import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("--- 1. NUMPY ---")
marks = np.array([[80, 75, 90],
                  [60, 70, 65],
                  [90, 85, 95],
                  [70, 60, 75]])
print("Shape:", marks.shape)
print("Student averages:", marks.mean(axis=1))
print("Subject averages:", marks.mean(axis=0))

grace = marks + 5
print("After Grace Marks:\n", grace)

weights = np.array([0.3, 0.3, 0.4])
weighted = np.dot(marks, weights)
print("Weighted Scores:", weighted)

print("\n--- 2. PANDAS LOAD ---")
df = pd.read_csv("employees.csv")
print(df.info())
print(df.describe())
print("loc:\n", df.loc[0:2])
print("iloc:\n", df.iloc[0:2])
print("Filtering >60000:\n", df[df['salary'] > 60000])

print("\n--- 3. CLEANING ---")
print("Before:", df.shape)
df['salary'] = pd.to_numeric(df['salary'], errors='coerce')
median_sal = df['salary'].median()
df['salary'] = df['salary'].fillna(median_sal)
df = df.drop_duplicates()
print("After Cleaning:", df.shape)
print(df)

print("\n--- 4. GROUPBY & MERGE ---")
dept = pd.read_csv("departments.csv")
summary = df.groupby('department').agg(headcount=('id','count'), avg_salary=('salary','mean'), max_salary=('salary','max'))
print(summary)

print("Inner:\n", pd.merge(df, dept, on='department', how='inner').head())
print("Left:\n", pd.merge(df, dept, on='department', how='left').head())
outer = pd.merge(df, dept, on='department', how='outer')
print("Outer:\n", outer)
no_emp = outer[outer['id'].isna()]['department'].tolist()
print("Department with no employees:", no_emp)

print("\n--- 5. CHARTS ---")
# Bar
plt.figure()
plt.bar(summary.index, summary['headcount'], label='Headcount')
plt.title("Headcount per Department"); plt.xlabel("Department"); plt.ylabel("Count"); plt.legend(); plt.savefig("bar.png"); plt.close()
print("Insight Bar: IT has highest headcount.")

# Histogram
plt.figure()
plt.hist(df['salary'], bins=4, label='Salary')
plt.title("Salary Distribution"); plt.xlabel("Salary"); plt.ylabel("Frequency"); plt.legend(); plt.savefig("hist.png"); plt.close()
print("Insight Histogram: Most salaries are around 60000-75000.")

# Scatter
plt.figure()
plt.scatter(df['id'], df['salary'], label='Salary vs ID')
plt.title("Salary vs ID"); plt.xlabel("ID"); plt.ylabel("Salary"); plt.legend(); plt.savefig("scatter.png"); plt.close()
print("Insight Scatter: Salary increases for IT employees.")

# Line
plt.figure()
plt.plot(summary.index, summary['avg_salary'], marker='o', label='Avg Salary')
plt.title("Avg Salary per Department"); plt.xlabel("Department"); plt.ylabel("Avg Salary"); plt.legend(); plt.savefig("line.png"); plt.close()
print("Insight Line: IT has highest average salary.")

print("\nTask 3 Done!")