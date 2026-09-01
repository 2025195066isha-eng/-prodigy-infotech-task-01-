import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Set visual style
sns.set_theme(style="whitegrid")

# Sample continuous data: Age distribution in a population
ages = [18, 19, 21, 22, 23, 24, 25, 25, 26, 28, 29, 30, 31, 33, 35, 37, 40, 42, 45, 48, 52, 55, 60, 65]

# Sample categorical data: Gender distribution
genders = ['Female', 'Male', 'Female', 'Female', 'Male', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male']

# Create subplots
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# 1. Histogram for Continuous Variable (Age)
sns.histplot(ages, bins=8, kde=True, color='skyblue', ax=axes[0])
axes[0].set_title('Age Distribution')
axes[0].set_xlabel('Age')
axes[0].set_ylabel('Count')

# 2. Bar Chart for Categorical Variable (Gender)
sns.countplot(x=genders, palette='pastel', ax=axes[1])
axes[1].set_title('Gender Distribution')
axes[1].set_xlabel('Gender')
axes[1].set_ylabel('Count')

plt.tight_layout()
plt.show()
task1
