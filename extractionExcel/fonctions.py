import pandas as pd
import datetime
import time
import numpy as np

from DataAndInstantiation import Instanciation
from extractionExcel.fonctionStateStocks import gantStock


Jorf = Instanciation.Jorf


# functions :
# def extractionTimeLine():
#     timeline = []
#     df22 = evolutionProductionLigne.iloc[:,1]
#     df33 = df22.tolist()
#     df1 = parametrage.iloc[1, 3]
#     date_time_obj = datetime.datetime.strptime(df1, '%d/%m/%Y')
#     date_time = date_time_obj.strftime("%Y-%m-%d, %H:%M:%S")
#
#     for i in df33:
#         timeline.append(str(i))
#
#     del timeline[0]
#     Jorf.timeLine = timeline
#     Jorf.timeLine.insert(0, date_time)
#     return
#
#
# def extractionStock(nomStock):
#     df6 = evolutionStock[nomStock]
#     df7 = df6.loc[0: len(Jorf.timeLine)-1]
#     stockEvolutionFinale = df7.tolist()
#
#     return stockEvolutionFinale
#
#
# def insertDataInStocks():
#     for entité in Jorf.entités.values():
#         for stock in entité.stocks.values():
#             try:
#                 stock.capacitéUtilisé = extractionStock(stock.nom)
#                 stock.states = gantStock(stock.nom)
#             except:
#                 pass
#     return
#
# # ligne de production
# def fromTimeToIndex(time):
#     d2 = Jorf.timeLine[len(Jorf.timeLine) - 1]
#
#     d1 = time
#
#     d1 = datetime.datetime.strptime(d1, "%Y-%m-%d %H:%M:%S")
#
#     d2 = datetime.datetime.strptime(d2, "%Y-%m-%d %H:%M:%S")
#
#     d3 = ((d2 - d1).days) * 24 + ((d2 - d1).seconds) / 3600
#
#     index = int(len(Jorf.timeLine) - d3) - 1
#
#     return index
#
#
# def getMaintenace():
#     liste = []
#
#     liste = [maintenance.columns.values.tolist()] + maintenance.values.tolist()
#
#     return liste
#
#
# def applyMaintenance(ligne, index, constante):
#     a = getMaintenace()
#
#     distance = fromTimeToIndex(a[index][2].strftime("%Y-%m-%d %H:%M:%S")) - fromTimeToIndex(
#         a[index][1].strftime("%Y-%m-%d %H:%M:%S"))
#
#     m = []
#
#     f = fromTimeToIndex(a[index][2].strftime("%Y-%m-%d %H:%M:%S"))
#
#     d = fromTimeToIndex(a[index][1].strftime("%Y-%m-%d %H:%M:%S"))
#
#     periode = int(int(a[index][3]) / 60)
#
#     b = ligne
#
#     c = constante
#
#     for i in range(0, len(b)):
#         m.append(9)
#
#     for i in range(0, len(b)):
#         m[i] = b[i]
#
#     if f == len(b) and d == 0:
#         m[d:f] = [2 for x in range(f - d)]
#
#     if f == len(b) and d != 0:
#         m[d + c:f] = [2 for x in range(f - d - c)]
#
#     if f != len(b) and d + c < len(b):
#
#         while d + c < len(b):
#
#             if d + c + distance < len(b):
#
#                 m[d + c:f + c + 1] = [2 for x in range(f - d + 1)]
#
#             else:
#
#                 m[d + c:len(b)] = [2 for x in range(len(b) - d - c)]
#
#             d = d + periode
#
#             f = f + periode
#
#     if d + c > len(b):
#         pass
#
#     return m
#
#
# def typeAtelier(nom):
#     nomComplet = Jorf.getAtelierOfLigne(nom).nom
#
#     nomRed = nomComplet.split("_")[1]
#
#     return nomRed
#
#
# def activiteProductionMp34(nomLigne):
#     test = evolutionProductionLigne
#
#     test2 = test.iloc[0, 0:37]
#
#     test3 = test2.iloc[2:]
#
#     test4 = test3.tolist()
#
#     ligneProdMod = evolutionProductionLigne.iloc[:, 2:37]
#
#     ligneProdMod.columns = test4
#
#     df2 = ligneProdMod[nomLigne]
#
#     df2 = df2.replace(np.nan, 0)
#
#     prodFinale = df2.tolist()
#
#     del prodFinale[0]
#
#     prodFinale2 = ([i if i == 0 else 1 for i in prodFinale])
#
#     gm = getMaintenace()
#
#     nomMaintenance = []
#
#     for i in gm:
#         nomMaintenance.append(i[0])
#
#     if Jorf.getLigne(nomLigne).mappingMaintenance in nomMaintenance:
#
#         if typeAtelier(nomLigne) == "Sulfurique":
#             return applyMaintenance(prodFinale2, nomMaintenance.index(Jorf.getLigne(nomLigne).mappingMaintenance), 0)
#
#         if typeAtelier(nomLigne) == "Phosphorique 29%":
#             return applyMaintenance(prodFinale2, nomMaintenance.index(Jorf.getLigne(nomLigne).mappingMaintenance), 4)
#
#         if typeAtelier(nomLigne) == "Phosphorique 54%":
#             return applyMaintenance(prodFinale2, nomMaintenance.index(Jorf.getLigne(nomLigne).mappingMaintenance), 1)
#
#     return prodFinale2
#
#
# def activiteProductionJfc(nomLigne):
#     test = productionJFC
#
#     test2 = test.iloc[0, 0:37]
#
#     test3 = test2.iloc[2:]
#
#     test4 = test3.tolist()
#
#     ligneProdjfc = productionJFC.iloc[:, 2:37]
#
#     ligneProdjfc.columns = test4
#
#     df2 = ligneProdjfc[nomLigne]
#
#     df2 = df2.replace(np.nan, 0)
#
#     prodFinale = df2.tolist()
#
#     del prodFinale[0]
#
#     prodFinale2 = ([i if i == 0 else 1 for i in prodFinale])
#
#     gm = getMaintenace()
#
#     nomMaintenance = []
#
#     for i in gm:
#         nomMaintenance.append(i[0])
#
#     if Jorf.getLigne(nomLigne).mappingMaintenance in nomMaintenance:
#
#         if typeAtelier(nomLigne) == "Sulfurique":
#             return applyMaintenance(prodFinale2, nomMaintenance.index(Jorf.getLigne(nomLigne).mappingMaintenance), 0)
#
#         if typeAtelier(nomLigne) == "Phosphorique 29%":
#             return applyMaintenance(prodFinale2, nomMaintenance.index(Jorf.getLigne(nomLigne).mappingMaintenance), 4)
#
#         if typeAtelier(nomLigne) == "Phosphorique 54%":
#             return applyMaintenance(prodFinale2, nomMaintenance.index(Jorf.getLigne(nomLigne).mappingMaintenance), 1)
#
#     return prodFinale2
#
#
# def activiteEngraisMp34(nom):
#     numero = Jorf.getLigne(nom).mappingExcel
#
#     ligneEng = evolutionProductionLigne.iloc[1:, 44:60]
#
#     carnet1 = parametrage.iloc[132:219, 1]
#
#     carnet2 = carnet1.replace(np.nan, 0)
#
#     carnet3 = carnet2.tolist()
#
#     carnet4 = [i for i in carnet3 if i != 0]
#
#     mylist = list(dict.fromkeys(carnet4))
#
#     # print(carnet4)
#
#     listeInter = []
#
#     for i in mylist:
#         listeInter.append([i, carnet4.count(i)])
#
#     carnetf = {}
#
#     a = []
#
#     c = 0
#
#     for i in listeInter:
#
#         for j in range(c + 1, i[1] + c + 1):
#             a.append("Commande " + str(j) + str(".1"))
#
#             c = c + 1
#
#         carnetf[i[0]] = a
#
#         a = []
#
#     # print(listeInter)
#
#     # print(carnetf)
#
#     k = []
#
#     for i in range(0, len(Jorf.timeLine) - 1):
#         k.append(0)
#
#     for i in range(0, len(carnetf[numero])):
#
#         # print(ligneEng[carnetf[numero][i]].replace(np.nan, 0).tolist())
#
#         for j in range(0, len(Jorf.timeLine) - 1):
#             k[j] = k[j] + float(ligneEng[carnetf[numero][i]].replace(np.nan, 0).tolist()[j])
#
#     engFinale2 = ([0 if i == 0 else 1 for i in k])
#
#     gm = getMaintenace()
#
#     nomMaintenance = []
#
#     for i in gm:
#         nomMaintenance.append(i[0])
#
#     if Jorf.getLigne(nom).mappingMaintenance in nomMaintenance:
#         return applyMaintenance(engFinale2, nomMaintenance.index(Jorf.getLigne(nom).mappingMaintenance), 4)
#
#     return engFinale2
#
#
# def activiteEngraisJFC(nom):
#     numero = Jorf.getLigne(nom).mappingExcel
#
#     ligneEng = engraisJFC.iloc[1:, 2:]
#
#     carnet1 = parametrage.iloc[132:219, 8]
#
#     carnet2 = carnet1.replace(np.nan, 0)
#
#     carnet3 = carnet2.tolist()
#
#     carnet4 = [i for i in carnet3 if i != 0]
#
#     mylist = list(dict.fromkeys(carnet4))
#
#     # print(carnet4)
#
#     listeInter = []
#
#     for i in mylist:
#         listeInter.append([i, carnet4.count(i)])
#
#     carnetf = {}
#
#     a = []
#
#     c = 0
#
#     for i in listeInter:
#
#         for j in range(c + 1, i[1] + c + 1):
#             a.append("Commande " + str(j) + str(".1"))
#
#             c = c + 1
#
#         carnetf[i[0]] = a
#
#         a = []
#
#     # print(listeInter)
#
#     # print(carnetf)
#
#     k = []
#
#     for i in range(0, len(Jorf.timeLine) - 1):
#         k.append(0)
#
#     for i in range(0, len(carnetf[numero])):
#
#         # print(ligneEng[carnetf[numero][i]].replace(np.nan, 0).tolist())
#
#         for j in range(0, len(Jorf.timeLine) - 1):
#             k[j] = k[j] + float(ligneEng[carnetf[numero][i]].replace(np.nan, 0).tolist()[j])
#
#     engFinale2 = ([0 if i == 0 else 1 for i in k])
#
#     gm = getMaintenace()
#
#     nomMaintenance = []
#
#     for i in gm:
#         nomMaintenance.append(i[0])
#
#     if Jorf.getLigne(nom).mappingMaintenance in nomMaintenance:
#         return applyMaintenance(engFinale2, nomMaintenance.index(Jorf.getLigne(nom).mappingMaintenance), 4)
#
#     return engFinale2
#
#
#
# # chemin d'accès au fichier source
# pathInPut = "C:/Users/HP/Desktop/test2.xlsm"
# pathOutPut = "C:/Users/HP/Desktop/RESULTATS_SIMULATION (4).xlsm"
#
# parametrage = pd.read_excel(pathInPut, sheet_name="Paramétrage")
# evolutionProductionLigne = pd.read_excel(pathOutPut, sheet_name='EVOLUTION PRODUCTIONS par LIGNE')
# evolutionStock = pd.read_excel(pathOutPut, sheet_name='EVOLUTION STOCKS')
# regimeDeMarche = pd.read_excel(pathInPut, sheet_name="Regime de marche")
# maintenance = pd.read_excel(pathInPut, sheet_name="Scheduled Maintenance1", usecols=[0, 1, 2, 3])
# productionJFC = pd.read_excel(pathOutPut, sheet_name='JFC Evolution Production ligne')
# engraisJFC = pd.read_excel(pathOutPut, sheet_name='JFC Production engrais ligne')
#
# # insertion etat stocks & time ligne:
# extractionTimeLine()
# insertDataInStocks()
#
# # pour MP34
#     # insertion etat ligne production MP34
# for atelier in Jorf['MP34'].ateliers.values():
#     for ligne in atelier.lignesDeProduction.values():
#         try:
#             ligne.states = activiteProductionMp34(nomLigne=ligne.nom)
#         except:
#             pass
#
#     #insertion etat ligne engrais:
# for ligne in Jorf['MP34'].lignesEngrais.values():
#     try:
#         ligne.states = activiteEngraisMp34(ligne.nom)
#     except:
#         pass
#     #ligne.states = activiteEngraisMp34(ligne.nom)
#
# # pour JFC
#     # insertion etat ligne de production
# for nomEntité in Jorf.entités:
#     if nomEntité == 'MP34':
#         continue
#
#     for atelier in Jorf[nomEntité].ateliers.values():
#         for ligne in atelier.lignesDeProduction.values():
#             try:
#                 ligne.states = activiteProductionJfc(ligne.nom)
#             except:
#                 pass
#
#     # insertion etat ligne d'engrais
#     for ligne in Jorf[nomEntité].lignesEngrais.values():
#         try:
#             ligne.states = activiteEngraisJFC(ligne.nom)
#         except:
#             pass


def uploadDataFromExcels(pathInput, pathOutput):

    def extractionTimeLine():
        timeline = []
        df22 = evolutionProductionLigne.iloc[:, 1]
        df33 = df22.tolist()
        df1 = parametrage.iloc[1, 3]
        try:
            date_time_obj = datetime.datetime.strptime(df1, '%d/%m/%Y')
            date_time = date_time_obj.strftime("%Y-%m-%d, %H:%M:%S")
        except:
            date_time = df1.strftime("%Y-%m-%d, %H:%M:%S")
        for i in df33:
            timeline.append(str(i))

        del timeline[0]
        Jorf.timeLine = timeline
        Jorf.timeLine.insert(0, date_time)
        return

    def extractionStock(nomStock):
        df6 = evolutionStock[nomStock]
        df7 = df6.loc[0: len(Jorf.timeLine) - 1]
        stockEvolutionFinale = df7.tolist()

        return stockEvolutionFinale

    def insertDataInStocks():
        for entité in Jorf.entités.values():
            for stock in entité.stocks.values():
                try:
                    stock.capacitéUtilisé = extractionStock(stock.nom)
                    stock.states = gantStock(stock.nom)
                except:
                    pass
        return

    # ligne de production
    def fromTimeToIndex(time):
        d2 = Jorf.timeLine[len(Jorf.timeLine) - 1]

        d1 = time

        d1 = datetime.datetime.strptime(d1, "%Y-%m-%d %H:%M:%S")

        d2 = datetime.datetime.strptime(d2, "%Y-%m-%d %H:%M:%S")

        d3 = ((d2 - d1).days) * 24 + ((d2 - d1).seconds) / 3600

        index = int(len(Jorf.timeLine) - d3) - 1

        return index

    def getMaintenace():
        liste = []

        liste = [maintenance.columns.values.tolist()] + maintenance.values.tolist()

        return liste

    def applyMaintenance(ligne, index, constante):
        a = getMaintenace()

        distance = fromTimeToIndex(a[index][2].strftime("%Y-%m-%d %H:%M:%S")) - fromTimeToIndex(
            a[index][1].strftime("%Y-%m-%d %H:%M:%S"))

        m = []

        f = fromTimeToIndex(a[index][2].strftime("%Y-%m-%d %H:%M:%S"))

        d = fromTimeToIndex(a[index][1].strftime("%Y-%m-%d %H:%M:%S"))

        periode = int(int(a[index][3]) / 60)

        b = ligne

        c = constante

        for i in range(0, len(b)):
            m.append(9)

        for i in range(0, len(b)):
            m[i] = b[i]

        if f == len(b) and d == 0:
            m[d:f] = [2 for x in range(f - d)]

        if f == len(b) and d != 0:
            m[d + c:f] = [2 for x in range(f - d - c)]

        if f != len(b) and d + c < len(b):

            while d + c < len(b):

                if d + c + distance < len(b):

                    m[d + c:f + c + 1] = [2 for x in range(f - d + 1)]

                else:

                    m[d + c:len(b)] = [2 for x in range(len(b) - d - c)]

                d = d + periode

                f = f + periode

        if d + c > len(b):
            pass

        return m

    def typeAtelier(nom):
        nomComplet = Jorf.getAtelierOfLigne(nom).nom

        nomRed = nomComplet.split("_")[1]

        return nomRed

    def activiteProductionMp34(nomLigne):
        test = evolutionProductionLigne

        test2 = test.iloc[0, 0:37]

        test3 = test2.iloc[2:]

        test4 = test3.tolist()

        ligneProdMod = evolutionProductionLigne.iloc[:, 2:37]

        ligneProdMod.columns = test4

        df2 = ligneProdMod[nomLigne]

        df2 = df2.replace(np.nan, 0)

        prodFinale = df2.tolist()

        del prodFinale[0]

        prodFinale2 = ([i if i == 0 else 1 for i in prodFinale])

        gm = getMaintenace()

        nomMaintenance = []

        for i in gm:
            nomMaintenance.append(i[0])

        if Jorf.getLigne(nomLigne).mappingMaintenance in nomMaintenance:

            if typeAtelier(nomLigne) == "Sulfurique":
                return applyMaintenance(prodFinale2, nomMaintenance.index(Jorf.getLigne(nomLigne).mappingMaintenance),
                                        0)

            if typeAtelier(nomLigne) == "Phosphorique 29%":
                return applyMaintenance(prodFinale2, nomMaintenance.index(Jorf.getLigne(nomLigne).mappingMaintenance),
                                        4)

            if typeAtelier(nomLigne) == "Phosphorique 54%":
                return applyMaintenance(prodFinale2, nomMaintenance.index(Jorf.getLigne(nomLigne).mappingMaintenance),
                                        1)

        return prodFinale2

    def activiteProductionJfc(nomLigne):
        test = productionJFC

        test2 = test.iloc[0, 0:37]

        test3 = test2.iloc[2:]

        test4 = test3.tolist()

        ligneProdjfc = productionJFC.iloc[:, 2:37]

        ligneProdjfc.columns = test4

        df2 = ligneProdjfc[nomLigne]

        df2 = df2.replace(np.nan, 0)

        prodFinale = df2.tolist()

        del prodFinale[0]

        prodFinale2 = ([i if i == 0 else 1 for i in prodFinale])

        gm = getMaintenace()

        nomMaintenance = []

        for i in gm:
            nomMaintenance.append(i[0])

        if Jorf.getLigne(nomLigne).mappingMaintenance in nomMaintenance:

            if typeAtelier(nomLigne) == "Sulfurique":
                return applyMaintenance(prodFinale2, nomMaintenance.index(Jorf.getLigne(nomLigne).mappingMaintenance),
                                        0)

            if typeAtelier(nomLigne) == "Phosphorique 29%":
                return applyMaintenance(prodFinale2, nomMaintenance.index(Jorf.getLigne(nomLigne).mappingMaintenance),
                                        4)

            if typeAtelier(nomLigne) == "Phosphorique 54%":
                return applyMaintenance(prodFinale2, nomMaintenance.index(Jorf.getLigne(nomLigne).mappingMaintenance),
                                        1)

        return prodFinale2

    def activiteEngraisMp34(nom):
        numero = Jorf.getLigne(nom).mappingExcel

        ligneEng = evolutionProductionLigne.iloc[1:, 44:60]

        carnet1 = parametrage.iloc[132:219, 1]

        carnet2 = carnet1.replace(np.nan, 0)

        carnet3 = carnet2.tolist()

        carnet4 = [i for i in carnet3 if i != 0]

        mylist = list(dict.fromkeys(carnet4))

        # print(carnet4)

        listeInter = []

        for i in mylist:
            listeInter.append([i, carnet4.count(i)])

        carnetf = {}

        a = []

        c = 0

        for i in listeInter:

            for j in range(c + 1, i[1] + c + 1):
                a.append("Commande " + str(j) + str(".1"))

                c = c + 1

            carnetf[i[0]] = a

            a = []

        # print(listeInter)

        # print(carnetf)

        k = []

        for i in range(0, len(Jorf.timeLine) - 1):
            k.append(0)

        for i in range(0, len(carnetf[numero])):

            # print(ligneEng[carnetf[numero][i]].replace(np.nan, 0).tolist())

            for j in range(0, len(Jorf.timeLine) - 1):
                k[j] = k[j] + float(ligneEng[carnetf[numero][i]].replace(np.nan, 0).tolist()[j])

        engFinale2 = ([0 if i == 0 else 1 for i in k])

        gm = getMaintenace()

        nomMaintenance = []

        for i in gm:
            nomMaintenance.append(i[0])

        if Jorf.getLigne(nom).mappingMaintenance in nomMaintenance:
            k1=applyMaintenance(engFinale2, nomMaintenance.index(Jorf.getLigne(nom).mappingMaintenance), 4)
            k1[0]=1
            k1[1]=1
            k1[2]=1
            return k1
        engFinale2[0]=1
        engFinale2[1]=1
        engFinale2[2]=1
        return  engFinale2
    def activiteEngraisJFC(nom):
        numero = Jorf.getLigne(nom).mappingExcel

        ligneEng = engraisJFC.iloc[1:, 2:]

        carnet1 = parametrage.iloc[132:219, 8]

        carnet2 = carnet1.replace(np.nan, 0)

        carnet3 = carnet2.tolist()

        carnet4 = [i for i in carnet3 if i != 0]

        mylist = list(dict.fromkeys(carnet4))

        # print(carnet4)

        listeInter = []

        for i in mylist:
            listeInter.append([i, carnet4.count(i)])

        carnetf = {}

        a = []

        c = 0

        for i in listeInter:

            for j in range(c + 1, i[1] + c + 1):
                a.append("Commande " + str(j) + str(".1"))

                c = c + 1

            carnetf[i[0]] = a

            a = []

        # print(listeInter)

        # print(carnetf)

        k = []

        for i in range(0, len(Jorf.timeLine) - 1):
            k.append(0)

        for i in range(0, len(carnetf[numero])):

            # print(ligneEng[carnetf[numero][i]].replace(np.nan, 0).tolist())

            for j in range(0, len(Jorf.timeLine) - 1):
                k[j] = k[j] + float(ligneEng[carnetf[numero][i]].replace(np.nan, 0).tolist()[j])

        engFinale2 = ([0 if i == 0 else 1 for i in k])

        gm = getMaintenace()

        nomMaintenance = []

        for i in gm:
            nomMaintenance.append(i[0])

        if Jorf.getLigne(nom).mappingMaintenance in nomMaintenance:
            k2=applyMaintenance(engFinale2, nomMaintenance.index(Jorf.getLigne(nom).mappingMaintenance), 4)
            k2[0]=1
            k2[1]=1
            k2[2]=1
            return k2
        engFinale2[0]=1
        engFinale2[1]=1
        engFinale2[2]=1
        return engFinale2
    # chemin d'accès au fichier source
    pathInPut = pathInput
    pathOutPut = pathOutput

    parametrage = pd.read_excel(pathInPut, sheet_name="Paramétrage")
    evolutionProductionLigne = pd.read_excel(pathOutPut, sheet_name='EVOLUTION PRODUCTIONS par LIGNE')
    evolutionStock = pd.read_excel(pathOutPut, sheet_name='EVOLUTION STOCKS')
    regimeDeMarche = pd.read_excel(pathInPut, sheet_name="Regime de marche")
    maintenance = pd.read_excel(pathInPut, sheet_name="Scheduled Maintenance1", usecols=[0, 1, 2, 3])
    productionJFC = pd.read_excel(pathOutPut, sheet_name='JFC Evolution Production ligne')
    engraisJFC = pd.read_excel(pathOutPut, sheet_name='JFC Production engrais ligne')

    # insertion etat stocks & time ligne:
    extractionTimeLine()
    insertDataInStocks()

    # pour MP34
    # insertion etat ligne production MP34
    for atelier in Jorf['MP34'].ateliers.values():
        for ligne in atelier.lignesDeProduction.values():
            try:
                ligne.states = activiteProductionMp34(nomLigne=ligne.nom)
            except:
                pass

        # insertion etat ligne engrais:
    for ligne in Jorf['MP34'].lignesEngrais.values():
        try:
            ligne.states = activiteEngraisMp34(ligne.nom)
        except:
            pass
        # ligne.states = activiteEngraisMp34(ligne.nom)

    # pour JFC
    # insertion etat ligne de production
    for nomEntité in Jorf.entités:
        if nomEntité == 'MP34':
            continue

        for atelier in Jorf[nomEntité].ateliers.values():
            for ligne in atelier.lignesDeProduction.values():
                try:
                    ligne.states = activiteProductionJfc(ligne.nom)
                except:
                    pass

        # insertion etat ligne d'engrais
        for ligne in Jorf[nomEntité].lignesEngrais.values():
            try:
                ligne.states = activiteEngraisJFC(ligne.nom)
            except:
                pass
    return
