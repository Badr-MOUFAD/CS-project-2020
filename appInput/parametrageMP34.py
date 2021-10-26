import dash

import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
from DataAndInstantiation import Instanciation

from acceuil import app
from Components import Table
from Components import navigate

from Components.GenInputOuput import generateInputForLignes, generateOutputForLignes, \
    generateInputForStocks, generateOutputForStocks, generateStateForLignes, generateStateForStocks


Jorf = Instanciation.Jorf

currentEntité = 'MP34'
numEntité = 1


navigationBar1 = html.Div(className='navigation-bar', children=[
    navigate.NavigateButton(link='/parametrage-' + 'MP34' + '-page1', direction='double-previous'),
    navigate.NavigateButton(link='/parametrage-' + currentEntité + '-page2', direction='next', id=currentEntité + '-next-button-page1')
])

layoutPage1 = html.Div(children=[
    navigate.SliderParametrage(currentEntité=numEntité, currentProcédure=1),
    Table.TableDisponibilitéRégimeDeMarche(Jorf[currentEntité]),
    navigationBar1
])


@app.callback(
    generateOutputForLignes(entité=currentEntité) + [
        Output(component_id='store-DispoLigneEngrais-' + Jorf[currentEntité].nom, component_property='data')],

    [Input(component_id=currentEntité + '-next-button-page1', component_property='n_clicks')],

    generateStateForLignes(entité=currentEntité)
)
def insertDispoReg(n_clicks, *args):
    if n_clicks is None:
        raise dash.exceptions.PreventUpdate

    state = []
    storageDispo = []
    count = 0

    for ligne in Jorf[currentEntité].lignesEngrais.values():
        ligne.disponibilité = int(args[count])
        state.append(not bool(args[count]))

        if args[count]:
            storageDispo.append({'label': ligne.nom, 'value': ligne.nom})

        count += 1

        ligne.régimeDeMarche[0] = args[count]
        count += 1

    for atelier in Jorf[currentEntité].ateliers.values():
        for ligne in atelier.lignesDeProduction.values():
            ligne.disponibilité = int(args[count])
            state.append(not bool(args[count]))
            count += 1

            ligne.régimeDeMarche[0] = args[count]
            count += 1

    state.append(storageDispo)

    return state


navigationBar3 = html.Div(className='navigation-bar', children=[
    navigate.NavigateButton(link='/parametrage-' + currentEntité + '-page2', direction='previous'),
    navigate.NavigateButton(link='/parametrage-' + currentEntité + '-page4', direction='next', id=currentEntité + '-next-button-page3')
])
layoutPage3 = html.Div(children=[
    navigate.SliderParametrage(currentEntité=numEntité, currentProcédure=3),
    Table.TableStocks(Jorf[currentEntité]),
    navigationBar3
])


@app.callback(
    generateOutputForStocks(entité=Jorf[currentEntité]),

    [Input(component_id=currentEntité + '-next-button-page3', component_property='n_clicks')],

    generateStateForStocks(Jorf[currentEntité])
)
def insertCapUtil(n_clicks, *args):
    if n_clicks is None:
        raise dash.exceptions.PreventUpdate

    count = 0

    for stock in Jorf[currentEntité].stocks.values():
        stock.capacitéUtilisé[0] = args[count]
        count += 1

    return list(range(len(args)))


navigationBar2 = html.Div(className='navigation-bar', children=[
    navigate.NavigateButton(link='/parametrage-' + currentEntité + '-page1', direction='previous'),
    navigate.NavigateButton(link='/parametrage-' + currentEntité + '-page3', direction='next', id=currentEntité + '-next-button-page2')
])

layoutPage2 = html.Div(children=[
    navigate.SliderParametrage(currentEntité=numEntité, currentProcédure=2),
    Table.TableCarnetCommande(entité=Jorf[currentEntité]),

    navigationBar2
])


@app.callback(
    [Output(component_id='row-' + str(i) + '-carnet-' + Jorf[currentEntité].nom, component_property='style') for i in
     range(20)],
    [Input(component_id='table-carnet-plus-' + Jorf[currentEntité].nom, component_property='n_clicks')]
)
def addNewLigneInCarnet(n_clicks):
    if n_clicks > 20:
        return
    if n_clicks == 0:
        raise dash.exceptions.PreventUpdate

    state = []

    for i in range(n_clicks):
        state.append({'display': 'table-row'})

    for i in range(n_clicks, 20):
        state.append({'display': 'none'})

    return state


for i in range(4):
    @app.callback(
        Output(component_id='row-' + str(i) + '-carnet-' + Jorf[currentEntité].nom, component_property='n_clicks'),
        [Input(component_id=currentEntité + '-next-button-page2', component_property='n_clicks')],
        [State(component_id=Jorf[currentEntité].nom + '-carnet-' + label + str(i), component_property='value')
         for label in ['engrais-', 'ligne-', 'quantite-', 'temps-']]
    )
    def insertCommande(n_clicks, engrais, ligne, quantité, temps):
        if n_clicks is None:
            raise dash.exceptions.PreventUpdate

        if engrais is None or ligne is None or quantité is None or temps is None:
            raise dash.exceptions.PreventUpdate

        ligneEngrais = Jorf[currentEntité].lignesEngrais[ligne]
        ligneEngrais.insertCommande(engrais=engrais, quantité=quantité, tempsLancement=temps)

        return 0

for i in range(20):
    @app.callback(
        Output(component_id=Jorf[currentEntité].nom + '-carnet-ligne-' + str(i), component_property='options'),
        [Input(component_id='store-DispoLigneEngrais-' + Jorf[currentEntité].nom, component_property='data')]
    )
    def updateOption(data):
        return data


navigationBar4_ = list(range(4))
layoutPage4_ = list(range(4))

for i in range(4):
    navigationBar4_[i] = html.Div(className="navigation-bar", children=[
        navigate.NavigateButton(link='/parametrage-' + currentEntité + '-page' + str(i + 4 - 1), direction='previous'),
        navigate.NavigateButton(link='/parametrage-' + currentEntité + '-page' + str(i + 4 + 1), direction='next',
                                id=currentEntité + '-next-button-page4' + str(i))
    ])

    layoutPage4_[i] = html.Div(children=[
        navigate.SliderParametrage(currentEntité=numEntité, currentProcédure=4),

        html.Div(children=[
            Table.TableEchange(entité=Jorf[currentEntité].nom, fournisseur=fournisseur)
            for fournisseur in Instanciation.generateListEchange(Jorf[currentEntité].nom)[i * 2: (i + 1) * 2]
        ]),

        navigationBar4_[i]
    ])

    if i == 3:
        navigationBar4_[i] = html.Div(className="navigation-bar", children=[
            navigate.NavigateButton(link='/parametrage-' + currentEntité + '-page' + str(i + 4 - 1),
                                    direction='previous'),
            navigate.NavigateButton(link='/parametrage-JFD-page1', direction='double-next')
        ])
        layoutPage4_[i] = html.Div(children=[
            navigate.SliderParametrage(currentEntité=numEntité, currentProcédure=4),

            html.Div(children=[
                Table.TableEchange(entité=Jorf[currentEntité].nom, fournisseur=fournisseur)
                for fournisseur in Instanciation.generateListEchange(Jorf[currentEntité].nom)[i * 2: (i + 1) * 2]
            ]),

            html.Div(children=[
                Table.TableExportMP34()
            ]),

            navigationBar4_[i]
        ])
    ##

for fournisseur in Instanciation.generateListEchange(Jorf[currentEntité].nom):
    @app.callback(
        [Output(component_id='row-' + str(i) + '-echange-' + Jorf[currentEntité].nom + fournisseur,
                component_property='style')
         for i in range(10)],
        [Input(component_id='table-echange-plus-' + Jorf[currentEntité].nom + fournisseur,
               component_property='n_clicks')]
    )
    def addNewLigneInEchange(n_cliclks):
        state = []

        for i in range(n_cliclks):
            state.append({'display': 'table-row'})

        for i in range(n_cliclks, 10):
            state.append({'display': 'none'})

        return state

for fournisseur in ['extérieur']:
    count = 0

    for i in range(10):
        @app.callback(
             Output(component_id='row-' + str(i) + '-echange-' + Jorf[currentEntité].nom + fournisseur,
                    component_property='n_clicks'),
            #Output(component_id='test', component_property='children'), id='row-' + index + '-echange-' + entité + fournisseur,
            [Input(component_id=currentEntité + '-next-button-page4' + str(int(count / 2)), component_property='n_clicks')],

            [State(component_id='echange-date' + Jorf[currentEntité].nom + fournisseur + str(i),
                   component_property='date')] +
            [State(component_id='echange-' + label + Jorf[currentEntité].nom + fournisseur + str(i),
                   component_property='value')
             for label in ['produit', 'temps', 'quantité', "débit"]]
        )
        def insertEchange_(n_clicks, date, produit, temps, quantité, débit):
            if date is None or produit is None or temps is None or débit is None or quantité is None:
                raise dash.exceptions.PreventUpdate

            Jorf[currentEntité].insertEchange(fournisseur='extérieur',
                                              date=date, débit=débit, produit=produit,
                                              heure=temps, quantité=quantité)

            return 0

for fournisseur in ['JFD']:
    count = 1

    for i in range(10):
        @app.callback(
             Output(component_id='row-' + str(i) + '-echange-' + Jorf[currentEntité].nom + fournisseur,
                    component_property='n_clicks'),
            #Output(component_id='test', component_property='children'), id='row-' + index + '-echange-' + entité + fournisseur,
            [Input(component_id=currentEntité + '-next-button-page4' + str(int(count / 2)), component_property='n_clicks')],

            [State(component_id='echange-date' + Jorf[currentEntité].nom + fournisseur + str(i),
                   component_property='date')] +
            [State(component_id='echange-' + label + Jorf[currentEntité].nom + fournisseur + str(i),
                   component_property='value')
             for label in ['produit', 'temps', 'quantité', "débit"]]
        )
        def insertEchange_(n_clicks, date, produit, temps, quantité, débit):
            if date is None or produit is None or temps is None or débit is None or quantité is None:
                raise dash.exceptions.PreventUpdate

            Jorf[currentEntité].insertEchange(fournisseur='JFD',
                                              date=date, débit=débit, produit=produit,
                                              heure=temps, quantité=quantité)

            return 0


for fournisseur in ['JFF']:
    count = 2

    for i in range(10):
        @app.callback(
             Output(component_id='row-' + str(i) + '-echange-' + Jorf[currentEntité].nom + fournisseur,
                    component_property='n_clicks'),
            #Output(component_id='test', component_property='children'), id='row-' + index + '-echange-' + entité + fournisseur,
            [Input(component_id=currentEntité + '-next-button-page4' + str(int(count / 2)), component_property='n_clicks')],

            [State(component_id='echange-date' + Jorf[currentEntité].nom + fournisseur + str(i),
                   component_property='date')] +
            [State(component_id='echange-' + label + Jorf[currentEntité].nom + fournisseur + str(i),
                   component_property='value')
             for label in ['produit', 'temps', 'quantité', "débit"]]
        )
        def insertEchange_(n_clicks, date, produit, temps, quantité, débit):
            if date is None or produit is None or temps is None or débit is None or quantité is None:
                raise dash.exceptions.PreventUpdate

            Jorf[currentEntité].insertEchange(fournisseur='JFF',
                                              date=date, débit=débit, produit=produit,
                                              heure=temps, quantité=quantité)

            return 0


for fournisseur in ['JFO']:
    count = 3

    for i in range(10):
        @app.callback(
             Output(component_id='row-' + str(i) + '-echange-' + Jorf[currentEntité].nom + fournisseur,
                    component_property='n_clicks'),
            #Output(component_id='test', component_property='children'), id='row-' + index + '-echange-' + entité + fournisseur,
            [Input(component_id=currentEntité + '-next-button-page4' + str(int(count / 2)), component_property='n_clicks')],

            [State(component_id='echange-date' + Jorf[currentEntité].nom + fournisseur + str(i),
                   component_property='date')] +
            [State(component_id='echange-' + label + Jorf[currentEntité].nom + fournisseur + str(i),
                   component_property='value')
             for label in ['produit', 'temps', 'quantité', "débit"]]
        )
        def insertEchange_(n_clicks, date, produit, temps, quantité, débit):
            if date is None or produit is None or temps is None or débit is None or quantité is None:
                raise dash.exceptions.PreventUpdate

            Jorf[currentEntité].insertEchange(fournisseur='JFO',
                                              date=date, débit=débit, produit=produit,
                                              heure=temps, quantité=quantité)

            return 0

for fournisseur in ['JFQ']:
    count = 4

    for i in range(10):
        @app.callback(
             Output(component_id='row-' + str(i) + '-echange-' + Jorf[currentEntité].nom + fournisseur,
                    component_property='n_clicks'),
            #Output(component_id='test', component_property='children'), id='row-' + index + '-echange-' + entité + fournisseur,
            [Input(component_id=currentEntité + '-next-button-page4' + str(int(count / 2)), component_property='n_clicks')],

            [State(component_id='echange-date' + Jorf[currentEntité].nom + fournisseur + str(i),
                   component_property='date')] +
            [State(component_id='echange-' + label + Jorf[currentEntité].nom + fournisseur + str(i),
                   component_property='value')
             for label in ['produit', 'temps', 'quantité', "débit"]]
        )
        def insertEchange_(n_clicks, date, produit, temps, quantité, débit):
            if date is None or produit is None or temps is None or débit is None or quantité is None:
                raise dash.exceptions.PreventUpdate

            Jorf[currentEntité].insertEchange(fournisseur='JFQ',
                                              date=date, débit=débit, produit=produit,
                                              heure=temps, quantité=quantité)

            return 0

for fournisseur in ['JFT']:
    count = 5

    for i in range(10):
        @app.callback(
             Output(component_id='row-' + str(i) + '-echange-' + Jorf[currentEntité].nom + fournisseur,
                    component_property='n_clicks'),
            #Output(component_id='test', component_property='children'), id='row-' + index + '-echange-' + entité + fournisseur,
            [Input(component_id=currentEntité + '-next-button-page4' + str(int(count / 2)), component_property='n_clicks')],

            [State(component_id='echange-date' + Jorf[currentEntité].nom + fournisseur + str(i),
                   component_property='date')] +
            [State(component_id='echange-' + label + Jorf[currentEntité].nom + fournisseur + str(i),
                   component_property='value')
             for label in ['produit', 'temps', 'quantité', "débit"]]
        )
        def insertEchange_(n_clicks, date, produit, temps, quantité, débit):
            if date is None or produit is None or temps is None or débit is None or quantité is None:
                raise dash.exceptions.PreventUpdate

            Jorf[currentEntité].insertEchange(fournisseur='JFT',
                                              date=date, débit=débit, produit=produit,
                                              heure=temps, quantité=quantité)

            return 0


for fournisseur in ['IMACID']:
    count = 6

    for i in range(10):
        @app.callback(
             Output(component_id='row-' + str(i) + '-echange-' + Jorf[currentEntité].nom + fournisseur,
                    component_property='n_clicks'),
            #Output(component_id='test', component_property='children'), id='row-' + index + '-echange-' + entité + fournisseur,
            [Input(component_id=currentEntité + '-next-button-page4' + str(int(count / 2)), component_property='n_clicks')],

            [State(component_id='echange-date' + Jorf[currentEntité].nom + fournisseur + str(i),
                   component_property='date')] +
            [State(component_id='echange-' + label + Jorf[currentEntité].nom + fournisseur + str(i),
                   component_property='value')
             for label in ['produit', 'temps', 'quantité', "débit"]]
        )
        def insertEchange_(n_clicks, date, produit, temps, quantité, débit):
            if date is None or produit is None or temps is None or débit is None or quantité is None:
                raise dash.exceptions.PreventUpdate

            Jorf[currentEntité].insertEchange(fournisseur='IMACID',
                                              date=date, débit=débit, produit=produit,
                                              heure=temps, quantité=quantité)

            return 0

for fournisseur in ['PMP']:
    count = 7

    for i in range(10):
        @app.callback(
             Output(component_id='row-' + str(i) + '-echange-' + Jorf[currentEntité].nom + fournisseur,
                    component_property='n_clicks'),
            #Output(component_id='test', component_property='children'), id='row-' + index + '-echange-' + entité + fournisseur,
            [Input(component_id=currentEntité + '-next-button-page4' + str(int(count / 2)), component_property='n_clicks')],

            [State(component_id='echange-date' + Jorf[currentEntité].nom + fournisseur + str(i),
                   component_property='date')] +
            [State(component_id='echange-' + label + Jorf[currentEntité].nom + fournisseur + str(i),
                   component_property='value')
             for label in ['produit', 'temps', 'quantité', "débit"]]
        )
        def insertEchange_(n_clicks, date, produit, temps, quantité, débit):
            if date is None or produit is None or temps is None or débit is None or quantité is None:
                raise dash.exceptions.PreventUpdate

            Jorf[currentEntité].insertEchange(fournisseur='PMP',
                                              date=date, débit=débit, produit=produit,
                                              heure=temps, quantité=quantité)

            return 0


@app.callback(
    [Output(component_id='row-' + str(i) + '-export',
                component_property='style') for i in range(10)],
    [Input(component_id='table-export-plus', component_property='n_clicks')]
)
def addRowExport(n_clicks):
    state = []

    for i in range(n_clicks):
        state.append({'display': 'table-row'})

    for i in range(n_clicks, 10):
        state.append({'display': 'none'})

    return state



for i in range(10):
    @app.callback(
        Output(component_id='row-' + str(i) + '-export',
               component_property='n_clicks'),
        [Input(component_id='export-date' + str(i),
               component_property='date')] +
        [Input(component_id='export-' + label + str(i),
               component_property='value')
         for label in ['temps', 'quantité', "débit"]]
    )
    def insertExport(date, temps, quantité, débit):
        if date is None or temps is None or débit is None or quantité is None:
            raise dash.exceptions.PreventUpdate

        Jorf.insertExportMP34(date=date, débit=débit, heure=temps, quantité=quantité)

        return 0