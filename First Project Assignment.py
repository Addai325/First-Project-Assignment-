#Name: Ransford Addai
#Training ID: 32524
#Week One(1) Python Programming Project

# Import necessary libraries
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt

# Question 1: Create a Python dictionary with student data and generate random data if needed.

# Define student data in a dictionary
data = {
    "Student ID": list(range(1, 9)),
    "Student Name": ["Student" + str(i) for i in range(1, 9)],
    "Sex": [random.choice(["Male", "Female"]) for _ in range(8)],
    "Math Score": [random.randint(0, 100) for _ in range(8)],
    "Science Score": [random.randint(0, 100) for _ in range(8)],
    "English Score": [random.randint(0, 100) for _ in range(8)],
    "History Score": [random.randint(0, 100) for _ in range(8)],
    "Geography Score": [random.randint(0, 100) for _ in range(8)]
}

# Question 2: Data checks

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)

# Print the shape of the DataFrame (number of rows and columns)
print("Shape of DataFrame:", df.shape)

# Check for missing values in each column and report the count of missing values
missing_values = df.isnull().sum()
print("Missing values per column:\n", missing_values)

# Check for duplicates in the dataset and report the count of duplicates
duplicates = df.duplicated().sum()
print("Duplicate rows:", duplicates)

# Question 3: Data calculations and statistics

# Calculate and add a new column for the "Average Score"
df["Average Score"] = df[["Math Score", "Science Score", "English Score", "History Score", "Geography Score"]].mean(axis=1)

# Calculate and print statistics for each subject
subject_stats = df[["Math Score", "Science Score", "English Score", "History Score", "Geography Score"]].agg(["mean", "max", "min"])
print("Subject statistics:\n", subject_stats)

# Calculate and print the overall mean score for all subjects for each gender category (Male and Female)
gender_mean = df.groupby("Sex")["Average Score"].mean()
print("Gender-wise overall mean score:\n", gender_mean)

# Question 4: Data Visualization

# Define subject columns for visualization
subject_columns = ["Math Score", "Science Score", "English Score", "History Score", "Geography Score"]

# Calculate the mean scores by subject and gender
gender_subject_mean = df.groupby("Sex")[subject_columns].mean()

# Create a bar chart to visualize average scores of students for each subject, grouped by gender
gender_subject_mean.plot(kind="bar")
plt.title("Average Scores by Subject and Gender")
plt.ylabel("Average Score")
plt.xlabel("Gender")
plt.xticks(rotation=0)
plt.legend(title="Subject", loc="upper right")
plt.show()
