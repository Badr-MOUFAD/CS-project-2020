class LigneDeProduction:
    def __init__(self, nom, mappingMaintenance):
        self.nom = nom
        self.mappingMaintenance = mappingMaintenance

        self.disponibilité = 1
        self.régimeDeMarche = [1]
        self.maintenance = []
        self.production = []

        self.states = []
        self.timeLine = []

        self.CONVENTION_ETAT_LIGNE = {
            '1': 'Normal',
            '0': "Arret",
            '2': "Maintenance"
        }
        return

    def __getitem__(self, index):
        return self.states[index]

    def __setitem__(self, index, value):
        self.states[index] = value
        return

    def __len__(self):
        return len(self.states)

    def getState(self, période):
        return

    def createStateForGantt(self):
        result = []

        i = 1
        while i < len(self):
            periode = self.indexesHavingSameState(fromIndex=i)
            startDate = self.timeLine[periode[0]]
            endDate = self.timeLine[periode[len(periode) - 1] + 1]

            currentState = self.CONVENTION_ETAT_LIGNE[str(self[i])]

            result.append({
                'Task': self.nom,
                'Start': startDate,
                'Finish': endDate,
                'Ressource': currentState
            })

            i += len(periode)

        return result

    def indexesHavingSameState(self, fromIndex):
        result = [fromIndex]

        for i in range(fromIndex + 1, len(self)):
            if self[i] != self[fromIndex]:
                break

            result.append(i)

        return result


class Stock:
    def __init__(self, nom, capacitéMax):
        self.nom = nom
        self.capacitéMax = capacitéMax

        self.capacitéUtilisé = [0]

        self.states = []
        self.timeLine = []

        self.CONVENTION_ETAT_STOCK = {
            '0': 'Normal',
            '1': "Rupture",
            '2': "Saturation"
        }

        return

    def __getitem__(self, index):
        return self.states[index]

    def __setitem__(self, index, value):
        self.states[index] = value
        return

    def __len__(self):
        return len(self.states)

    def getState(self, période):
        return

    def createStateForGantt(self):
        result = []

        i = 1
        while i < len(self):
            periode = self.indexesHavingSameState(fromIndex=i)
            startDate = self.timeLine[periode[0]]
            endDate = self.timeLine[periode[len(periode) - 1] + 1] if periode[len(periode) - 1] + 1 < len(self.timeLine) else self.timeLine[-1]

            currentState = self.CONVENTION_ETAT_STOCK[str(self[i])]

            result.append({
                'Task': self.nom,
                'Start': startDate,
                'Finish': endDate,
                'Ressource': currentState
            })

            i += len(periode)

        return result  #(Task='Morning Sleep', Start='2016-01-01', Finish='2016-01-01 6:00:00', Resource='Sleep')

    # période dans lesquels le stock a même etat
    def indexesHavingSameState(self, fromIndex):
        result = [fromIndex]

        for i in range(fromIndex+1, len(self)):
            if self[i] != self[fromIndex]:
                break

            result.append(i)

        return result
