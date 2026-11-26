#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

# 1. Load your single-file casualty dataset
file_path = r'C:\Users\claud\Dataset BigData Analytics\dft-road-casualty-statistics-casualty-2024.csv'
print("Loading casualty dataset...")
df_casualty = pd.read_csv(file_path)

# 2. Select demographic characteristics and the 3 distinct additional attributes + target
features_to_use = [
    'age_of_casualty',      # Demographic predictor 1 (Age / biological vulnerability)
    'sex_of_casualty',      # Demographic predictor 2 (Sex / behavioral exposure)
    'casualty_imd_decile',  # Additional Attribute 1: Socioeconomic deprivation decile
    'pedestrian_location',  # Additional Attribute 2: Pedestrian positioning & micro-environment
    'car_passenger',        # Additional Attribute 3: Cabin seating configuration / dynamics
    'casualty_severity'     # Target variable (1: Fatal, 2: Serious, 3: Slight)
]

# Clean sentinel values (-1) across all selected features
for col in features_to_use:
    if col in df_casualty.columns:
        df_casualty[col] = df_casualty[col].replace(-1, np.nan)

# Drop missing rows for clean machine learning training (Complete-case analysis)
df_ml = df_casualty.dropna(subset=features_to_use).copy()

# Ensure integer types where appropriate
for col in features_to_use:
    df_ml[col] = df_ml[col].astype(int)

print(f"Rows used for Decision Tree model: {len(df_ml)}")

# 3. Define Features (X) and Target (y)
X = df_ml[[
    'age_of_casualty', 
    'sex_of_casualty', 
    'casualty_imd_decile', 
    'pedestrian_location', 
    'car_passenger'
]]
y = df_ml['casualty_severity'] # 1: Fatal, 2: Serious, 3: Slight

# 4. Train/Test Split (Stratified to maintain class balance for rare fatal accidents)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 5. Train Decision Tree Classifier
# max_depth=6 keeps the tree interpretable and avoids overfitting
dt_model = DecisionTreeClassifier(max_depth=6, random_state=42)
dt_model.fit(X_train, y_train)

# 6. Evaluate Model Accuracy, Performance, and Confusion Matrix
y_pred = dt_model.predict(X_test)
print(f"\nModel Accuracy: {accuracy_score(y_test, y_pred):.4f}\n")
print("Classification Report:")
# zero_division=0 prevents warnings when minority classes have zero predicted samples
print(classification_report(y_test, y_pred, zero_division=0))

# Confusion Matrix Generation and Display 
print("Confusion Matrix:")
cm = confusion_matrix(y_test, y_pred)
print(cm)

# Plot Confusion Matrix
fig, ax = plt.subplots(figsize=(8, 6))
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['Fatal (1)', 'Serious (2)', 'Slight (3)'])
disp.plot(cmap=plt.cm.Blues, ax=ax, values_format='d')
plt.title('Confusion Matrix for Casualty Severity Classification')
plt.tight_layout()
plt.show()

# 7. Extract Feature Importances (Quantitative Evidence for your report)
feature_importances = pd.DataFrame({
    'Feature': X.columns,
    'Importance Score': dt_model.feature_importances_
}).sort_values(by='Importance Score', ascending=False)

print("\n--- DECISION TREE FEATURE IMPORTANCE RANKING ---")
print(feature_importances)

# 8. Plot Feature Importance Bar Chart
plt.figure(figsize=(9, 5))
plt.barh(feature_importances['Feature'], feature_importances['Importance Score'], color='steelblue')
plt.xlabel('Importance Score')
plt.ylabel('Predictive Attributes')
plt.title('Decision Tree Feature Importance for Predicting Casualty Severity')
plt.gca().invert_yaxis() # Puts highest importance at the top
plt.tight_layout()
plt.show()

