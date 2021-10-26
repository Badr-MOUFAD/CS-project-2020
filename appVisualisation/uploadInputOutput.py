import dash

import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State

from Components import navigate

from acceuil import app

from DataAndInstantiation import Instanciation


Jorf = Instanciation.Jorf
count = 0

layout = html.Div(children=[
    html.H4(children='Importer fichier input :'),
    navigate.UploadField(id='upload-input'),

    html.H4(children='Importer fichier output :'),
    navigate.UploadField(id='upload-output'),

    html.Hr(),

    # dcc.Loading(children=navigate.Button(link='/visualisation-output-evolution-stocks',
    #                 label='Commencer la visualisation', id='commencer-visualisation', style={'display': 'none'}, n_clicks=0))

    dcc.Loading(id='commencer-visualisation', children=[

    ])
])


for label in ["output", "input"]:
    @app.callback(
        Output(component_id='upload-' + label, component_property='children'),
        [Input(component_id='upload-' + label, component_property='filename')]
    )
    def showFileName(fileName):
        if fileName is None:
            raise dash.exceptions.PreventUpdate

        return ['Document ', html.A(children=fileName), ' importé.']


@app.callback(
    Output(component_id='commencer-visualisation', component_property='children'),

    [Input(component_id='commencer-visualisation', component_property='n_clicks'),
     Input(component_id='upload-input', component_property='filename'),
     Input(component_id='upload-output', component_property='filename')]
)
def CommencerVisualisation(click, fileInput, fileOutput):
    global count

    if fileInput is None or fileOutput is None:
        raise dash.exceptions.PreventUpdate

    if count == 0:
        # try:
        #     count += 1
        #     from extractionExcel.fonctions import uploadDataFromExcels
        #
        #     uploadDataFromExcels(pathInput='C:/Users/HP/Desktop/' + fileInput, pathOutput='C:/Users/HP/Desktop/' + fileOutput)
        #
        #     return navigate.Button(link='/visualisation-output-evolution-stocks',
        #         label='Commencer la visualisation', n_clicks=0)
        # except:
        #     count -= 1
        #
        #     return 'Error.\nVeuillez réessayer.'

        from extractionExcel.fonctions import uploadDataFromExcels
        uploadDataFromExcels(pathInput='C:/Users/HP/Desktop/' + fileInput, pathOutput='C:/Users/HP/Desktop/' + fileOutput)


    return navigate.Button(link='/visualisation-output-evolution-stocks',
                label='Commencer la visualisation', n_clicks=0)
