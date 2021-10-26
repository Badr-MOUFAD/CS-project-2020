from Components import navigate


mainSideBar = [
    navigate.SideBarButton(label='Générer fichier Input', link='/generation-input', active=False),
    navigate.SideBarButton(label='Visualiser fichier Output', link='/visualisation-output', active=False)
]

mainSideBarGenActive = [
    navigate.SideBarButton(label='Générer fichier Input', link='/generation-input', active=True),
    navigate.SideBarButton(label='Visualiser fichier Output', link='/visualisation-output', active=False),
    navigate.SideBarButton(label='Retour Acceuil', link='/', active=False)
]

mainSideBarVisActive = [
    navigate.SideBarButton(label='Générer fichier Input', link='/generation-input', active=False),
    navigate.SideBarButton(label='Visualiser fichier Output', link='/visualisation-output', active=True),
    navigate.SideBarButton(label='Retour Acceuil', link='/', active=False)
]

parametrageSideBarActive = [
    navigate.SideBarButton(label='Paramétrage des entités', link='/parametrage-MP34-page1', active=True),
    navigate.SideBarButton(label='Autre paramètres', link='/autre-parametre-page1', active=False),
    navigate.SideBarButton(label='Retour Acceuil', link='/', active=False)
]

autreSideBarActive = [
     navigate.SideBarButton(label='Paramétrage des entités', link='/parametrage-MP34-page1', active=False),
     navigate.SideBarButton(label='Autre paramètres', link='/autre-parametre-page1', active=True),
     navigate.SideBarButton(label='Retour Acceuil', link='/', active=False)
]


def sideBarVisualisation(*args):
    sideBar= [
        navigate.SideBarButton(label='Evolution des stocks', link='/visualisation-output-evolution-stocks',
                               active=args[0]),
        navigate.SideBarButton(label='Gant des Stocks', link='/visualisation-output-gantt-stocks', active=args[1]),
        navigate.SideBarButton(label='Gant des lignes de production',
                               link='/visualisation-output-gantt-lignes-production', active=args[2]),
        navigate.SideBarButton(label='Retour Acceuil', link='/', active=False)
    ]

    return sideBar
