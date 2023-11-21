import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data=pd.read_csv("Crime_Data_from_2020_to_Present.csv")
print(data.shape)

data=data.drop(['DR_NO','Crm Cd Desc','AREA NAME','Premis Desc','Weapon Desc','Status Desc','Mocodes','LAT','LON','LOCATION','Cross Street','Vict Descent','Crm Cd 1','Crm Cd 2','Crm Cd 3','Crm Cd 4'],axis=1)

crime_counts = data['Crm Cd'].value_counts()

# Define a threshold for the minimum number of occurrences
threshold = 1000

# Create a list of crime codes to remove
negligible_crime_codes = crime_counts[crime_counts <= threshold].index.tolist()

# Remove the rows where the crime code is in the negligible list
data = data[~data['Crm Cd'].isin(negligible_crime_codes)]

print(data.shape)

data.to_csv('Cleaned_Data.csv')