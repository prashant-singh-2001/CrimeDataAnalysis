from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd
 
# Reads 'Youtube04-Eminem.csv' file
df = pd.read_csv('Crm-Desc.csv')
df2=pd.read_csv('Cleaned_Data.csv')
df.merge(df2,how='inner',on='Crm Cd')
comment_words = ''
stopwords = set(STOPWORDS)
for val in df.Desc:
    val = str(val)
    tokens = val.split()
    for i in range(len(tokens)):
        tokens[i] = tokens[i].lower()
     
    comment_words += " ".join(tokens)+" "
 
wordcloud = WordCloud(width = 800, height = 800,
                background_color ='white',
                stopwords = stopwords,
                min_font_size = 10).generate(comment_words)                    
plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wordcloud,interpolation='bilinear')
plt.axis("off")
plt.tight_layout(pad = 0)
plt.show()

'''
This following code creates a relation between status of accused in Crime specifics
'''
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# data=pd.read_csv('Cleaned_Data.csv',index_col='ID')
# # print(data.groupby('Status').size())
# for name,group in data.groupby('Status'):
#     group=group.groupby('Crm Cd').size().sort_values(ascending=False)
#     print(name,'\n',group.head())
'''
This following code creates a relation between guns/weapons used in Crimes specifics
'''
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# data=pd.read_csv('Cleaned_Data.csv',index_col='ID')
# for name,group in data.groupby('Weapon Used Cd'):
#     if group.size>20000:
#         group=group.groupby('Crm Cd').size().sort_values(ascending=False)
#         print(name,'\n',group.head())

# import folium as fl
# import matplotlib.pyplot as plt
# import pandas as pd
# from io import StringIO
# df=pd.read_csv('Crime_Data_from_2020_to_Present.csv')
# map_LA = fl.Map(location=[34.0522, -118.2437], zoom_start=10)
# for name,group in df.groupby('Crm Cd'):
#     if group.size<=1:
#       for index,data in group.iterrows():
#         fl.Marker(location=[data.LAT,data.LON], tooltip="").add_to(map_LA) 
# map_LA