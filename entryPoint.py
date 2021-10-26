import dash_html_components as html

from dash.dependencies import Input, Output

from appInput import dateDuration
from acceuil import app, layout
from appInput import parametrageMP34, parametrageJFD, parametrageJFF, parametrageJFO, \
    parametrageJFQ, parametrageJFT, parametrageIMACID, parametragePMP, autreParametre
from appVisualisation import uploadInputOutput, evolutionStocks, ganttStock, ganttLignes

from Components import navigate
from Components.sideBars import mainSideBarVisActive, mainSideBarGenActive, \
    mainSideBar, parametrageSideBarActive, autreSideBarActive, sideBarVisualisation

app.layout = layout



@app.callback(
    [Output(component_id='scene', component_property='children'), Output(component_id='app-bar', component_property='children'),
    Output(component_id='app-side-bar', component_property='children')],
    [Input(component_id='url', component_property='pathname')]
)
def mainPages(pathname):
    if pathname == '/generation-input':
        return dateDuration.layout, html.H3(style={'margin-left': '10px'}, children='Acceuil'), mainSideBarGenActive

    elif pathname == '/visualisation-output':
        return uploadInputOutput.layout, html.H3(style={'margin-left': '10px'}, children='Acceuil'), mainSideBarVisActive

    ### visualisation :

    elif pathname == '/visualisation-output-evolution-stocks':
        return evolutionStocks.layoutPage, html.H3(style={'margin-left': '10px'}, children='Visualisation'), sideBarVisualisation(True, False, False)
    elif pathname == '/visualisation-output-gantt-stocks':
        return ganttStock.layoutPage, html.H3(style={'margin-left': '10px'}, children='Visualisation'), sideBarVisualisation(False, True, False)
    elif pathname == '/visualisation-output-gantt-lignes-production':
        return ganttLignes.layoutPage, html.H3(style={'margin-left': '10px'}, children='Visualisation'), sideBarVisualisation(False, False, True)
    ### parametrage :

    elif pathname == '/parametrage-MP34-page1':
        return parametrageMP34.layoutPage1, html.H3(style={'margin-left': '10px'}, children='Générer fichier Input'), parametrageSideBarActive
    elif pathname == '/parametrage-MP34-page2':
        return parametrageMP34.layoutPage2, html.H3(style={'margin-left': '10px'}, children='Générer fichier Input'), parametrageSideBarActive
    elif pathname == '/parametrage-MP34-page3':
        return parametrageMP34.layoutPage3, html.H3(style={'margin-left': '10px'}, children='Générer fichier Input'), parametrageSideBarActive

    elif pathname == '/parametrage-MP34-page4':
        return parametrageMP34.layoutPage4_[0], html.H3(style={'margin-left': '10px'}, children='Générer fichier Input'), parametrageSideBarActive
    elif pathname == '/parametrage-MP34-page5':
        return parametrageMP34.layoutPage4_[1], html.H3(style={'margin-left': '10px'}, children='Générer fichier Input'), parametrageSideBarActive
    elif pathname == '/parametrage-MP34-page6':
        return parametrageMP34.layoutPage4_[2], html.H3(style={'margin-left': '10px'}, children='Générer fichier Input'), parametrageSideBarActive
    elif pathname == '/parametrage-MP34-page7':
        return parametrageMP34.layoutPage4_[3], html.H3(style={'margin-left': '10px'}, children='Générer fichier Input'), parametrageSideBarActive

    ###

    elif pathname == '/parametrage-JFD-page1':
        return parametrageJFD.layoutPage1, html.H3(style={'margin-left': '10px'}, children='Générer fichier Input'), parametrageSideBarActive
    elif pathname == '/parametrage-JFD-page2':
        return parametrageJFD.layoutPage2, html.H3(style={'margin-left': '10px'}, children='Générer fichier Input'), parametrageSideBarActive
    elif pathname == '/parametrage-JFD-page3':
        return parametrageJFD.layoutPage3, html.H3(style={'margin-left': '10px'}, children='Générer fichier Input'), parametrageSideBarActive

    elif pathname == '/parametrage-JFD-page4':
        return parametrageJFD.layoutPage4_[0], html.H3(style={'margin-left': '10px'}, children='Générer fichier Input'), parametrageSideBarActive
    elif pathname == '/parametrage-JFD-page5':
        return parametrageJFD.layoutPage4_[1], html.H3(style={'margin-left': '10px'}, children='Générer fichier Input'), parametrageSideBarActive
    elif pathname == '/parametrage-JFD-page6':
        return parametrageJFD.layoutPage4_[2], html.H3(style={'margin-left': '10px'}, children='Générer fichier Input'), parametrageSideBarActive
    elif pathname == '/parametrage-JFD-page7':
        return parametrageJFD.layoutPage4_[3], html.H3(style={'margin-left': '10px'}, children='Générer fichier Input'), parametrageSideBarActive

    ###

    elif pathname == '/parametrage-JFF-page1':
        return parametrageJFF.layoutPage1, html.H3(style={'margin-left': '10px'}, children='Générer fichier Input'), parametrageSideBarActive
    elif pathname == '/parametrage-JFF-page2':
        return parametrageJFF.layoutPage2, html.H3(style={'margin-left': '10px'}, children='Générer fichier Input'), parametrageSideBarActive
    elif pathname == '/parametrage-JFF-page3':
        return parametrageJFF.layoutPage3, html.H3(style={'margin-left': '10px'}, children='Générer fichier Input'), parametrageSideBarActive

    elif pathname == '/parametrage-JFF-page4':
        return parametrageJFF.layoutPage4_[0], html.H3(style={'margin-left': '10px'}, children='Générer fichier Input'), parametrageSideBarActive
    elif pathname == '/parametrage-JFF-page5':
        return parametrageJFF.layoutPage4_[1], html.H3(style={'margin-left': '10px'}, children='Générer fichier Input'), parametrageSideBarActive
    elif pathname == '/parametrage-JFF-page6':
        return parametrageJFF.layoutPage4_[2], html.H3(style={'margin-left': '10px'}, children='Générer fichier Input'), parametrageSideBarActive
    elif pathname == '/parametrage-JFF-page7':
        return parametrageJFF.layoutPage4_[3], html.H3(style={'margin-left': '10px'}, children='Générer fichier Input'), parametrageSideBarActive

    ###

    elif pathname == '/parametrage-JFO-page1':
        return parametrageJFO.layoutPage1, html.H3(style={'margin-left': '10px'}, children='Générer fichier Input'), parametrageSideBarActive
    elif pathname == '/parametrage-JFO-page2':
        return parametrageJFO.layoutPage2, html.H3(style={'margin-left': '10px'}, children='Générer fichier Input'), parametrageSideBarActive
    elif pathname == '/parametrage-JFO-page3':
        return parametrageJFO.layoutPage3, html.H3(style={'margin-left': '10px'}, children='Générer fichier Input'), parametrageSideBarActive

    elif pathname == '/parametrage-JFO-page4':
        return parametrageJFO.layoutPage4_[0], html.H3(style={'margin-left': '10px'}, children='Générer fichier Input'), parametrageSideBarActive
    elif pathname == '/parametrage-JFO-page5':
        return parametrageJFO.layoutPage4_[1], html.H3(style={'margin-left': '10px'}, children='Générer fichier Input'), parametrageSideBarActive
    elif pathname == '/parametrage-JFO-page6':
        return parametrageJFO.layoutPage4_[2], html.H3(style={'margin-left': '10px'}, children='Générer fichier Input'), parametrageSideBarActive
    elif pathname == '/parametrage-JFO-page7':
        return parametrageJFO.layoutPage4_[3], html.H3(style={'margin-left': '10px'}, children='Générer fichier Input'), parametrageSideBarActive

    ###

    elif pathname == '/parametrage-JFQ-page1':
        return parametrageJFQ.layoutPage1, html.H3(style={'margin-left': '10px'}, children='Générer fichier Input'), parametrageSideBarActive
    elif pathname == '/parametrage-JFQ-page2':
        return parametrageJFQ.layoutPage2, html.H3(style={'margin-left': '10px'}, children='Générer fichier Input'), parametrageSideBarActive
    elif pathname == '/parametrage-JFQ-page3':
        return parametrageJFQ.layoutPage3, html.H3(style={'margin-left': '10px'}, children='Générer fichier Input'), parametrageSideBarActive

    elif pathname == '/parametrage-JFQ-page4':
        return parametrageJFQ.layoutPage4_[0], html.H3(style={'margin-left': '10px'}, children='Générer fichier Input'), parametrageSideBarActive
    elif pathname == '/parametrage-JFQ-page5':
        return parametrageJFQ.layoutPage4_[1], html.H3(style={'margin-left': '10px'}, children='Générer fichier Input'), parametrageSideBarActive
    elif pathname == '/parametrage-JFQ-page6':
        return parametrageJFQ.layoutPage4_[2], html.H3(style={'margin-left': '10px'}, children='Générer fichier Input'), parametrageSideBarActive
    elif pathname == '/parametrage-JFQ-page7':
        return parametrageJFQ.layoutPage4_[3], html.H3(style={'margin-left': '10px'}, children='Générer fichier Input'), parametrageSideBarActive

    ###

    elif pathname == '/parametrage-JFT-page1':
        return parametrageJFT.layoutPage1, html.H3(style={'margin-left': '10px'}, children='Générer fichier Input'), parametrageSideBarActive
    elif pathname == '/parametrage-JFT-page2':
        return parametrageJFT.layoutPage2, html.H3(style={'margin-left': '10px'}, children='Générer fichier Input'), parametrageSideBarActive
    elif pathname == '/parametrage-JFT-page3':
        return parametrageJFT.layoutPage3, html.H3(style={'margin-left': '10px'}, children='Générer fichier Input'), parametrageSideBarActive

    elif pathname == '/parametrage-JFT-page4':
        return parametrageJFT.layoutPage4_[0], html.H3(style={'margin-left': '10px'}, children='Générer fichier Input'), parametrageSideBarActive
    elif pathname == '/parametrage-JFT-page5':
        return parametrageJFT.layoutPage4_[1], html.H3(style={'margin-left': '10px'}, children='Générer fichier Input'), parametrageSideBarActive
    elif pathname == '/parametrage-JFT-page6':
        return parametrageJFT.layoutPage4_[2], html.H3(style={'margin-left': '10px'}, children='Générer fichier Input'), parametrageSideBarActive
    elif pathname == '/parametrage-JFT-page7':
        return parametrageJFT.layoutPage4_[3], html.H3(style={'margin-left': '10px'}, children='Générer fichier Input'), parametrageSideBarActive

    ###

    elif pathname == '/parametrage-IMACID-page1':
        return parametrageIMACID.layoutPage1, html.H3(style={'margin-left': '10px'}, children='Générer fichier Input'), parametrageSideBarActive
    elif pathname == '/parametrage-IMACID-page2':
        return parametrageIMACID.layoutPage2, html.H3(style={'margin-left': '10px'}, children='Générer fichier Input'), parametrageSideBarActive
    elif pathname == '/parametrage-IMACID-page3':
        return parametrageIMACID.layoutPage3, html.H3(style={'margin-left': '10px'}, children='Générer fichier Input'), parametrageSideBarActive

    elif pathname == '/parametrage-IMACID-page4':
        return parametrageIMACID.layoutPage4_[0], html.H3(style={'margin-left': '10px'}, children='Générer fichier Input'), parametrageSideBarActive
    elif pathname == '/parametrage-IMACID-page5':
        return parametrageIMACID.layoutPage4_[1], html.H3(style={'margin-left': '10px'}, children='Générer fichier Input'), parametrageSideBarActive
    elif pathname == '/parametrage-IMACID-page6':
        return parametrageIMACID.layoutPage4_[2], html.H3(style={'margin-left': '10px'}, children='Générer fichier Input'), parametrageSideBarActive
    elif pathname == '/parametrage-IMACID-page7':
        return parametrageIMACID.layoutPage4_[3], html.H3(style={'margin-left': '10px'}, children='Générer fichier Input'), parametrageSideBarActive

    ###

    elif pathname == '/parametrage-PMP-page1':
        return parametragePMP.layoutPage1, html.H3(style={'margin-left': '10px'}, children='Générer fichier Input'), parametrageSideBarActive
    elif pathname == '/parametrage-PMP-page2':
        return parametragePMP.layoutPage2, html.H3(style={'margin-left': '10px'}, children='Générer fichier Input'), parametrageSideBarActive
    elif pathname == '/parametrage-PMP-page3':
        return parametragePMP.layoutPage3, html.H3(style={'margin-left': '10px'}, children='Générer fichier Input'), parametrageSideBarActive

    elif pathname == '/parametrage-PMP-page4':
        return parametragePMP.layoutPage4_[0], html.H3(style={'margin-left': '10px'}, children='Générer fichier Input'), parametrageSideBarActive
    elif pathname == '/parametrage-PMP-page5':
        return parametragePMP.layoutPage4_[1], html.H3(style={'margin-left': '10px'}, children='Générer fichier Input'), parametrageSideBarActive
    elif pathname == '/parametrage-PMP-page6':
        return parametragePMP.layoutPage4_[2], html.H3(style={'margin-left': '10px'}, children='Générer fichier Input'), parametrageSideBarActive
    elif pathname == '/parametrage-PMP-page7':
        return parametragePMP.layoutPage4_[3], html.H3(style={'margin-left': '10px'}, children='Générer fichier Input'), parametrageSideBarActive

    ###

    ### autre parametre:

    elif pathname == '/autre-parametre-page1':
        return autreParametre.layoutPage1, html.H3(style={'margin-left': '10px'}, children='Générer fichier Input'), autreSideBarActive
    elif pathname == '/autre-parametre-page2':
        return autreParametre.layoutPage2, html.H3(style={'margin-left': '10px'}, children='Générer fichier Input'), autreSideBarActive
    elif pathname == '/autre-parametre-page3':
        return autreParametre.layoutPage3, html.H3(style={'margin-left': '10px'}, children='Générer fichier Input'), autreSideBarActive
    elif pathname == '/autre-parametre-page4':
        return autreParametre.layoutPage4, html.H3(style={'margin-left': '10px'}, children='Générer fichier Input'), autreSideBarActive
    ###

    else:
        return 'scene is working', html.H3(style={'margin-left': '10px'}, children='Acceuil'), mainSideBar


if __name__ == '__main__':
    app.run_server(debug=True)
