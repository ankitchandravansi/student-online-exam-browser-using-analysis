import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# CSV load
df = pd.read_csv("browser_usage.csv")

print("Dataset Preview:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

# Browser usage count
browser_count = df['Browser'].value_counts()
print("\nBrowser Usage Count:")
print(browser_count)

plt.figure(figsize=(7,5))
browser_count.plot(kind='bar')
plt.title("Browser Usage in Online Exams")
plt.xlabel("Browser")
plt.ylabel("Number of Students")
plt.xticks(rotation=0)
plt.show()

# Average exam duration
avg_time = df.groupby('Browser')['Duration_Minutes'].mean()
print("\nAverage Exam Duration per Browser:")
print(avg_time)

plt.figure(figsize=(7,5))
avg_time.plot(kind='bar')
plt.title("Average Exam Duration per Browser")
plt.xlabel("Browser")
plt.ylabel("Minutes")
plt.xticks(rotation=0)
plt.show()

# Exam-wise usage
plt.figure(figsize=(8,5))
sns.countplot(data=df, x='Browser', hue='Exam_Name')
plt.title("Browser Usage by Exam Type")
plt.show()

print("EDA Project Completed Successfully")
print("\nExam-wise Browser Usage Table:")
print(pd.crosstab(df['Browser'], df['Exam_Name']))
