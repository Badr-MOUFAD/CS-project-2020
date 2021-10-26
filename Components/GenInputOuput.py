from dash.dependencies import Input, Output, State
from DataAndInstantiation import Instanciation

Jorf = Instanciation.Jorf


def generateInputForLignes(entité):
    result = []

    for ligne in Jorf[entité].lignesEngrais.values():
        result.append(Input(component_id=ligne.nom + '-dispo', component_property='on'))
        result.append(Input(component_id=ligne.nom + '-reg', component_property='value'))

    for atelier in Jorf[entité].ateliers.values():
        for ligne in atelier.lignesDeProduction.values():
            result.append(Input(component_id=ligne.nom + '-dispo', component_property='on'))
            result.append(Input(component_id=ligne.nom + '-reg', component_property='value'))

    return result

def generateStateForLignes(entité):
    result = []

    for ligne in Jorf[entité].lignesEngrais.values():
        result.append(State(component_id=ligne.nom + '-dispo', component_property='on'))
        result.append(State(component_id=ligne.nom + '-reg', component_property='value'))

    for atelier in Jorf[entité].ateliers.values():
        for ligne in atelier.lignesDeProduction.values():
            result.append(State(component_id=ligne.nom + '-dispo', component_property='on'))
            result.append(State(component_id=ligne.nom + '-reg', component_property='value'))

    return result




def generateOutputForLignes(entité):
    result = []

    for ligne in Jorf[entité].lignesEngrais.values():
        result.append(Output(component_id=ligne.nom + '-reg', component_property='disabled'))
       # result.append(Output(component_id=ligne.nom + '-reg', component_property='value'))

    for atelier in Jorf[entité].ateliers.values():
        for ligne in atelier.lignesDeProduction.values():
            result.append(Output(component_id=ligne.nom + '-reg', component_property='disabled'))
         #   result.append(Output(component_id=ligne.nom + '-reg', component_property='value'))

    return result


def generateInputForStocks(entité):
    result = []

    for stock in entité.stocks.values():
        result.append(Input(component_id=stock.nom + '-cap-util', component_property='value'))

    return result

def generateStateForStocks(entité):
    result = []

    for stock in entité.stocks.values():
        result.append(State(component_id=stock.nom + '-cap-util', component_property='value'))

    return result


def generateOutputForStocks(entité):
    result = []

    for stock in entité.stocks.values():
        result.append(Output(component_id=stock.nom + '-cap-util', component_property='n_clicks'))

    return result