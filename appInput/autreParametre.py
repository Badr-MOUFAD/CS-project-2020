import dash

import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, State, Output

from Components import Table, navigate, Icons
from acceuil import app

from DataAndInstantiation import Instanciation


Jorf = Instanciation.Jorf


navigationBar1 = [
    navigate.NavigateButton(link='/parametrage-PMP-page1', direction='previous'),
    navigate.NavigateButton(link='/autre-parametre-page2', direction='next', id='autre-parametre-page1-next')
]

layoutPage1 = html.Div(children=[
    navigate.SliderAutre(currentProcédure=1),

    Table.TableStocksCommun(),

    html.Div(className='navigation-bar', children=navigationBar1),
])


@app.callback(
    [Output(component_id=stock.nom + '-cap-util', component_property='value') for stock in Jorf.stocksCommun.values()],
    [Input(component_id='autre-parametre-page1-next', component_property='n_clicks')],
    [State(component_id=stock.nom + '-cap-util', component_property='value') for stock in Jorf.stocksCommun.values()]
)
def insertCapUtil(*args):
    count = 1

    for stock in Jorf.stocksCommun.values():
        stock.capacitéUtilisé[0] = args[count]
        count += 1

    return args[1:]


navigationBar2 = [
    navigate.NavigateButton(link='/autre-parametre-page1', direction='previous'),
    navigate.NavigateButton(link='/autre-parametre-page3', direction='next', id='autre-parametre-page2-next')
]

layoutPage2 = html.Div(children=[
    navigate.SliderAutre(currentProcédure=2),

    Table.TableMaintenance(),

    html.Div(className='navigation-bar', children=navigationBar2)
])


@app.callback(
    [Output(component_id='row-maintenance-' + str(i), component_property='style') for i in range(20)],
    [Input(component_id='table-maintenance-plus', component_property='n_clicks')]
)
def addNewRow(n_clicks):
    if n_clicks == 0:
        raise dash.exceptions.PreventUpdate

    if n_clicks > 20:
        return

    state = []

    for i in range(n_clicks):
        state.append({'display': 'table-row'})

    for i in range(n_clicks, 20):
        state.append({'display': 'none'})

    return state


for i in range(20):
    @app.callback(
        Output(component_id='row-changement-reg-' + str(i), component_property='n_clicks'),

        [Input(component_id='autre-parametre-page3-next', component_property='n_clicks')],

        [State(component_id='lignes-changement-' + str(i), component_property='value'),
         State(component_id='date-changement-' + str(i), component_property='date'),
         State(component_id='nouveau-reg-' + str(i), component_property='value')]
    )
    def insertRégimeMarche(n_clicks, ligne, date, régime):
        if ligne is None or date is None or régime is None:
            raise dash.exceptions.PreventUpdate

        Jorf.insertRégimeDeMarche(ligne, date, régime)

        return 0#str(Jorf.emploiRégimeDeMarche)


navigationBar3 = [
    navigate.NavigateButton(link='/autre-parametre-page2', direction='previous'),
    navigate.IconButton(icon=Icons.Confirm, label='Confirmer', link='/autre-parametre-page4', id='autre-parametre-page3-next')
]

layoutPage3 = html.Div(children=[
    navigate.SliderAutre(currentProcédure=3),

    Table.TableChangementRégDeMarche(),

    html.Hr(),

    html.Div(className='navigation-bar', children=navigationBar3)
])

@app.callback(
    [Output(component_id='row-changement-reg-' + str(i), component_property='style') for i in range(20)],
    [Input(component_id='table-changement-reg-plus', component_property='n_clicks')]
)
def addNewRow(n_clicks):
    if n_clicks == 0:
        raise dash.exceptions.PreventUpdate

    if n_clicks > 20:
        return

    state = []

    for i in range(n_clicks):
        state.append({'display': 'table-row'})

    for i in range(n_clicks, 20):
        state.append({'display': 'none'})

    return state


for i in range(10):
    @app.callback(
        Output(component_id='row-maintenance-' + str(i), component_property='n_clicks'),

        [Input(component_id='autre-parametre-page2-next', component_property='n_clicks')],

        [State(component_id='maintenance-lignes-' + str(i), component_property='value'),
         State(component_id='maintenance-date-debut-' + str(i), component_property='date'),
         State(component_id='maintenance-date-fin-' + str(i), component_property='date'),
         State(component_id='maintenance-periodicite-' + str(i), component_property='value')]
    )
    def insertMaintenance(n_clicks, ligne, dateDébut, dateFin, périodicité):
        if ligne is None or dateDébut is None or dateFin is None or périodicité is None:
            raise dash.exceptions.PreventUpdate

        Jorf.insertMaintenance(ligne, dateDébut, dateFin, périodicité)

        return 0#str(Jorf.emploiMaintenance)


layoutPage4 = html.Div(children=[
    html.H4(children='Note importante:'),

    html.P(children=["Vous trouverez le fichier Input générée dans le bureau.\nLe processus de génération du fichier va prendre quelques seconds.\nClicker Cliquer sur Générer pour terminer."]),

    html.Hr(),

    dcc.Loading(children=[
        # html.Button(children=[
        #     navigate.IconButton(icon=Icons.Document, label='Générer', link='/', id='confirmer-saisi-input')
        # ])
        navigate.Button(link='', label='Générer', id='confirmer-saisi-input')
    ])

])

@app.callback(
    Output(component_id='confirmer-saisi-input', component_property='className'),
    [Input(component_id='confirmer-saisi-input', component_property='n_clicks')]
)
def genFichierInput(n_clicks):
    if n_clicks is None:
        raise dash.exceptions.PreventUpdate

    from insertionExcel import fonctions

    return ''
