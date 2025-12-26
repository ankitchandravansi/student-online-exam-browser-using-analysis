

📊 Student Online Exam Browser Usage Analysis

(Exploratory Data Analysis using Python)


---

🔹 Step 1: Project Objective

The objective of this project is to analyze browser usage patterns of students during online examinations using Python. The analysis focuses on:

Identifying the most used browser

Calculating average exam duration per browser

Visualizing browser usage patterns using bar charts



---

🔹 Step 2: Dataset Creation

Since no dataset was provided by the college, a self-generated dataset was created to simulate real-world online exam behavior.

Dataset File: browser_usage.csv

Student_ID,Browser,Exam_Name,Duration_Minutes
1,Chrome,Maths,60
2,Chrome,Physics,70
3,Firefox,Maths,55
4,Edge,Chemistry,50
5,Chrome,Chemistry,65
6,Firefox,Physics,60
7,Edge,Maths,45
8,Chrome,Physics,75
9,Chrome,Maths,80
10,Firefox,Chemistry,55
11,Edge,Physics,50
12,Chrome,Maths,70
13,Firefox,Maths,60
14,Chrome,Chemistry,68
15,Edge,Maths,48


---

🔹 Step 3: Tools & Libraries Used

Python 3.13

Pandas – Data manipulation

Matplotlib – Data visualization

Seaborn – Advanced plotting

VS Code – Code editor



---

🔹 Step 4: Installing Required Libraries

The following command was used to install the required Python libraries:

py -m pip install pandas matplotlib seaborn


---

🔹 Step 5: Python Code for EDA

The main analysis was performed using the following Python script.

File: browser_analysis.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the dataset
df = pd.read_csv("browser_usage.csv")

# Step 2: Display dataset preview
print("Dataset Preview:")
print(df.head())

# Step 3: Dataset information
print("\nDataset Information:")
print(df.info())

# Step 4: Statistical summary
print("\nStatistical Summary:")
print(df.describe())

# Step 5: Browser usage count
browser_count = df['Browser'].value_counts()
print("\nBrowser Usage Count:")
print(browser_count)

# Step 6: Bar chart - Browser usage
plt.figure(figsize=(7,5))
browser_count.plot(kind='bar')
plt.title("Browser Usage in Online Exams")
plt.xlabel("Browser")
plt.ylabel("Number of Students")
plt.xticks(rotation=0)
plt.show()

# Step 7: Average exam duration per browser
avg_time = df.groupby('Browser')['Duration_Minutes'].mean()
print("\nAverage Exam Duration per Browser:")
print(avg_time)

# Step 8: Bar chart - Average exam duration
plt.figure(figsize=(7,5))
avg_time.plot(kind='bar')
plt.title("Average Exam Duration per Browser")
plt.xlabel("Browser")
plt.ylabel("Minutes")
plt.xticks(rotation=0)
plt.show()

# Step 9: Browser usage by exam type
plt.figure(figsize=(8,5))
sns.countplot(data=df, x='Browser', hue='Exam_Name')
plt.title("Browser Usage by Exam Type")
plt.show()

print("\nEDA Project Completed Successfully")


---

🔹 Step 6: Running the Project

The project was executed using the Python launcher:

py browser_analysis.py


---

🔹 Step 7: Results & Observations

Google Chrome is the most commonly used browser during online exams.

Students using Chrome have a higher average exam duration.

Firefox and Edge show comparatively lower usage.

Browser usage varies slightly across different exam subjects.



---

🔹 Step 8: Conclusion

This project demonstrates how Python can be used for Exploratory Data Analysis to extract meaningful insights from data. Using Pandas for data handling and Matplotlib/Seaborn for visualization, browser usage patterns during online exams were successfully analyzed. This type of analysis can help institutions improve the compatibility and performance of online examination systems.

