from DataAndInstantiation import Instanciation


Jorf = Instanciation.Jorf


def gantStock(nom):
    liste = []

    # for i in extractionStock(nom):
    for i in Jorf.getStock(nomStock=nom).capacitéUtilisé:
        if i / Jorf.getStock(nom).capacitéMax < Jorf.pourcentageRupture:
            liste.append(1)
            continue
        if i / Jorf.getStock(nom).capacitéMax > Jorf.pourcentageSaturation:
            liste.append(2)
            continue
        else:
            liste.append(0)

    return liste


def updateStateStocks():
    for entité in Jorf.entités.values():
        for stock in entité.stocks.values():
            try:
                stock.states = gantStock(stock.nom)
            except:
                pass
    return