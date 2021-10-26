import dash
import dash_html_components as html
import dash_core_components as dcc
from dash_daq import BooleanSwitch, NumericInput

from Components import Icons
from DataAndInstantiation import Instanciation


def NavigateButton(link, direction, id=None):
    if direction == 'next' or direction == 'double-next':
        icon = Icons.NextPage if direction == 'next' else Icons.DoubleNextPage
        text = 'Suivant' if direction == 'next' else 'Entité suivante'

        navButton = html.Div(id=id, style={'margin-left': '100px', 'display': 'flex', 'align-items': 'center'}, children=[
                dcc.Link(className='side-bar', href=link, children=text),
                dcc.Link(className='side-bar', href=link, children=html.Img(src=icon, alt='', height='40', width='40')),
        ])

        return navButton

    elif direction == 'previous' or direction == 'double-previous':
        icon = Icons.PreviousPage if direction == 'previous' else Icons.DoublePreviousPage
        text = 'Précédent' if direction == 'previous' else 'Entité précédente'

        navButton = html.Div(id=id, style={'margin-right': '100px', 'display': 'flex', 'align-items': 'center'}, children=[
            dcc.Link(className='side-bar', href=link,
                     children=html.Img(src=icon, alt='', height='40', width='40')),
            dcc.Link(className='side-bar', href=link, children=text)
        ])

        return navButton

    return


def SliderParametrage(currentEntité, currentProcédure):
    procédure = ['Information ligne', 'Carnet commande', 'Stocks', 'Echange']

    silderEntité = dcc.Slider(min=0, max=9, disabled=True, value=currentEntité,
                         marks={i+1: {'label': Instanciation.allEntités[i]} for i in range(8)})

    silderProcédure = dcc.Slider(min=0, max=5, disabled=True, value=currentProcédure,
                                 marks={i+1: {'label': procédure[i]} for i in range(4)})

    component = html.Fieldset(#style={'margin-bottom': '40px', 'border': '1px solid rgb(128, 128, 128)', 'border-radius': '5px', 'padding': '30px'},
                      children=[
        html.Legend(children='Etape actuelle :'),
        html.Div(style={'margin-bottom': '20px'}, children=silderEntité),
        html.Hr(),
        html.Div(style={'margin-bottom': '20px'}, children=silderProcédure)
    ])

    return component


def SliderAutre(currentProcédure):
    procédure = ['Stocks commun', 'Emploi maintenance', 'Emploi régime de marche']

    silder = dcc.Slider(min=0, max=4, marks={i+1: {'label': procédure[i]} for i in range(len(procédure))},
                        value=currentProcédure, disabled=True)

    component = html.Fieldset(
        style={'margin-bottom': '40px', 'border': '1px solid rgb(128, 128, 128)', 'border-radius': '5px',
               'padding': '30px'},
        children=[
            html.Legend(children='Etape actuelle :'),
            html.Div(style={'margin-bottom': '20px'}, children=silder),
        ])

    return component


def SideBarButton(label, link, active, id=None):
    content = dcc.Link(className='side-bar', href=link, children=label)
    className = 'side-bar'

    if active:
        className = 'side-bar-active'
        content = label

    if id is None:
        return html.Button(className=className, children=content)
    else:
        return html.Button(id=id, className=className, children=content)


def Button(link, label, id=None, **kwargs):
    if id is None:
        return html.Button(**kwargs, children=[
            dcc.Link(className='side-bar', href=link, children=label)
        ])

    else:
        return html.Button(**kwargs, id=id, children=[
            dcc.Link(className='side-bar', href=link, children=label)
        ])


def IconButton(icon, label, link='', id=None):

    navButton = html.Div(id=id, style={'margin-left': '100px', 'display': 'flex', 'align-items': 'center'}, children=[
        dcc.Link(className='side-bar', href=link, children=label),
        dcc.Link(className='side-bar', href=link, children=html.Img(src=icon, alt='', height='40', width='40')),
    ])

    return navButton


def UploadField(id, text='Glisser ou Sélectioner le fichier'):
    style = {
            'width': '90%',
            'height': '100px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'font-style': 'italic',
            'margin': '10px',
            'cursor': 'pointer'
        }

    return dcc.Upload(id=id, style=style, children=html.A(children=text))
