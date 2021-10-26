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


layoutPage = html.Div([
    html.H4(children='Gantt des lignes de production :'),

    html.Table(className='leave-space', children=[
        html.Tr(children=[
                html.Th(children='Sélectioner Entité :')
        ]),

        html.Tr(children=[
            html.Td(children=dcc.Dropdown(style={'width': '250px'}, id='gantt-ligne-production-menu-entité', placeholder='Sélectioner entité',
                            options=[{'label': 'Entité ' + entité, 'value': entité} for entité in Jorf.entités], value='')),
            ])
    ]),

    html.Th(children='Graphe :'),

    html.Div(className='graph', children=[
        dcc.Graph(id='gantt-ligne-production', figure=ff.create_gantt(
            df=[dict(Task='', Start='', Finish='', Resource='')], title=''))
    ]),

    html.Br(),

    html.Div(children=[
        html.H4(children="Plus de détails sur les lignes de Production :"),

        html.Table(className='leave-space', children=[
            html.Tr(children=[
                html.Th(children='Ligne de production'), html.Th(children='Interval de temps :')
            ]),

            html.Tr(children=[
                html.Td(children=dcc.Dropdown(style={'width': '250px'}, id='plus-info-select-ligne', placeholder='Sélectioner ligne',
                                              options=[])),
                html.Td(children=dcc.Dropdown(style={'width': '200px'}, id='plus-info-date-start', placeholder='Date début')),
                html.Td(children=dcc.Dropdown(style={'width': '200px'}, id='plus-info-date-end', placeholder='Date fin')),
                html.Td(children=html.Button(id='button-afficher-details', children='Afficher'))
            ])
        ]),

        html.Br(),

        html.Div(className='row', children=[
            html.Div(className='one-half column', id='graph-stock-amont',
                 style={'padding-right': '2px', 'padding-left': '2px', 'border-right': '1px dashed rgb(128, 128, 128)'},
                 children=[
                        html.H5("Stock Amont :"),
                        dcc.Graph()
            ]),

            html.Div(className='one-half column', id='graph-stock-aval',
                 style={'padding-right': '2px', 'padding-left': '2px'},
                 children=[
                        html.H5("Stock Aval :"),
                        dcc.Graph()
            ])
        ])
    ]),

    html.Hr(),

    html.Br(),
    html.Br()
])



@app.callback(
    [Output(component_id='gantt-ligne-production', component_property='figure'),
     Output(component_id='plus-info-select-ligne', component_property='options'),
     Output(component_id='plus-info-date-start', component_property='options'),
     Output(component_id='plus-info-date-end', component_property='options')],

    [Input(component_id='gantt-ligne-production-menu-entité', component_property='value')]
)
def showGanttForEntité(nomEntité):
    if nomEntité == '':
        raise dash.exceptions.PreventUpdate

    options = []
    options_ = [{'label': date, 'value': date} for date in Jorf.timeLine]

    for ligne in Jorf[nomEntité].getAllLignesDeProduction():
        options.append({'label': ligne.nom, 'value': ligne.nom})

    return Graphs.FigureGanttLignesProduction(nomEntité), options, options_, options_


@app.callback(
    [Output(component_id='graph-stock-amont', component_property='children'),
     Output(component_id='graph-stock-aval', component_property='children')],

    [Input(component_id='button-afficher-details', component_property='n_clicks')],

    [State(component_id='plus-info-select-ligne', component_property='value'),
     State(component_id='plus-info-date-start', component_property='value'),
     State(component_id='plus-info-date-end', component_property='value')]
)
def afficheDetails(n_clicks, nomLigne, dateStart, dateEnd):
    if n_clicks is None or nomLigne is None:
        raise dash.exceptions.PreventUpdate

    if dateStart is None or dateEnd is None:
        raise dash.exceptions.PreventUpdate

    atelier = Jorf.getAtelierOfLigne(nomLigne)

    if atelier is not None:
        graphsStockAmont = html.Div(children=[
            html.H5(children='Stocks amont ' + nomLigne),

            *[html.Div(children=[Graphs.GraphEvolutionStock(nomStock=stock, interval=[dateStart, dateEnd]), html.Hr()])
                for stock in atelier.stocksAmont]
        ])

        graphsStockAval = html.Div(children=[
            html.H5(children='Stock aval ' + nomLigne),

            *[html.Div(children=[Graphs.GraphEvolutionStock(nomStock=stock, interval=[dateStart, dateEnd]), html.Hr()])
                for stock in atelier.stocksAval]
        ])

        return graphsStockAmont, graphsStockAval

    ligneEngrais = Jorf.getLigne(nomLigne)

    graphsStockAmont = html.Div(children=[
        html.H5(children='Stocks amont ' + nomLigne),

        *[html.Div(children=[Graphs.GraphEvolutionStock(nomStock=stock, interval=[dateStart, dateEnd]), html.Hr()])
          for stock in ligneEngrais.stocksAmont]
        ])

    return graphsStockAmont, nomLigne + "n'a pas stocks Aval"
