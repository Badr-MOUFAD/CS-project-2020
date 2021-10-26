import dash

import dash_html_components as html
import dash_core_components as dcc

from dash.dependencies import Input, Output
from Components import Graphs

from acceuil import app
from DataAndInstantiation import Instanciation

Jorf = Instanciation.Jorf


layoutPage = html.Div(children=[
    html.H4(children='Evolution des stocks :'),

    html.Tr(children=[
        html.Th(children='Paramétrage :')
    ]),
    html.Tr(children=[
            html.Td(children=dcc.Input(className='mode-table', id='input-pourcentage-saturation-evolution', type="number",
                                   min=0, max=1, step=0.01, placeholder='Pourcentage saturation (par défaut 0.99)',
                                   persistence=True, persistence_type='memory', style={'width': '310px'})),
            html.Td(children=dcc.Input(className='mode-table', id='input-pourcentage-rupture-evolution', type="number",
                                   min=0, max=1, step=0.01, placeholder='Pourcentage rupture (par défaut 0.01)',
                                   persistence=True, persistence_type='memory', style={'width': '290px'}))
    ]),

    html.Br(),

    html.Table(children=[
        html.Tr(children=[
            html.Th(children='Filtre :')
        ]),

        html.Tr(children=[
            html.Td(children=dcc.Dropdown(style={'width': '250px'}, id='evolution-menu-entité', placeholder='Sélectioner entité',
                        options=[{'label': 'entité ' + entité, 'value': entité} for entité in Jorf.entités], value='MP34')),

            html.Td(children=dcc.Dropdown(style={'width': '400px'}, id='evolution-menu-stock', placeholder='Sélectioner stock',
                                          options=[{'label': stock, 'value': stock} for stock in Jorf['MP34'].stocks]))
        ])
    ]),

    html.Br(),

    html.Th(children='Graphe :'),

    html.Div(id='evolution-graph', className='graph', children=[
        Graphs.GraphEvolutionStock('')
    ]),

    html.Hr()
])


@app.callback(
    Output(component_id='evolution-menu-stock', component_property='options'),
    [Input(component_id='evolution-menu-entité', component_property='value')]
)
def selectEntité(entité):
    if entité is None:
        raise dash.exceptions.PreventUpdate

    options = [{'label': stock, 'value': stock} for stock in Jorf[entité].stocks]

    return options


@app.callback(
    Output(component_id='evolution-graph', component_property='children'),
    [Input(component_id='evolution-menu-stock', component_property='value')]
)
def selectStock(stock):
    if stock is None:
        raise dash.exceptions.PreventUpdate

    return Graphs.GraphEvolutionStock(nomStock=stock)

@app.callback(
    Output(component_id='evolution-graph', component_property='figure'),
    [Input(component_id='evolution-menu-stock', component_property='value')]
)
def selectStock(stock):
    if stock is None:
        raise dash.exceptions.PreventUpdate

    return Graphs.GraphEvolutionStock(nomStock=stock)


@app.callback(
    [Output(component_id='evolution-menu-entité', component_property='value'),
     Output(component_id='evolution-menu-stock', component_property='value')],
    [Input(component_id='input-pourcentage-rupture-evolution', component_property='value'),
     Input(component_id='input-pourcentage-saturation-evolution', component_property='value')]
)
def changePourcentageRS(prRup, prSat):
    if prRup is None and prSat is None:
        raise dash.exceptions.PreventUpdate

    Jorf.pourcentageSaturation = prSat
    Jorf.pourcentageRupture = prRup

    return 'MP34', 'Stock_Soufre_MP34'

