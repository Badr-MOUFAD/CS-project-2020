import dash
import dash_html_components as html
import dash_core_components as dcc

from dash.dependencies import Input, Output, State

from DataAndInstantiation import Instanciation
from Components import navigate
from acceuil import app

from insertionExcel.dateManipulation import adjustFormatDate

Jorf = Instanciation.Jorf

# layout = html.Div(children=[
#     html.H4(children='Saisie de la date :'),
#
#     html.Div(className='content', children=[
#
#         html.Table(children=[
#             html.Tr(children=[
#                html.Th(children='Date de début'),
#                html.Th(children='Durée de la simulation')
#             ]),
#
#             html.Tr(children=[
#                 html.Td(children=[dcc.DatePickerSingle(id='date-debut-scenario', date=Jorf.date, persistence=True, persistence_type='memory')]),
#                 html.Td(children=[dcc.Input(id='duree-scenario', type='number', value=Jorf.durée,
#                                             min=1, required=True, persistence=True, persistence_type='memory')])
#             ])
#         ])
#
#     ]),
#
#     html.Button(className='leave-space', id='commencer-saisie', n_clicks=0, children='Commencer la saisie')
# ])


# @app.callback(
#     [Output(component_id='side-bar', component_property='children'), Output(component_id='url', component_property='pathname')],
#     [Input(component_id='commencer-saisie', component_property='n_clicks')],
#     [State(component_id='date-debut-scenario', component_property='date'), State(component_id='duree-scenario', component_property='value')]
# )
# def insertDateDuration(n_clicks, date, duree):
#     if n_clicks == 0:
#         raise dash.exceptions.PreventUpdate
#
#     Jorf.date = date
#     Jorf.durée = duree
#
#     sideBar = [
#
#         html.Button(className='side-bar', children=[
#             dcc.Link(className='side-bar', children=['Paramétrage des entités'], href='/parametrage-entites')
#         ]),
#         html.Button(className='side-bar', children=[
#             dcc.Link(className='side-bar', children=['Emploi des maintenances'], href='/emploi-maintenances')
#         ]),
#         html.Button(className='side-bar', children=[
#             dcc.Link(className='side-bar', children=['Emploi des régimes de marche'], href='/emploi-regime-marche')
#         ])
#     ]
#
#     pathname = '/parametrage-MP34-page1'
#
#     return sideBar, pathname


layout = html.Div(children=[
    html.H4(children='Saisie de la date :'),

    html.Div(className='content', children=[

        html.Table(id='date-duree-scenario', children=[
            html.Tr(children=[
               html.Th(children='Date de début'),
               html.Th(children='Durée de la simulation')
            ]),

            html.Tr(children=[
                html.Td(children=[dcc.DatePickerSingle(id='date-debut-scenario', display_format='D/M/YYYY',
                                                       persistence=True, persistence_type='memory')]),
                html.Td(children=[dcc.Input(id='duree-scenario', type='number', value=1,
                                            min=1, required=True, persistence=True, persistence_type='memory')])
            ])
        ])

    ]),

    html.Br(),
    navigate.Button(link='/parametrage-MP34-page1', label='Commencer la saisi', id='commencer-saisi')
])


@app.callback(
    Output(component_id='date-duree-scenario', component_property='n_clicks'),
    [Input(component_id='commencer-saisi', component_property='n_clicks')],
    [State(component_id='date-debut-scenario', component_property='date'), State(component_id='duree-scenario', component_property='value')]
)
def insertDateDuration(n_clicks, date, duree):
    if n_clicks == 0:
        raise dash.exceptions.PreventUpdate

    Jorf.date = adjustFormatDate(date)
    Jorf.durée = duree

    return 0
