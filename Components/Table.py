import dash_html_components as html
import dash_core_components as dcc
from dash_daq import BooleanSwitch

from DataAndInstantiation import Instanciation
from Components import Icons

import datetime as Date


Jorf = Instanciation.Jorf


def RowDisponibilitéRégime(ligne):
    row = html.Tr(children=[
        html.Td(children=ligne.nom), html.Td(children=BooleanSwitch(id=ligne.nom + '-dispo', on=True)),
        html.Td(children=dcc.Input(className='mode-table', id=ligne.nom + '-reg', type="number",
                                   min=0, max=1, step=0.01, value=1, required=True,
                                   persistence=True, persistence_type='memory'))
    ])

    return row


def RowCapacité(stock):
    row = html.Tr(children=[
        html.Td(children=stock.nom), html.Td(children=dcc.Input(className='mode-table', id=stock.nom + '-cap-util', type="number",
                                   min=0, max=stock.capacitéMax, value=stock.capacitéUtilisé[0], required=True,
                                                                persistence=True, persistence_type='memory'))
    ])

    return row


def RowCarnetCommande(index, entité):
    ligneDisponible = []
    displayProp = 'table-row' if index != 0 else 'none'

    row = html.Tr(style={'display': displayProp}, id='row-' + index + '-carnet-' + entité.nom, children=[
        html.Td(children=dcc.Dropdown(style={'width': '250px'}, id=entité.nom + '-carnet-engrais-' + index, placeholder='Sélectioner engrais',
                                      options=[{'label': engrais, 'value': engrais}for engrais in Jorf.listEngrais])),

        html.Td(children=dcc.Dropdown(style={'width': '250px'}, id=entité.nom + '-carnet-ligne-' + index, placeholder="sélectioner ligne Engrais",
                                      options=[{'label': ligne, 'value': ligne} for ligne in ligneDisponible])),

        html.Td(children=dcc.Input(id=entité.nom + '-carnet-quantite-' + index, className='mode-table', type="number", min=0)),
        html.Td(children=dcc.Input(id=entité.nom + '-carnet-temps-' + index, className='mode-table', type="number", min=0, max=24))
    ])

    return row


def RowEchange(index, entité, fournisseur):
    #listOptions = Jorf.PRODUIT_ECHANGEABLE if fournisseur != 'extérieur' else Jorf.PRODUIT_ECHANGEABLE_EXTERIEUR

    listNomProduit = Jorf.PRODUIT_ECHANGEABLE if fournisseur != 'extérieur' else Jorf.PRODUIT_ECHANGEABLE_EXTERIEUR
    listProduit = Jorf[entité].PRODUIT_ECHANGEABLE if fournisseur != 'extérieur' else Jorf[entité].PRODUIT_ECHANGEABLE_EXTERIEUR

    listOptions = []
    for i in range(len(listNomProduit)):
        listOptions.append([listNomProduit[i], listProduit[i]])

    displayProp = 'table-row' if index != 0 else 'none'

    row = html.Tr(style={'display': displayProp}, id='row-' + index + '-echange-' + entité + fournisseur, children=
    [html.Td(children=dcc.Dropdown(style={'width': '280px'}, id='echange-produit' + entité + fournisseur + index, placeholder='Sélection produit',
                                   options=[{'label': produit[0], 'value': produit[1]} for produit in listOptions])),
     html.Td(children=dcc.DatePickerSingle(id='echange-date' + entité + fournisseur + index, display_format='D/M/YYYY'))] +
    [html.Td(children=dcc.Input(className='mode-table', id='echange-' + label + entité + fournisseur + index, type='number', min=0,
                                placeholder="Saisir " + label))
             for label in ['temps', 'quantité', 'débit']]
    )

    return row


def RowExportMP34(index):
    displayProp = 'table-row' if index != 0 else 'none'

    row = html.Tr(style={'display': displayProp}, id='row-' + index + '-export', children=[
            html.Td(children=dcc.DatePickerSingle(
                    id='export-date' + index,
                    display_format='D/M/YYYY'))] +
        [html.Td(children=dcc.Input(className='mode-table', id='export-' + label + index, type='number', min=0,
            placeholder="Saisir " + label))

         for label in ['temps', 'quantité', 'débit']
    ])

    return row


def RowMaintenance(index):
    displayProp = 'table-row' if index != 0 else 'none'

    row = html.Tr(id='row-maintenance-' + index, style={'display': displayProp}, children=[
        html.Td(dcc.Dropdown(id='maintenance-lignes-' + index, style={'width': '280px'},
                             options=[{'label': ligne.nom, 'value': ligne.mappingMaintenance} for ligne in Jorf.getAllLignesDeProduction()],
                             placeholder='Sélectioner ligne')),
        html.Td(dcc.DatePickerSingle(id='maintenance-date-debut-' + index, display_format='D/M/YYYY')),
        html.Td(dcc.DatePickerSingle(id='maintenance-date-fin-' + index, placeholder='Date fin', display_format='D/M/YYYY')),
        html.Td(dcc.Input(className='table-mode', id='maintenance-periodicite-' + index, value=0, required=True, min=0))
    ])

    return row


def RowChangementRégMarche(index):
    displayProp = 'table-row' if index != 0 else 'none'

    row = html.Tr(id='row-changement-reg-' + index, style={'display': displayProp}, children=[
        html.Td(dcc.Dropdown(id='lignes-changement-' + index, style={'width': '250px'},placeholder='Sélectionner ligne',
                             options=[{'label': ligne.nom, 'value': ligne.nom} for ligne in
                                      Jorf.getAllLignesDeProduction()])),
        html.Td(dcc.DatePickerSingle(id='date-changement-' + index, display_format='D/M/YYYY')),
        html.Td(dcc.Input(className='table-mode', id='nouveau-reg-' + index, value=0, required=True, min=0))
    ])

    return row


def table(atelier):
    content = []

    for ligne in atelier.lignesDeProduction.values():
        content.append(RowDisponibilitéRégime(ligne))

    return html.Table(className='leave-space', children=[
        html.Tr(children=[
            html.Th(children='Nom de la ligne'), html.Th(children='Disponibilité'), html.Th(children='Régime de marche'),


        ])
    ] + content)


def TableDisponibilitéRégimeDeMarche(entité):
    content = [html.H4(children="Information sur les lignes d'engrais :")]

    tableLigneEngrais = []
    for ligneEngrais in entité.lignesEngrais.values():
        tableLigneEngrais.append(RowDisponibilitéRégime(ligneEngrais))

    content.append(html.Table(className='leave-space', children=[
        html.Th(children='Nom de la ligne'), html.Th(children='Disponibilité'), html.Th(children='Régime de marche'),
    ] + tableLigneEngrais))

    for atelier in entité.ateliers.values():
        content.append(html.H4(children='Information sur ' + atelier.nom))
        content.append(table(atelier))

    return html.Div(children=content)


def TableStocks(entité):
    content = [html.Tr(children=[
        html.Th(children='Nom du Stock'), html.Th(children='Capacité utilisée')
    ])]

    for stock in entité.stocks.values():
        content.append(RowCapacité(stock))

    return html.Div(children=[
        html.H4(children='Information Stock'),
        html.Table(className='leave-space', children=content)
    ])


def TableStocksCommun():
    content = [html.Tr(children=[
        html.Th(children='Nom du Stock'), html.Th(children='Capacité utilisée')
    ])]

    for stock in Jorf.stocksCommun.values():
        content.append(RowCapacité(stock))

    return html.Div(children=[
        html.H4(children='Information sur les Stocks communs :'),
        html.Table(id='table-stocks-commun', className='leave-space', children=content)
    ])


def TableCarnetCommande(entité):
    content = [html.Tr(children=[
        html.Th(children=label) for label in ["Engrais", "Ligne d'engrais", "Quantité", "Temps de lancement"]
    ])]

    for i in range(20):
        content.append(RowCarnetCommande(index=str(i), entité=entité))

    content.append(
        html.Tr(children=[
            html.Img(id='table-carnet-plus-' + entité.nom, src=Icons.Plus, alt='', height='40', width='40', n_clicks=1)
        ])
    )

    return html.Div(children=[
        html.H4(children="Carnet de commandes :"),
        html.Table(className='leave-space', children=content)
    ])


def TableEchange(entité, fournisseur):
    content = [html.Tr(children=[
        html.Th(children=label) for label in ['Produit', 'Date échange', 'Temps', 'Quantité', 'Débit']
    ])]

    for i in range(10):
        content.append(RowEchange(index=str(i), entité=entité, fournisseur=fournisseur))

    content.append(
        html.Tr(children=[
            html.Img(id='table-echange-plus-' + entité + fournisseur, src=Icons.Plus,
                     alt='', height='40', width='40', n_clicks=1)
        ])
    )

    return html.Div(children=[
        html.H4(children="Echange {0} / {1} (Avec {1} comme fournisseur):".format(entité, fournisseur)),
        html.Table(className='leave-space', children=content)
    ])


def TableExportMP34():
    content = [html.Tr(children=[
        html.Th(children=label) for label in ['Date échange', 'Temps', 'Quantité', 'Débit']
    ])]

    for i in range(10):
        content.append(RowExportMP34(index=str(i)))

    content.append(
        html.Tr(children=[
            html.Img(id='table-export-plus', src=Icons.Plus,
                     alt='', height='40', width='40', n_clicks=1)
        ])
    )

    return html.Div(children=[
        html.H4(children="Export Acide Phosphorique 54% MP34):"),
        html.Table(className='leave-space', children=content)
    ])


def TableMaintenance():
    content = [
        html.Tr(children=[
           html.Th(children='Ligne de production'), html.Th(children='Date de début'), html.Th(children='Date de fin'),
            html.Th(children='Périodicité')
        ])
    ]

    for i in range(20):
        content.append(RowMaintenance(str(i)))

    content.append(
        html.Tr(children=[
            html.Img(id='table-maintenance-plus', src=Icons.Plus,
                     alt='', height='40', width='40', n_clicks=1)
        ])
    )

    return html.Div(children=[
        html.H4(children="Emploi de Maintenance des lignes de production :"),

        html.Table(className='leave-space', children=content)
    ])


def TableChangementRégDeMarche():
    content = [
        html.Tr(children=[
            html.Th(children='Ligne de production'), html.Th(children='Date de changement du régime'),
            html.Th(children='Nouveau régime')
        ])
    ]

    for i in range(20):
        content.append(RowChangementRégMarche(str(i)))

    content.append(
        html.Tr(children=[
            html.Img(id='table-changement-reg-plus', src=Icons.Plus,
                     alt='', height='40', width='40', n_clicks=1)
        ])
    )

    return html.Div(children=[
        html.H4(children="Emploi de changement de régime de marche :"),

        html.Table(className='leave-space', children=content)
    ])