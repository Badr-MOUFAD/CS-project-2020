from DataAndInstantiation import ClassElémentaire as C1
from DataAndInstantiation import ClassSecondaire as C2
from DataAndInstantiation import ClassTertiaire as C3

import datetime as date

# création du complexe Jorf :
Jorf = C3.Complexe(nom="Jorf")
Jorf.date = date.datetime.now()
Jorf.durée = 1

    # entité
allEntités = ['MP34', "JFD", "JFF", "JFO", "JFQ", "JFT", "IMACID", "PMP"]
for entité in allEntités:
    Jorf.entités[entité] = C3.Entité(entité)

    # stocks commun :
for stock in [['DAP JFC', 150000], ['MAP JFC', 150000], ['TSP JFC', 150000], ['ASP JFC', 150000], ['NPS JFC', 150000], ['NPK JFC', 150000]]:
    Jorf.stocksCommun[stock[0]] = C1.Stock(nom=stock[0], capacitéMax=stock[1])

# liste des engrais
###

# création des entités
allStoks = [[['Stock_Soufre_MP34', 30000], ['Fosse soufre liquide 1', 258], ['Fosse soufre liquide 2', 258], ['Fosse soufre liquide 3', 258], ['Stock_Sulfurique_MP34', 73000], ['Stock_Pulpe_MP34', 1000000], ['Stock_Phosphorique 29%_MP34', 18947.74624], ['Stock_Phosphorique 54%_MP34', 49659.627744000005], ['Stock_Phosphorique 29%_MP34_Ligne 107A', 890.88], ['Stock_Phosphorique 54%_MP34_Ligne 107A', 2151.3599999999997], ['Stock_Ammoniac_MP34_Ligne 107', 1200], ['H2SO4 engrais L1', 543.72], ['Stock_Fuel_MP34_Ligne 107A', 500], ['Enrobant L1', 500], ['KCL L1&2&3', 50], ['Stock_Phosphorique 29%_MP34_Ligne 107B&C', 1484.8], ['Stock_Phosphorique 54%_MP34_Ligne 107B&C', 3585.6], ['Stock_Sulfurique_MP34_Ligne 07&107', 1103.7516], ['Stock_Fuel_MP34_Ligne 107B&C', 1000], ['Enrobant L2&3', 1000], ['Stock capacitaire 29 vers E', 371.2], ['Stock capacitaire 29 vers 54', 896.4], ['Stock capacitaire 29 vers exterieur', 1087.44], ['Stock_Phosphorique 29%_MP34_Ligne 07', 1483.75329024], ['Stock_Phosphorique 54%_MP34_Ligne 07', 7166.144662560001], ['Stock_Ammoniac_MP34_Ligne 07', 4000], ['H2SO4 engrais L4&5&6&7', 16.311600000000002], ['Stock_Fuel_MP34_Ligne 07', 50], ['Enrobant L4&5&6&7', 50], ['DAP', 150000], ['MAP', 150000], ['TSP', 150000], ['ASP', 150000], ['NPS', 150000], ['NPK', 150000], ['Stock capacitaire H2SO4 vers E', 4000], ['Stock capacitaire H2SO4 vers ACP', 4000], ['Stock capacitaire H2SO4 vers exterieur', 50]],
[['Stock_Soufre_JFD', 40000], ['Stock_Sulfurique_JFD', 15000], ['Stock_Phosphorique 29%_JFD', 20000], ['Stock_Phosphorique 54%_JFD', 50000], ['Stcok_Ammoniac_JFD', 50000], ['Stock Fioul JFD', None], ['Stock Enrobant JFD', None]],
[['Stock_Soufre_JFF', 40000], ['Stock_Sulfurique_JFF', 15000], ['Stock_Phosphorique 29%_JFF', 20000], ['Stock_Phosphorique 54%_JFF', 50000], ['Stcok_Ammoniac_JFF', 50000], ['Stock Fioul JFF', None], ['Stock Enrobant JFF', None]],
[['Stock_Soufre_JFO', 40000], ['Stock_Sulfurique_JFO', 15000], ['Stock_Phosphorique 29%_JFO', 20000], ['Stock_Phosphorique 54%_JFO', 50000], ['Stcok_Ammoniac_JFO', 50000], ['Stock Fioul JFO', None], ['Stock Enrobant JFO', None]],
[['Stock_Soufre_JFQ', 40000], ['Stock_Sulfurique_JFQ', 15000], ['Stock_Phosphorique 29%_JFQ', 20000], ['Stock_Phosphorique 54%_JFQ', 50000], ['Stcok_Ammoniac_JFQ', 50000], ['Stock Fioul JFQ', None], ['Stock Enrobant JFQ', None]],
[['Stock_Soufre_JFT', 40000], ['Stock_Sulfurique_JFT', 15000], ['Stock_Phosphorique 29%_JFT', 20000], ['Stock_Phosphorique 54%_JFT', 50000], ['Stcok_Ammoniac_JFT', 50000], ['Stock Fioul JFT', None], ['Stock Enrobant JFT', None]],
[['Stock_Soufre_IMACID', 40000], ['Stock_Sulfurique_IMACID', 15000], ['Stock_Phosphorique 29%_IMACID', 20000], ['Stock_Phosphorique 54%_IMACID', 50000]],
[['Stock_Soufre_PMP', 40000], ['Stock_Sulfurique_PMP', 15000], ['Stock_Phosphorique 29%_PMP', 20000], ['Stock_Phosphorique 54%_PMP', 50000]]]
    # stock  de chaque entité
count = 0
for entité in Jorf.entités.values():
    for stock in allStoks[count]:
        entité.stocks[stock[0]] = C1.Stock(nom=stock[0], capacitéMax=stock[1])

    count += 1

    # atelier pour chaque entité:
allAtlier = ['Atelier_Sulfurique_MP34', 'Atelier_Phosphorique 29%_MP34', 'Atelier_Phosphorique 54%_MP34', 'Atelier_Sulfurique_JFD', 'Atelier_Phosphorique 29%_JFD', 'Atelier_Phosphorique 54%_JFD', 'Atelier_Sulfurique_JFF', 'Atelier_Phosphorique 29%_JFF', 'Atelier_Phosphorique 54%_JFF', 'Atelier_Sulfurique_JFO', 'Atelier_Phosphorique 29%_JFO', 'Atelier_Phosphorique 54%_JFO', 'Atelier_Sulfurique_JFQ', 'Atelier_Phosphorique 29%_JFQ', 'Atelier_Phosphorique 54%_JFQ', 'Atelier_Sulfurique_JFT', 'Atelier_Phosphorique 29%_JFT', 'Atelier_Phosphorique 54%_JFT', 'Atelier_Sulfurique_IMACID', 'Atelier_Phosphorique 29%_IMACID', 'Atelier_Phosphorique 54%_IMACID', 'Atelier_Sulfurique_PMP', 'Atelier_Phosphorique 29%_PMP', 'Atelier_Phosphorique 54%_PMP']
count = 0
for entité in Jorf.entités.values():
    for atelier in allAtlier[3 * count: 3 * (count+1)]:
        entité.ateliers[atelier] = C2.Atelier(nom=atelier)

    count += 1

    # ligne engrais pour chaque entité :
allLignesEngrais = [['Ligne engrais 107 A', "WCF admission Ligne d'engrais 1", 1], ['Ligne engrais 107 B', "WCF admission Ligne d'engrais 2", 2], ['Ligne engrais 107 C', "WCF admission Ligne d'engrais 3", 3], ['Ligne engrais 07 A', "WCF admission Ligne d'engrais 4", 4], ['Ligne engrais 07 B', "WCF admission Ligne d'engrais 5", 5], ['Ligne engrais 07 C', "WCF admission Ligne d'engrais 6", 6], ['Ligne engrais 07 D', "WCF admission Ligne d'engrais 7", 7], ["Ligne JFD d'engrais", "WCF admission Ligne d'engrais JFD", 1], ["Ligne JFF d'engrais 1", "WCF admission Ligne d'engrais JFF 1", 2], ["Ligne JFF d'engrais 2", "WCF admission Ligne d'engrais JFF 2", 3], ["Ligne JFO d'engrais", "WCF admission Ligne d'engrais JFO", 4], ["Ligne JFQ d'engrais", "WCF admission Ligne d'engrais JFQ", 5], ["Ligne JFT d'engrais", "WCF admission Ligne d'engrais JFT", 6]]

for ligneEngrais in allLignesEngrais[:7]:
    Jorf['MP34'].lignesEngrais[ligneEngrais[0]] = C2.LigneEngrais(nom=ligneEngrais[0], mappingMaintenance=ligneEngrais[1], mappingExcel=ligneEngrais[2])

for entité in Jorf.entités.values():
    if entité.nom != "MP34":
        for ligneEngrais in allLignesEngrais[7:]:
            if entité.nom in ligneEngrais[0]:
                entité.lignesEngrais[ligneEngrais[0]] = C2.LigneEngrais(nom=ligneEngrais[0], mappingMaintenance=ligneEngrais[1], mappingExcel=ligneEngrais[2])

        # ligne de production
lignesMP34 = [['Ligne sulfurique 1 (A)', 'WCF admission H2SO4 1'], ['Ligne sulfurique 2 (B)', 'WCF admission H2SO4 2'], ['Ligne sulfurique 3 (E)', 'WCF admission H2SO4 3'], ['Ligne sulfurique 4 (X)', 'WCF admission H2SO4 4'], ['Ligne sulfurique 5 (Y)', 'WCF admission H2SO4 5'], ['Ligne sulfurique 6 (Z)', 'WCF admission H2SO4 6'], ['Ligne phosphorique 29 1 (AB)', 'WCF admission H3PO4 29 1'], ['Ligne phosphorique 29 2 (CD)', 'WCF admission H3PO4 29 2'], ['Ligne phosphorique 29 3 (XY)', 'WCF admission H3PO4 29 3'], ['Ligne phosphorique 29 4 (Z)', 'WCF admission H3PO4 29 4'], ['Ligne phosphorique 29 5 (U)', 'WCF admission H3PO4 29 5'], ['Ligne phosphorique 29 6 (E)', 'WCF admission H3PO4 29 6'], ['Ligne phosphorique 54 1', 'WCF admission P2O5 1'], ['Ligne phosphorique 54 2', 'WCF admission P2O5 2'], ['Ligne phosphorique 54 3', 'WCF admission P2O5 3'], ['Ligne phosphorique 54 4', 'WCF admission P2O5 4'], ['Ligne phosphorique 54 5', 'WCF admission P2O5 5'], ['Ligne phosphorique 54 6', 'WCF admission P2O5 6'], ['Ligne phosphorique 54 7', 'WCF admission P2O5 7'], ['Ligne phosphorique 54 8', 'WCF admission P2O5 8'], ['Ligne phosphorique 54 9', 'WCF admission P2O5 9'], ['Ligne phosphorique 54 10', 'WCF admission P2O5 10'], ['Ligne phosphorique 54 11', 'WCF admission P2O5 11'], ['Ligne phosphorique 54 12', 'WCF admission P2O5 12'], ['Ligne phosphorique 54 13', 'WCF admission P2O5 13'], ['Ligne phosphorique 54 14', 'WCF admission P2O5 14'], ['Ligne phosphorique 54 15', 'WCF admission P2O5 15'], ['Ligne phosphorique 54 16', 'WCF admission P2O5 16'], ['Ligne phosphorique 54 17', 'WCF admission P2O5 17'], ['Ligne phosphorique 54 18', 'WCF admission P2O5 18'], ['Ligne phosphorique 54 19', 'WCF admission P2O5 19'], ['Ligne phosphorique 54 20', 'WCF admission P2O5 20']]
count = 0
for atelier in Jorf['MP34'].ateliers.values():
    for ligne in lignesMP34:
        if Jorf.ENCHAINEMENT_ATELIER[count] in ligne[0]:
            atelier.lignesDeProduction[ligne[0]] = C1.LigneDeProduction(nom=ligne[0], mappingMaintenance=ligne[1])

    count += 1

lignesProductionRestantes = [['Ligne sulfurique (JFD)', 'WCF admission H2SO4 JFD'], ['Ligne phosphorique 29 (JFD)', 'WCF admission H3PO4 29 JFD'], ['Ligne phosphorique 54 JFD (1)', 'WCF admission P2O5 JFD 1'], ['Ligne phosphorique 54 JFD (2)', 'WCF admission P2O5 JFD 2'], ['Ligne phosphorique 54 JFD (3)', 'WCF admission P2O5 JFD 3'], ['Ligne sulfurique (JFF)', 'WCF admission H2SO4 JFF'], ['Ligne phosphorique 29 (JFF)', 'WCF admission H3PO4 29 JFF'], ['Ligne phosphorique 54 JFF (1)', 'WCF admission P2O5 JFF 1'], ['Ligne phosphorique 54 JFF (2)', 'WCF admission P2O5 JFF 2'], ['Ligne phosphorique 54 JFF (3)', 'WCF admission P2O5 JFF 3'], ['Ligne sulfurique (JFO)', 'WCF admission H2SO4 JFO'], ['Ligne phosphorique 29 (JFO)', 'WCF admission H3PO4 29 JFO'], ['Ligne phosphorique 54 JFO (1)', 'WCF admission P2O5 JFO 1'], ['Ligne phosphorique 54 JFO (2)', 'WCF admission P2O5 JFO 2'], ['Ligne phosphorique 54 JFO (3)', 'WCF admission P2O5 JFO 3'], ['Ligne sulfurique (JFQ)', 'WCF admission H2SO4 JFQ'], ['Ligne phosphorique 29 (JFQ)', 'WCF admission H3PO4 29 JFQ'], ['Ligne phosphorique 54 JFQ (1)', 'WCF admission P2O5 JFQ 1'], ['Ligne phosphorique 54 JFQ (2)', 'WCF admission P2O5 JFQ 2'], ['Ligne phosphorique 54 JFQ (3)', 'WCF admission P2O5 JFQ 3'], ['Ligne sulfurique (JFT)', 'WCF admission H2SO4 JFT'], ['Ligne phosphorique 29 (JFT)', 'WCF admission H3PO4 29 JFT'], ['Ligne phosphorique 54 JFT (1)', 'WCF admission P2O5 JFT 1'], ['Ligne phosphorique 54 JFT (2)', 'WCF admission P2O5 JFT 2'], ['Ligne phosphorique 54 JFT (3)', 'WCF admission P2O5 JFT 3'], ['Ligne sulfurique (PMP)', 'WCF admission H2SO4 PMP'], ['Ligne phosphorique 29 (PMP)', 'WCF admission H3PO4 29 PMP'], ['Ligne phosphorique 54 PMP (1)', 'WCF admission P2O5 PMP 1'], ['Ligne phosphorique 54 PMP (2)', 'WCF admission P2O5 PMP 2'], ['Ligne phosphorique 54 PMP (3)', 'WCF admission P2O5 PMP 3'], ['Ligne sulfurique (IMACID)', 'WCF admission H2SO4 IMACID'], ['Ligne phosphorique 29 (IMACID)', 'WCF admission H3PO4 29 IMACID'], ['Ligne phosphorique 54 IMACID (1)', 'WCF admission P2O5 IMACID 1'], ['Ligne phosphorique 54 IMACID (2)', 'WCF admission P2O5 IMACID 2'], ['Ligne phosphorique 54 IMACID (3)', 'WCF admission P2O5 IMACID 3']]

for entité in Jorf.entités.values():
    count = 0
    if entité.nom != 'MP34':
        for atelier in entité.ateliers.values():
            for ligne in lignesProductionRestantes:
                if entité.nom in ligne[0] and Jorf.ENCHAINEMENT_ATELIER[count] in ligne[0]:
                    atelier.lignesDeProduction[ligne[0]] = C1.LigneDeProduction(nom=ligne[0], mappingMaintenance=ligne[1])

            count += 1

stocksAmontAval = [[['Stock_Soufre_MP34'], ['Stock_Sulfurique_MP34']],
[['Stock_Sulfurique_MP34', 'Stock_Pulpe_MP34'], ['Stock_Phosphorique 29%_MP34']],
[['Stock_Phosphorique 29%_MP34'], ['Stock_Phosphorique 54%_MP34']],
[['Stock_Soufre_JFD'], ['Stock_Sulfurique_JFD']],
[['Stock_Sulfurique_JFD', 'Stock_Pulpe_MP34'], ['Stock_Phosphorique 29%_JFD']],
[['Stock_Phosphorique 29%_JFD'], ['Stock_Phosphorique 54%_JFD']],
[['Stock_Soufre_JFF'], ['Stock_Sulfurique_JFF']],
[['Stock_Sulfurique_JFF', 'Stock_Pulpe_MP34'], ['Stock_Phosphorique 29%_JFF']],
[['Stock_Phosphorique 29%_JFF'], ['Stock_Phosphorique 54%_JFF']],
[['Stock_Soufre_JFO'], ['Stock_Sulfurique_JFO']],
[['Stock_Sulfurique_JFO', 'Stock_Pulpe_MP34'], ['Stock_Phosphorique 29%_JFO']],
[['Stock_Phosphorique 29%_JFO'], ['Stock_Phosphorique 54%_JFO']],
[['Stock_Soufre_JFQ'], ['Stock_Sulfurique_JFQ']],
[['Stock_Sulfurique_JFQ', 'Stock_Pulpe_MP34'], ['Stock_Phosphorique 29%_JFQ']],
[['Stock_Phosphorique 29%_JFQ'], ['Stock_Phosphorique 54%_JFQ']],
[['Stock_Soufre_JFT'], ['Stock_Sulfurique_JFT']],
[['Stock_Sulfurique_JFT', 'Stock_Pulpe_MP34'], ['Stock_Phosphorique 29%_JFT']],
[['Stock_Phosphorique 29%_JFT'], ['Stock_Phosphorique 54%_JFT']],
[['Stock_Soufre_IMACID'], ['Stock_Sulfurique_IMACID']],
[['Stock_Sulfurique_IMACID', 'Stock_Pulpe_MP34'], ['Stock_Phosphorique 29%_IMACID']],
[['Stock_Phosphorique 29%_IMACID'], ['Stock_Phosphorique 54%_IMACID']],
[['Stock_Soufre_PMP'], ['Stock_Sulfurique_PMP']],
[['Stock_Sulfurique_PMP', 'Stock_Pulpe_MP34'], ['Stock_Phosphorique 29%_PMP']],
[['Stock_Phosphorique 29%_PMP'], ['Stock_Phosphorique 54%_PMP']]]


for entité in Jorf.entités.values():
    count = 0
    for amontAval in stocksAmontAval[3 * count: 3 * (count+1)]:    # atelier fixe
        x = entité.getAtelier(Jorf.ENCHAINEMENT_ATELIER[count])

        for stockAmont in amontAval[0]:
            try:
                x.stocksAmont[stockAmont] = entité.stocks[stockAmont]
            except:
                x.stocksAmont[stockAmont] = Jorf['MP34'].stocks[stockAmont]

        for stockAval in amontAval[1]:
            try:
                x.stocksAval[stockAval] = entité.stocks[stockAval]
            except:
                x.stocksAval[stockAmont] = Jorf['MP34'].stocks[stockAval]

        count += 1

stocksAmontMP34 = [['Stock_Sulfurique_MP34_Ligne 07&107', 'Stock_Phosphorique 29%_MP34_Ligne 107A', 'Stock_Phosphorique 54%_MP34_Ligne 107A', 'Stock_Ammoniac_MP34_Ligne 107', 'Stock_Fuel_MP34_Ligne 107A'],
['Stock_Sulfurique_MP34_Ligne 07&107', 'Stock_Phosphorique 29%_MP34_Ligne 107B&C', 'Stock_Phosphorique 54%_MP34_Ligne 107B&C', 'Stock_Ammoniac_MP34_Ligne 107', 'Stock_Fuel_MP34_Ligne 107B&C'],
['Stock_Sulfurique_MP34_Ligne 07&107', 'Stock_Phosphorique 29%_MP34_Ligne 107B&C', 'Stock_Phosphorique 54%_MP34_Ligne 107B&C', 'Stock_Ammoniac_MP34_Ligne 107', 'Stock_Fuel_MP34_Ligne 107B&C'],
['Stock_Sulfurique_MP34_Ligne 07&107', 'Stock_Phosphorique 29%_MP34_Ligne 07', 'Stock_Phosphorique 54%_MP34_Ligne 07', 'Stock_Ammoniac_MP34_Ligne 07', 'Stock_Fuel_MP34_Ligne 07'],
['Stock_Sulfurique_MP34_Ligne 07&107', 'Stock_Phosphorique 29%_MP34_Ligne 07', 'Stock_Phosphorique 54%_MP34_Ligne 07', 'Stock_Ammoniac_MP34_Ligne 07', 'Stock_Fuel_MP34_Ligne 07'],
['Stock_Sulfurique_MP34_Ligne 07&107', 'Stock_Phosphorique 29%_MP34_Ligne 07', 'Stock_Phosphorique 54%_MP34_Ligne 07', 'Stock_Ammoniac_MP34_Ligne 07', 'Stock_Fuel_MP34_Ligne 07'],
['Stock_Sulfurique_MP34_Ligne 07&107', 'Stock_Phosphorique 29%_MP34_Ligne 07', 'Stock_Phosphorique 54%_MP34_Ligne 07', 'Stock_Ammoniac_MP34_Ligne 07', 'Stock_Fuel_MP34_Ligne 07']]

count = 0
for ligne in Jorf["MP34"].lignesEngrais.values():
    for stock in stocksAmontMP34[count]:
        ligne.stocksAmont[stock] = Jorf['MP34'].stocks[stock]

    count += 1

for ligne in Jorf['JFF'].lignesEngrais.values():
    for stock in ['Stock_Sulfurique_JFF', 'Stock_Phosphorique 29%_JFF', 'Stock_Phosphorique 54%_JFF', 'Stcok_Ammoniac_JFF', 'Stock Fioul JFF']:
        ligne.stocksAmont[stock] = Jorf['JFF'].stocks[stock]

restStocksAmont =[['Stock_Sulfurique_JFD', 'Stock_Phosphorique 29%_JFD', 'Stock_Phosphorique 54%_JFD', 'Stcok_Ammoniac_JFD', 'Stock Fioul JFD'],
['Stock_Sulfurique_JFO', 'Stock_Phosphorique 29%_JFO', 'Stock_Phosphorique 54%_JFO', 'Stcok_Ammoniac_JFO', 'Stock Fioul JFO'],
['Stock_Sulfurique_JFQ', 'Stock_Phosphorique 29%_JFQ', 'Stock_Phosphorique 54%_JFQ', 'Stcok_Ammoniac_JFQ', 'Stock Fioul JFQ'],
['Stock_Sulfurique_JFT', 'Stock_Phosphorique 29%_JFT', 'Stock_Phosphorique 54%_JFT', 'Stcok_Ammoniac_JFT', 'Stock Fioul JFT']]

count = 0
for entité in Jorf.entités.values():
    if entité.nom not in ['MP34', 'JFF', 'IMACID', 'PMP']:
        for stock in restStocksAmont[count]:
           for ligne in entité.lignesEngrais.values():
               ligne.stocksAmont[stock] = entité.stocks[stock]
        count += 1

#
# for entité in Jorf.entités.values():
#     if entité.nom not in ['IMACID', 'PMP']:
#         for ligneEngrais in entité.lignesEngrais.values():
#             ligneEngrais.insertCommande(Jorf.listEngrais[0], 1000, 0)


def generateListEchange(currentEntité):
    result = ['extérieur']

    for entité in Jorf.entités.values():
        if entité.nom is not currentEntité:
            result.append(entité.nom)

    return result

# #"(self, fournisseur, produit, date, heure, quantité, débit):
#
# Jorf['MP34'].insertEchange(fournisseur='extérieur', produit='SOUFFRE', date='15/12/2019', quantité=1000, débit=16, heure=12)
# Jorf['MP34'].insertEchange(fournisseur='JFD', produit='H2S04', date='01/12/2019', quantité=1000, débit=16, heure=12)
# #
# # print(Jorf['MP34'].getEchanges('JFD'))
# print(Jorf['MP34'].échanges)
#print(generateListEchange('MP34'))

