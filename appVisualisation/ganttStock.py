import dash

import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input, Output, State

from acceuil import app
from Components import Graphs

import chart_studio.plotly
import plotly.figure_factory as ff

from DataAndInstantiation import Instanciation
from extractionExcel.fonctionStateStocks import updateStateStocks

Jorf = Instanciation.Jorf


layoutPage = html.Div(children=[
    html.H4(children='Gantt des stocks :'),

    html.Tr(children=[
        html.Th(children='Paramétrage :')
    ]),
    html.Tr(children=[
            html.Td(children=dcc.Input(className='mode-table', id='input-pourcentage-saturation', type="number",
                                   min=0, max=1, step=0.01, placeholder='Pourcentage saturation (par défaut 0.99)',
                                   persistence=True, persistence_type='memory', style={'width': '310px'})),
            html.Td(children=dcc.Input(className='mode-table', id='input-pourcentage-rupture', type="number",
                                   min=0, max=1, step=0.01, placeholder='Pourcentage rupture (par défaut 0.01)',
                                   persistence=True, persistence_type='memory', style={'width': '290px'}))
    ]),

    html.Br(),

    html.Table(children=[
        html.Tr(children=[
                html.Th(children='Sélectioner Entité :')
        ]),

        html.Tr(children=[
            html.Td(children=dcc.Dropdown(style={'width': '250px'}, id='gantt-menu-entité', placeholder='Sélectioner entité',
                            options=[{'label': 'Entité ' + entité, 'value': entité} for entité in Jorf.entités], value='')),
            ])
    ]),

    html.Br(),

    html.Th(children='Graphe :'),

    html.Div(className='graph', children=[
        dcc.Graph(id='gantt-stocks', figure=ff.create_gantt(
            df=[dict(Task='', Start='', Finish='', Resource='')], title=''))
    ]),

])



@app.callback(
    Output(component_id='gantt-stocks', component_property='figure'),
    [Input(component_id='gantt-menu-entité', component_property='value')]
)
def showGanttForEntité(nomEntité):
    if nomEntité == '':
        raise dash.exceptions.PreventUpdate

    return Graphs.FigureGanttStock(nomEntité)


@app.callback(
    Output(component_id='gantt-menu-entité', component_property='value'),
    [Input(component_id='input-pourcentage-rupture', component_property='value'),
     Input(component_id='input-pourcentage-saturation', component_property='value')]
)
def changePourcentage(prRupt, prSat):
    if prRupt is None and prSat is None:
        raise dash.exceptions.PreventUpdate

    Jorf.pourcentageSaturation = prSat
    Jorf.pourcentageRupture = prRupt

    updateStateStocks()
    return 'MP34'
