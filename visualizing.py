# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import datetime as dt
# data=pd.read_csv('Cleaned_Data.csv',index_col='ID')
# # plt.figure(figsize=(10,4))
# # Group the data with respect to Crm Cd and Vict Sex and plot the bar graph
# # import matplotlib.pyplot as plt
# # gencrm=data.groupby(['Crm Cd','Vict Sex']).size().unstack()
# # gencrm['H']=gencrm['H'].fillna(gencrm['H'].mean)
# # gencrm['X']=gencrm['H'].fillna(gencrm['X'].mean)
# # gencrm['H']=gencrm['F'].fillna(gencrm['F'].mean)
# # gencrm['X']=gencrm['M'].fillna(gencrm['M'].mean)
# # percent_data=gencrm.copy()
# # percent_data['percent_m'] = (gencrm['M'] / (gencrm['F'] + gencrm['M']+gencrm['H']+gencrm['X'])) * 100
# # percent_data['percent_f'] = (gencrm['F'] / (gencrm['F'] + gencrm['M']+gencrm['H']+gencrm['X'])) * 100
# # percent_data['percent_x'] = (gencrm['X'] / (gencrm['F'] + gencrm['M']+gencrm['H']+gencrm['X'])) * 100
# # percent_data['percent_h'] = (gencrm['H'] / (gencrm['F'] + gencrm['M']+gencrm['H']+gencrm['X'])) * 100
# # percent_data = percent_data.drop(['F', 'M','H','X'], axis=1)
# # percent_data_sorted = percent_data.assign(diff=(percent_data['percent_f'] - percent_data['percent_m'])).sort_values(by='diff', ascending=False)
# # percent_data_sorted = percent_data_sorted.drop(['percent_x','percent_h'],axis=1)
# # percent_data_sorted.plot(kind='bar',stacked=False,xlabel="Crime Code Description",ylabel="Count",title="Crimes by Gender",figsize=(20,10))
# # plt.show()
# crm=data.groupby('Crm Cd')
# for name,group in crm:
#     if group.size>300000:
#         group['DATE OCC']=pd.to_datetime(group['DATE OCC'])
#         group['DATE OCC']=group['DATE OCC'].dt.month
#         group=group.groupby('DATE OCC').count()
#         group.plot(y='AREA',ylabel='Count',figsize=(20,8))
#         group.index=pd.Categorical(group.index)
#         group['ID']=group.index.codes
#         sns.regplot(x='ID',y='AREA',data=group)
#         plt.show()

import plotly.express as px

# load the gapminder dataset
df = px.data.gapminder()

# filter the data to keep only 2007 year data
df = df[df['year']==2007]

# create a choropleth map
fig = px.choropleth(df, locations='iso_alpha',
                    color='lifeExp', 
                    hover_name='country',
                    color_continuous_scale=px.colors.sequential.Plasma,
                    title='World Life Expectancy in 2007'
                   )

# display the map
fig.show()
