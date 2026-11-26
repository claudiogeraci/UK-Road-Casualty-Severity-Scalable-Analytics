#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set style for professional charts
sns.set_theme(style="whitegrid")

# 1. Load data
file_path = r'C:\Users\claud\Dataset BigData Analytics\dft-road-casualty-statistics-casualty-2024.csv'
df = pd.read_csv(file_path)

print(f"Total rows in raw dataset: {len(df)}")

# 2. Convert -1 sentinel values to true NaN in target columns
columns_to_clean = ['age_of_casualty', 'casualty_type', 'casualty_severity']
for col in columns_to_clean:
    df[col] = df[col].replace(-1, np.nan)

# 3. Drop NaN rows ONLY for our analytical subset so missing data doesn't skew relationships
df_analysis = df.dropna(subset=columns_to_clean).copy()

# Ensure correct data types for valid records
df_analysis['casualty_severity'] = df_analysis['casualty_severity'].astype(int)
df_analysis['casualty_type'] = df_analysis['casualty_type'].astype(int)
df_analysis['age_of_casualty'] = df_analysis['age_of_casualty'].astype(int)

# 4. Map numerical casualty types to descriptive labels
casualty_type_mapping = {
    0: 'Pedestrian',
    1: 'Pedal cyclist',
    2: 'Motorcycle (<=50cc)',
    3: 'Motorcycle (50-125cc)',
    4: 'Motorcycle (125-500cc)',
    5: 'Motorcycle (>500cc)',
    8: 'Taxi/Private hire',
    9: 'Car occupant',
    10: 'Bus/Coach occupant',
    11: 'Other vehicle',
    16: 'Horse rider',
    17: 'Agricultural vehicle',
    18: 'Tram occupant',
    19: 'Van / Light goods',
    20: 'Goods vehicle',
    21: 'HGV (>7.35t)',
    22: 'Mobility scooter',
    23: 'E-scooter rider',
    90: 'Other vehicle',
    97: 'Unknown'
}

df_analysis['casualty_type_label'] = df_analysis['casualty_type'].map(casualty_type_mapping)

# ==========================================
# 5. CONTINGENCY TABLE WITH SEVERITY ON TOP
# ==========================================
print("\n--- CONTINGENCY TABLE: Casualty Severity by Transport Type (%) ---")
type_severity_ct = pd.crosstab(
    df_analysis['casualty_type_label'], 
    df_analysis['casualty_severity'], 
    normalize='index'
) * 100

# Rename columns so headers clearly show severity levels
type_severity_ct = type_severity_ct.rename(columns={1: 'Fatal (1)', 2: 'Serious (2)', 3: 'Slight (3)'})
print(type_severity_ct.round(2))

# ==========================================
# 6. VISUALIZATIONS (Box Plot, Stacked Bar, & Frequency Histogram)
# ==========================================
fig, axes = plt.subplots(1, 3, figsize=(20, 6))

# Plot A: Box plot of Age across Severities
sns.boxplot(
    data=df_analysis, 
    x='casualty_severity', 
    y='age_of_casualty', 
    ax=axes[0], 
    palette='Set2'
)
axes[0].set_title('Age Distribution Across Injury Severities')
axes[0].set_xlabel('Casualty Severity (1=Fatal, 2=Serious, 3=Slight)')
axes[0].set_ylabel('Age of Casualty')

# Plot B: Proportional Bar Chart using descriptive category labels
type_severity_ct.plot(
    kind='bar', 
    stacked=True, 
    ax=axes[1], 
    colormap='viridis'
)
axes[1].set_title('Proportion of Injury Severity by Transport Type')
axes[1].set_xlabel('Casualty Type')
axes[1].set_ylabel('Percentage (%)')
axes[1].legend(title='Severity')
axes[1].tick_params(axis='x', rotation=45)
plt.setp(axes[1].get_xticklabels(), ha='right')

# Plot C: Frequency Histogram / Count Plot for Each Casualty Category
sns.countplot(
    data=df_analysis, 
    y='casualty_type_label', 
    ax=axes[2], 
    order=df_analysis['casualty_type_label'].value_counts().index,
    palette='crest'
)
axes[2].set_title('Total Casualty Count by Category')
axes[2].set_xlabel('Number of Casualties')
axes[2].set_ylabel('Casualty Type')

plt.tight_layout()
plt.show()


# In[2]:


print(df_analysis['casualty_type_label'].value_counts())


# In[ ]:




