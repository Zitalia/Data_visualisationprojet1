import sys
import pandas as pd 
import dataset as ds
import plotly.express as px
import plotly.graph_objects as go
import plotly.offline as pyo
import json
from getplot import * 

df_conv = ds.load_conv()
df_benef = ds.load_benef()
df_remu = ds.load_remu()

getmontantfig(df_remu)
gethistomontant(df_remu)


print(df_conv['conv_objet'].value_counts())
x= df_conv['conv_objet'].value_counts()
z=[]
y=[]
for i in x.index :
    z.append(i) 
    print(len(y))
for j in x :
    y.append(j)
d = {'x': y, 'y': z}
df = pd.DataFrame(data=d)
print(df)
fig = px.pie(df, values='x', names='y')
pyo.plot(fig)