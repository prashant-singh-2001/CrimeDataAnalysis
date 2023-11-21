 import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data=pd.read_csv('Cleaned_Data.csv',index_col='ID')
# print(data.groupby('Status').size())
for name,group in data.groupby('Status'):
    group=group.groupby('Crm Cd').size().sort_values(ascending=False)
    print(name,'\n',group.head()