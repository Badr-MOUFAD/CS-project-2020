import dash_core_components as dcc

import chart_studio.plotly
import plotly.figure_factory as ff

from DataAndInstantiation import Instanciation

Jorf = Instanciation.Jorf


def GraphEvolutionStock(nomStock, interval=None):
    if nomStock is None or nomStock == '':
        return dcc.Graph()

    if interval is None:
        interval = [Jorf.timeLine[0], Jorf.timeLine[len(Jorf.timeLine) - 1]]

    evolution = []
    timeLine = []

    startDateIndex, endDateIndex = Jorf.timeLine.index(interval[0]), Jorf.timeLine.index(interval[1])

    timeLine = Jorf.timeLine[startDateIndex: endDateIndex + 1]
    evolution = Jorf.getStock(nomStock).capacitéUtilisé[startDateIndex: endDateIndex + 1]

    graph = dcc.Graph(figure=dict(
        data=[
            dict(
               x=timeLine,
               y=evolution,
               name="Evolution",
               marker=dict(color='rgb(32, 121, 238)')
            ),
            dict(
                x=timeLine,
                y=[Jorf.getStock(nomStock).capacitéMax * Jorf.pourcentageRupture for t in timeLine],
                name="Seuil de rupture",
                marker=dict(color='rgb(251, 255, 28)')
            ),
            dict(
                x=timeLine,
                y=[Jorf.getStock(nomStock).capacitéMax * Jorf.pourcentageSaturation for t in timeLine],
                name="Seuil de saturation",
                marker=dict(color='rgb(221, 28, 28)')
            )
        ],
        layout=dict(
            title=nomStock,
            showlegend=True,
            yaxis=dict(title='unité Tonne')
        )
    ))

    return graph


def FigureGanttStock(nomEntité):
    df = []

    for stock in Jorf[nomEntité].stocks.values():
        df += stock.createStateForGantt()

    colors = dict(Normal='rgb(67, 221, 28)',
                  Rupture='rgb(255, 55, 55)',
                  Saturation='rgb(255, 251, 43)')

    figure = ff.create_gantt(df, colors=colors, index_col='Ressource', title='Gantt ' + nomEntité,
                          show_colorbar=True, bar_width=0.1, showgrid_x=True, showgrid_y=True, group_tasks=True)

    return figure


def FigureGanttLignesProduction(nomEntité):
    df = []

    for ligne in Jorf[nomEntité].getAllLignesDeProduction():
        df += ligne.createStateForGantt()

    colors = dict(Normal='rgb(67, 221, 28)',
                  Arret='rgb(255, 55, 55)',
                  Maintenance='rgb(255, 251, 43)')

    figure = ff.create_gantt(df, colors=colors, index_col='Ressource', title='Gantt ' + nomEntité,
                             show_colorbar=True, bar_width=0.1, showgrid_x=True, showgrid_y=True, group_tasks=True)

    return figure
