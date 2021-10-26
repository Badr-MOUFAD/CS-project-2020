class Entité:
    def __init__(self, nom):
        self.PRODUIT_ECHANGEABLE = ['H2S04', 'H3PO4 29', 'H3PO4 54']
        self.PRODUIT_ECHANGEABLE_EXTERIEUR = ['SOUFFRE', 'H2S04']

        self.nom = nom

        self.ateliers = {}
        self.lignesEngrais = {}

        self.stocks = {}

        self.échanges = {'extérieur': []}
        for entité in ['MP34', "JFD", "JFF", "JFO", "JFQ", "JFT", "PMP", "IMACID"]:
            if self.nom == entité:
                continue

            self.échanges[entité] = []
        return

    def getAllLignesDeProduction(self):
        lignes = []

        for ligne in self.lignesEngrais.values():
            lignes += [ligne]

        for atelier in self.ateliers.values():
            lignes += atelier.getLignesDeProduction()

        return lignes

    def getAllLignesDeProduction_(self):
        lignes = []

        for atelier in self.ateliers.values():
            lignes += atelier.getLignesDeProduction()

        for ligne in self.lignesEngrais.values():
            lignes += [ligne]

        return lignes

    def getAtelier(self, nomAtelier):
        def getElementAt(index):
            count = 0
            for atelier in self.ateliers.values():
                if count == index:
                    return atelier
                count += 1
            return

        try:
            return self.ateliers[nomAtelier]
        except:
            if nomAtelier == 'sulfurique':
                return getElementAt(0)
            if nomAtelier == 'phosphorique 29':
                return getElementAt(1)
            if nomAtelier == 'phosphorique 54':
                return getElementAt(2)
        return

    def getAtelierOfLigne(self, ligne):
        for atelier in self.ateliers.values():
            if ligne in atelier:
                return atelier

        return

    def getLigne(self, nomLigne):
        for ligne in self.lignesEngrais:
            if ligne == nomLigne:
                return self.lignesEngrais[nomLigne]

        for atelier in self.ateliers.values():
            if atelier.getLigne(nomLigne) is not None:
                return atelier.getLigne(nomLigne)

        return

    def insertEchange(self, fournisseur, produit, date, heure, quantité, débit):
        currentEchanges = self.échanges[fournisseur]

        currentEchanges.append(Echange(produit, date, heure, quantité, débit))

        self.échanges[fournisseur] = currentEchanges
        return

    def getEchanges(self, fournisseur):
        produits = self.PRODUIT_ECHANGEABLE_EXTERIEUR if fournisseur == 'extérieur' else self.PRODUIT_ECHANGEABLE

        échanges = self.échanges[fournisseur]
        result = []

        for produit in produits:
            échangeProduit = []

            for échange in échanges:
                if produit == échange.produit:
                    échangeProduit.append(échange.get())
                    #result.append(échange.get())

            result.append(échangeProduit)

        return result


class Echange:
    def __init__(self, produit, date, heure, quantité, débit):
        self.produit = produit
        self.date = date
        self.heure = heure
        self.quantité = quantité
        self.débit = débit
        return

    def insert(self, produit, date, heure, quantité, débit):
        self.produit = produit
        self.date = date
        self.heure = heure
        self.quantité = quantité
        self.débit = débit
        return

    def get(self):
        return [self.date, self.heure, self.quantité, self.débit]


class Complexe:
    def __init__(self, nom):
        self.nom = nom

        self.entités = {}
        self.stocksCommun = {}

        # self.emploiRégimeDeMarche = [
        #     RégimeDeMarche('Ligne sulfurique 1 (A)', '12/05/2019', 0.6),
        #     RégimeDeMarche('Ligne sulfurique 3 (E)', '11/01/2019', 0.7),
        #     RégimeDeMarche('Ligne phosphorique 54 6', '10/02/2019', 0.3)
        # ]

        self.emploiRégimeDeMarche = {}

        self.emploiMaintenance = []

        self.exportMP34 = []

        self.listEngrais = ['DAP (Chambal)', 'DAP (Std)', 'DAP (EURO -normal)', 'DAP (EURO - fin)', 'DAP (Std Noir)',
                            'MAP (Std) (11-52) ', 'MAP (Clair) (11-52) ', 'MAP (TAP) (11-52)', 'MAP (Reach) (11-52) ',
                            'MAP (Std) (11-54) ', 'MAP (Clair) (11-54)', 'MAP (Reach) (11-54) ', 'MAP désulfaté',
                            'MAP (11-52) Zn', 'MAP Kidee', 'NPS (12-46-7S)', 'NPS (12-46-7S-Zn)', 'NPS (12-48-5s)',
                            'NPS (12-48-5s-Zn)', 'NPS (12-48-7s)', 'NPS (16-20-13S)', 'NPS (12-40-1Zn)',
                            'NPS (20-20-15S)', 'NPS (16-20)', 'NPS (12-46-7S-1Z)', 'TSP', 'ASP (Std)',
                            'ASP (euro) (19-38) ', 'ASP (Chambal) (19-38) ', 'ASP Borique', 'ASP Zinc',
                            'ASP (18,9-37,7-6,95S-0,1B)', 'ASP 17,7-35,5-7,6S-0,1B-2,2Zn', 'NPk (12-23-14)',
                            'NPk (14-23-14-B2O3)', 'NPk (12-24-12)', 'NPk (12-24-12-B2O3)', 'NPk (14-15-15)',
                            'NPk (14-15-15-B2O3)', 'NPK (10-18-24-7S)', 'NPK (14-28-14)', 'NPK (14-18-18-5S-1B2O3)',
                            'NPk (14-15-15-10S)', 'NPk (10-20-10-6S)', 'NPk (12-24-12-6S)', 'NPk (14-23-14-5S-1B2O3)',
                            'NPk (12-20-18-6S-1B2O3)', 'NPk (14-15-15-10S-1B2O3))', 'NPk (12-30-12-3S-0,1Cu-0,2ZN)',
                            'NPk(14-18-18-6S-1B2O3)', 'NPK (12-32-16-4S)']

        self.ENCHAINEMENT_ATELIER = ["sulfurique", "phosphorique 29", "phosphorique 54"]
        self.PRODUIT_ECHANGEABLE = ['Sulfurique (H2SO4)', 'Phosphorique 29 (H3PO4 29)', 'Phosphorique 54 (H3PO4 54)']
        self.PRODUIT_ECHANGEABLE_EXTERIEUR = ['Souffre', 'Sulfurique (H2SO4)']

        self.CONVENTION_ARRET = {"maintenace": 1, "non prévu": 2}
        self.CONVENTION_ETAT_STOCK = {"rupture": 1, "saturation": 2}

        self.__pourcentageRupture = 0.01
        self.__pourcentageSaturation = 0.99

        self.__timeLine = []#['22/11/2019 0' + str(i) + ':00:00' for i in range(12)]
        return

    def __getitem__(self, item):
        return self.entités[item]

    @property
    def pourcentageRupture(self):
        return self.__pourcentageRupture

    @pourcentageRupture.setter
    def pourcentageRupture(self, value):
        try:
            if abs(value-0.5) > 1:
                self.__pourcentageRupture = 0.01
                return

            self.__pourcentageRupture = float(value)
        except:
            self.__pourcentageRupture = 0.01
        return

    @property
    def pourcentageSaturation(self):
        return self.__pourcentageSaturation

    @pourcentageSaturation.setter
    def pourcentageSaturation(self, value):
        try:
            if abs(value - 0.5) > 1:
                self.__pourcentageSaturation = 0.99
                return

            self.__pourcentageSaturation = float(value)
        except:
            self.__pourcentageSaturation = 0.99

        return

    @property
    def timeLine(self):
        return self.__timeLine

    @timeLine.setter
    def timeLine(self, timeList):
        self.__timeLine = timeList

        for entité in self.entités.values():
            for stock in entité.stocks.values():
                stock.timeLine = timeList

            for ligne in entité.getAllLignesDeProduction():
                ligne.timeLine = timeList

        for stock in self.stocksCommun.values():
            stock.timeLine = timeList
        return

    def getAllLignesDeProduction(self):
        lignes = []

        for entité in self.entités.values():
            lignes += entité.getAllLignesDeProduction()

        return lignes

    def getAllLignesDeProduction_(self):
        lignes = []

        for entité in self.entités.values():
            lignes += entité.getAllLignesDeProduction_()

        return lignes

    def getAtelierOfLigne(self, nomLigne):
        for entité in self.entités.values():
            if entité.getAtelierOfLigne(nomLigne) is not None:
                return entité.getAtelierOfLigne(nomLigne)

        return

    def insertMaintenance(self, ligne, dateDébut, dateFin, périodicité):
        self.emploiMaintenance += [Maintenenance(ligne, dateDébut, dateFin, périodicité)]
        return

    def insertRégimeDeMarche(self, ligne, date, régime):
        for existingDate in self.emploiRégimeDeMarche:
            if date == existingDate:
                self.emploiRégimeDeMarche[existingDate].append([ligne, régime])

        self.emploiRégimeDeMarche[date] = [[ligne, régime]]
        return

    def insertExportMP34(self, date, heure, quantité, débit):
        self.exportMP34.append(Echange('H3PO4 54', date, heure, quantité, débit))
        return

    def getMaintenances(self):
        result = []

        for maintenance in self.emploiMaintenance:
            result.append(maintenance.getMaintenance())

        return result

    def getExportMP34(self):
        result = []

        for echange in self.exportMP34:
            result.append(echange.get())

        return result

    def getStock(self, nomStock):
        for entité in self.entités.values():
            try:
                stock = entité.stocks[nomStock]

                return stock
            except:
                continue

    def getLigne(self, nomLigne):
        for entité in self.entités.values():
            if entité.getLigne(nomLigne) is not None:
                return entité.getLigne(nomLigne)

        return


class Maintenenance:
    def __init__(self, ligne, dateDébut, dateFin, périodicité):
        self.ligne = ligne
        self.dateDébut = dateDébut
        self.dateFin = dateFin
        self.périodicité = périodicité
        return

    def getMaintenance(self):
        return [self.ligne, self.dateDébut, self.dateFin, self.périodicité]
