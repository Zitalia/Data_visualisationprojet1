import sys
import pandas as pd 
import dataset as ds
import plotly.express as px
import plotly.graph_objects as go
import plotly.offline as pyo
import json
import helpers


def getnamecateg(df):
    with open('codes/codes.json', 'r', encoding='utf-8') as f :
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
    with open('codes/codes.json', 'r', encoding='utf-8') as f :
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
    fig.update_layout(title = 'Pourcentage des revenues toucher par les entreprises', annotations=[
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
    return fig

def gethistomontant(df_remu):
    histi = df_remu[['benef_categorie_code', 'remu_montant_ttc']].groupby(['benef_categorie_code']).mean().sort_values(by='remu_montant_ttc')
    getnamecateg(histi)
    fig = px.histogram(histi, x=histi.index, y = histi['remu_montant_ttc'], histfunc='max',title='Les catégorie les plus rentables',labels={'remu_montant_ttc':'Montant en €', 'x':'Categorie'}, )
    return fig

def get_montant_by_pays(df):
    with open('codes/codes.json', 'r', encoding='utf-8') as f :
        codes = json.loads(f.read())
        
    montant_by_pays = df.groupby(['benef_pays_code']).mean()['remu_montant_ttc'].sort_values()
    to_plot = {'label' : [], 'value' : []}
    for item in montant_by_pays.items():
        to_plot['label'].append(codes['pays'][item[0]])
        to_plot['value'].append(item[1])

    # Scatter
    # fig = go.Figure(data=go.Scatter(x=to_plot['label'], y=to_plot['value'], mode='markers+lines'))

    fig = px.histogram(
            montant_by_pays,
            x=to_plot['label'], y = to_plot['value'], 
            histfunc='max',
            title='Les pays que gagne le plus',
            labels={'y':'Montant en €', 'x':'Pays'}, )

    return fig


def get_fig_for(df, montant, by, translate_key=None):
    montants = helpers.arrange_to_plot(df.groupby(by).mean()[montant].sort_values())

    if translate_key != None:
        montants['labels'] = helpers.translate_list(translate_key, montants['labels'])
    
    return {
        'data': [
            {'x': montants['labels'], 'y': montants['values'], 'type': 'bar', 'name': '.'},
        ],
        'layout': {
            'title': 'Dash Data Visualization'
        }
    }