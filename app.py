# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

import pandas as pd

import dataset as ds
import helpers
import getplot

# ['benef_categorie_code', 'benef_pays_code', 'benef_identifiant_type_code', 'benef_titre_code', 'benef_specialite_code']

WHO_MSG = ['Bénéficiaire', 'Entreprise']

CURRENT_WHO_0 = 0
CURRENT_WHO_1 = 0
CURRENT_WHO_2 = 0
CURRENT_CAT_2 = 'benef_categorie_code'

REMU_COL = 'remu_montant_ttc'
DATE_COL = 'remu_date'

CAT_OPTIONS = [
    [
        { 'label' : 'Catégorie', 'value' : 'benef_categorie_code' },
        { 'label' : 'Pays', 'value' : 'benef_pays_code' },
        { 'label' : 'Identifiant', 'value' : 'benef_identifiant_type_code' },
        { 'label' : 'Titre', 'value' : 'benef_titre_code' },
        { 'label' : 'Spécialité', 'value' : 'benef_specialite_code' }
    ],
    [
        { 'label' : 'Pays', 'value' : 'pays_code' },
        { 'label' : 'Secteur', 'value' : 'secteur_activite_code' },
    ]]
WHO_OPTIONS = [
    { 'label' : 'Bénéficiaire', 'value': 0 },
    { 'label' : 'Entreprise', 'value': 1 }]


df_remu = ds.load_short_remu()
df_entr = ds.load_short_entr()
dfs = [
    df_remu,
    df_entr
]

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div([
    html.Br(),
    html.Br(),
    html.H1(children='Les revenus des entreprises et partenaires de la santé'),
    html.A(children=['Rapport'], href='https://docs.google.com/document/d/1PCWeUZ-qySD9mGjVfZhZ09Zx85vseR-PKRsAhVhFqP0/edit?usp=sharing'),
    html.Br(),
    html.Br(),
    dcc.Tabs([
        dcc.Tab(label='Résultats', children=[
            html.Br(),
            html.Br(),
            # HISTO CONTROL
            html.Div(
                children=[
                    html.Div(
                        children=[html.P()],
                        className='one columns'
                    ),
                    dcc.Dropdown(
                        id='who-dropdown_0',
                        options= WHO_OPTIONS,
                        value= WHO_OPTIONS[0]['value'],
                        className='two columns'
                    ),
                    dcc.Dropdown(
                        id='cat-dropdown_0',
                        options= CAT_OPTIONS[0],
                        value= CAT_OPTIONS[0][0]['value'],
                        className='two columns'
                    ),
                    html.Div(
                        children=[html.P()],
                        className='three columns'
                    ),
                    dcc.Dropdown(
                        id='who-dropdown_1',
                        options= WHO_OPTIONS,
                        value= WHO_OPTIONS[0]['value'],
                        className='two columns'
                    ),
                    dcc.Dropdown(
                        id='cat-dropdown_1',
                        options= CAT_OPTIONS[0],
                        value= CAT_OPTIONS[0][1]['value'],
                        className='two columns'
                    ),
                ],
                className='row flex-display'
            ),
            # HISTO
            html.Div(
                children=[
                    html.Div(
                        children=[
                            dcc.Graph(id='cat-fig-output_0'),
                        ],
                        className='pretty_container six columns'
                    ),
                    html.Div(
                        children=[
                            dcc.Graph( id='cat-fig-output_1'),
                        ],
                        className='pretty_container six columns'
                    )
                ],
                className='row flex-display'
            ),
            html.Br(),
            html.Br(),
            html.Br(),
            # SCATTER CONTROL
            html.Div(
                children=[
                    dcc.Dropdown(
                        id='who-dropdown_2',
                        options= WHO_OPTIONS,
                        value= WHO_OPTIONS[0]['value'],
                        className='four columns'
                    ),
                    dcc.Dropdown(
                        id='cat-dropdown_2',
                        options= CAT_OPTIONS[0],
                        value= CAT_OPTIONS[0][0]['value'],
                        className='four columns'
                    ),
                    dcc.Dropdown(
                        id='value-dropdown_2',
                        options= [{'label':helpers.translate(CURRENT_CAT_2, u), 'value':u } for u in dfs[CURRENT_WHO_2][CURRENT_CAT_2].unique()],
                        value=  dfs[CURRENT_WHO_2][CURRENT_CAT_2].unique()[0],
                        className='four columns'
                    ),
                ],
                className='row flex-display'
            ),
            # SCATTER
            html.Div(
                children=[
                    dcc.Graph(
                        id='cat-fig-output_2',
                    )
                ]
            )
        ]),
        dcc.Tab(label='Progression', children=[
            html.Br(),
            html.Br(),
            dcc.Graph(
                figure= getplot.getmontantfig(df_remu)),
            html.Br(),
            html.Br(),
            html.Br(),
            dcc.Graph(
                figure= getplot.gethistomontant(df_remu)),
            html.Br(),
            html.Br(),
            html.Br(),
            dcc.Graph(
                figure= getplot.get_montant_by_pays(df_remu)),
        ]),
        dcc.Tab(label='Infos', children=[
            html.Br(),
            html.Br(),
            html.Div(children=[
                html.Div(children=[
                    html.P(['Bénéficiaire :']),
                    html.P(['---- Catégorie    : 100% non null']),
                    html.P(['---- Pays         : 99.9% non null']),
                    html.P(['---- Titre        : 36.1% non null']),
                    html.P(['---- Spécialité   : 38.8%% non null']),
                    html.P(['---- Identifiant  : 100% non null'])],
                    className='three columns'
                ),
                html.Div(children=[
                    html.P(['Rémunération :']),
                    html.P(['---- Date    : 100% non null']),
                    html.P(['---- Montant : 100% non null'])],
                    className='three columns'
                ),
                html.Div(children=[
                    html.P(['Entreprise :']),
                    html.P(['---- Pays    : 100% non null']),
                    html.P(['---- Secteur : 100% non null'])],
                    className='three columns'
                )],
                className='row flex-display'
            ),
        ])
    ])
])

''' HISTO LEFT CALLBACKS'''

@app.callback(
    dash.dependencies.Output('cat-fig-output_0', 'figure'),
    [dash.dependencies.Input('cat-dropdown_0', 'value')])
def get_fig_for_0(value):
    # BENEF
    remu = helpers.arrange_to_plot(dfs[CURRENT_WHO_0].groupby(value).mean()[REMU_COL].sort_values())
    remu['labels'] = helpers.translate_list(value, remu['labels'])
    return {
        'data': [
            {'x': remu['labels'], 'y': remu['values'], 'type': 'bar', 'name': '.'},
        ],
        'layout': {
            'title': 'Moyennes des montants pour : %s > %s'%(WHO_MSG[CURRENT_WHO_0], helpers.cols_to_codes[value])
        }
    }
@app.callback(
    dash.dependencies.Output('cat-dropdown_0', 'options'),
    [dash.dependencies.Input('who-dropdown_0', 'value')])
def get_cat_option_0(value):
    global CURRENT_WHO_0
    CURRENT_WHO_0 = value
    return CAT_OPTIONS[value]

''' HISTO RIGHT CALLBACKS '''

@app.callback(
    dash.dependencies.Output('cat-fig-output_1', 'figure'),
    [dash.dependencies.Input('cat-dropdown_1', 'value')])
def get_fig_for_1(value):
    # BENEF
    remu = helpers.arrange_to_plot(dfs[CURRENT_WHO_1].groupby(value).mean()[REMU_COL].sort_values())
    remu['labels'] = helpers.translate_list(value, remu['labels'])
    return {
        'data': [
            {'x': remu['labels'], 'y': remu['values'], 'type': 'bar', 'name': '.'},
        ],
        'layout': {
            'title': 'Moyennes des montants pour : %s > %s'%(WHO_MSG[CURRENT_WHO_1], helpers.cols_to_codes[value])
        }
    }
@app.callback(
    dash.dependencies.Output('cat-dropdown_1', 'options'),
    [dash.dependencies.Input('who-dropdown_1', 'value')])
def get_cat_option_1(value):
    global CURRENT_WHO_1
    CURRENT_WHO_1 = value
    return CAT_OPTIONS[value]

''' SCATTER CALLBACKS '''

@app.callback(
    dash.dependencies.Output('cat-dropdown_2', 'options'),
    [dash.dependencies.Input('who-dropdown_2', 'value')])
def get_cat_option_2(value):
    global CURRENT_WHO_2
    CURRENT_WHO_2 = value
    return CAT_OPTIONS[value]
@app.callback(
    dash.dependencies.Output('value-dropdown_2', 'options'),
    [dash.dependencies.Input('cat-dropdown_2', 'value')])
def get_value_option_2(value):
    global CURRENT_WHO_2
    global CURRENT_CAT_2
    CURRENT_CAT_2 = value
    options = [{'label':helpers.translate(CURRENT_CAT_2, u), 'value':u } for u in dfs[CURRENT_WHO_2][CURRENT_CAT_2].dropna().unique()]
    return options
@app.callback(
    dash.dependencies.Output('cat-fig-output_2', 'figure'),
    [dash.dependencies.Input('value-dropdown_2', 'value')])
def get_fig_for_2(value):
    global CURRENT_WHO_2
    global CURRENT_CAT_2
    tmp = dfs[CURRENT_WHO_2][dfs[CURRENT_WHO_2][CURRENT_CAT_2] == value][[REMU_COL, DATE_COL]].sort_values(DATE_COL)
    tmp = tmp[tmp[DATE_COL] < pd.Timestamp('2019-07-01T12')]
    tmp = tmp[tmp[DATE_COL] > pd.Timestamp('2012-01-01T12')]

    return go.Figure(
        data=[go.Scatter(x=tmp[DATE_COL], y=tmp[REMU_COL])],
        layout= {
            'title': 'Evolution du montant des rémunération pour %s > %s > %s'%(WHO_MSG[CURRENT_WHO_1], helpers.cols_to_codes[CURRENT_CAT_2], helpers.translate(CURRENT_CAT_2, value))
        })

if __name__ == '__main__':
    app.run_server(debug=True) 