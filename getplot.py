import sys
import pandas as pd 
import dataset as ds
import plotly.express as px
import plotly.graph_objects as go
import plotly.offline as pyo
import json



def getnamecateg(df):
    with open('codes/codes.json') as f :
        data = json.loads(f.read())
    l = []
    for i in df.index : 
        x= data['categorie'][i]
        x= x[:40]
        l.append(x)
    df.reset_index()
    df.index = l
    return df

def getnamequali(df):
    with open('codes/codes.json') as f :
        data = json.loads(f.read())
    l = []
    for i in df.index : 
        x= data['qualite'][i]
        x= x[:40]
        l.append(x)
    df.reset_index()
    df.index = l
    return df
    

def getmontantfig(df_remu):
    x= df_remu['remu_montant_ttc'].quantile([.8,.9,.95,.99,.999,1])
    temp = []
    j= []
    l=[]
    s=0
    for axe in x.axes : 
        for i in axe: 
            temp.append(x[i])
            j.append(i)
    for this in temp :
        x= this / temp[-1] * 100
        l.append(x)
    
    fig = go.Figure(data=go.Scatter(x=j, y=l, mode='markers+lines'))
    fig.update_xaxes(type="log")
    fig.update_yaxes(type="log")
    fig.update_layout(title = 'pourcentage des revenues toucher par les entreprises', annotations=[
            dict(
                x=0.5004254919715793,
                y=-0.16191064079952971,
                showarrow=False,
                text='Nombre d"entreprise en pourcentage',
                xref='paper',
                yref='paper'
            ),
            dict(
                x=-0.04944728761514841,
                y=0.4714285714285711,
                showarrow=False,
                text='pourcentage du montant total distribué',
                textangle=-90,
                xref='paper',
                yref='paper'
            )
        ])
    pyo.plot(fig)


def gethistomontant(df_remu):
    histi = df_remu[['benef_categorie_code', 'remu_montant_ttc']].groupby(['benef_categorie_code']).mean().sort_values(by='remu_montant_ttc')
    getnamecateg(histi)
    fig = px.histogram(histi, x=histi.index, y = histi['remu_montant_ttc'], histfunc='max',title='Les catégorie les plus rentables',labels={'remu_montant_ttc':'Montant en €', 'x':'Categorie'}, )
    pyo.plot(fig)