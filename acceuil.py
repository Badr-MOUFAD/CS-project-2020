import dash
import dash_html_components as html
import dash_core_components as dcc

from Components import navigate, Icons

from DataAndInstantiation import Instanciation


Jorf = Instanciation.Jorf

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets, suppress_callback_exceptions=True)


layout = html.Div(id='document', style={}, children=[

    dcc.Location(id='url', refresh=False),

    html.Div(id='app-bar', className='app-bar', children=[
        html.H3(style={'margin-left': '10px'}, children='Acceuil')
    ]),

    html.Div(className='row', children=[

        html.Div(id='app-side-bar', className='three columns', children=[
            # html.Button(className='side-bar', children=[
            #     dcc.Link(className='side-bar', children=['Générer fichier Input'], href='/generation-input')]),
            # html.Button(className='side-bar', children=[
            #     dcc.Link(className='side-bar', children=['Visualiser fichier Output'], href='/visualisation-output')])
            navigate.SideBarButton(label='Générer fichier Input', link='/generation-input', active=False),
            navigate.SideBarButton(label='Visualiser fichier Output', link='/visualisation-output', active=False)
        ]),

        html.Div(className='nine columns', id='scene', children=[

        ])
    ]),

    *[dcc.Store(id='store-DispoLigneEngrais-' + entité, storage_type='memory') for entité in Jorf.entités]
])
