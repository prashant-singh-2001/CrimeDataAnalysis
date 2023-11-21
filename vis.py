import pandas as pd
df=pd.read_csv('Cleaned_Data.csv')
df=df.drop(df.columns[0],axis=1)
AreaWise=df.groupby(['AREA','Crm Cd']).size().unstack()
import networkx as nx
import matplotlib.pyplot as plt

# create a network graph
G = nx.Graph()

# add nodes
for area in AreaWise.index:
    G.add_node(area)

# add edges
for col in AreaWise.columns:
    for i in range(len(AreaWise)):
        if AreaWise.iloc[i][col] > 0:
            G.add_edge(AreaWise.index[i], col)

# draw the graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='grey', font_size=8, node_size=500)
plt.show()

