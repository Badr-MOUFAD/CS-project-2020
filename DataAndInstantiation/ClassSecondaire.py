from DataAndInstantiation.ClassElémentaire import LigneDeProduction

class Atelier:
    def __init__(self, nom):
        self.nom = nom

        self.lignesDeProduction = {}

        self.stocksAmont = {}
        self.stocksAval = {}
        return

    def __contains__(self, ligne):
        if ligne in self.lignesDeProduction:
            return True

        return False

    def getLignesDeProduction(self):
        lignes = []

        for ligne in self.lignesDeProduction.values():
            lignes.append(ligne)

        return lignes

    def getCauseArrêt(self, ligneDeProdution, période):
        return

    def getDécision(self, cas):
        return

    def getLigne(self, nomLigne):
        for ligne in self.lignesDeProduction:
            if ligne == nomLigne:
                return self.lignesDeProduction[nomLigne]

        return


class LigneEngrais(LigneDeProduction):
    def __init__(self, nom, mappingMaintenance, mappingExcel):
        super().__init__(nom=nom, mappingMaintenance=mappingMaintenance)

        self.mappingExcel = mappingExcel

        self.stocksAmont = {}

        self.__engraisAProduire = []
        self.__quantitéAProduire = []
        self.__tempsDeLancement = []
        return

    def insertCommande(self, engrais, quantité, tempsLancement):
        self.__engraisAProduire.append(engrais)
        self.__quantitéAProduire.append(quantité)
        self.__tempsDeLancement.append(tempsLancement)
        return

    def getNombreCommandes(self):
        return len(self.__engraisAProduire)

    def getCommandes(self):
        commande = []

        for i in range(self.getNombreCommandes()):
            commande.append([self.__engraisAProduire[i], self.__quantitéAProduire[i], self.__tempsDeLancement[i]])

        return commande

    def getCauseArrêt(self, période):
        return