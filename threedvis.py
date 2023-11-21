import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv('Cleaned_Data.csv',index_col='ID')
AreaWise=df.groupby(['AREA','Crm Cd']).size().unstack()
plt.figure(figsize=(24,16))
sns.heatmap(AreaWise, cmap="coolwarm")
plt.title('Crime Count by Area and Type')
plt.show()

