class Quoridor:
    def __init__(self, joueurs, murs=None):
        #jeu = Quoridor(["joueur 1", "joueur 2"])
        def débuter_partie(idul):
          url_base = 'https://python.gel.ulaval.ca/quoridor/api/débuter'
          rep = requests.post(url_base+'débuter/', data={'idul': idul})
          rep.json()
          if rep.status_code == 200:
            rep = rep.json()
            print(rep) 
          else:
            raise RuntimeError('il y a forcement une erreur dans le code')

        # raise QuoridorError if l'argument 'joueurs' n'est pas itérable.
        # raise QuoridorError if l'itérable de joueurs en contient un nombre différent de deux.
        # raise QuoridorError if le nombre de murs qu'un joueur peut placer est >10, ou négatif.
        # raise QuoridorError if la position d'un joueur est invalide.
        # raise QuoridorError if l'argument 'murs' n'est pas un dictionnaire lorsque présent.
        # raise QuoridorError if le total des murs placés et plaçables n'est pas égal à 20.
        # raise QuoridorError if la position d'un mur est invalide.

def __str__(self):
          def afficher_damier_ascii():
            print('Légende: 1=idul, 2=automate')
            print('   -----------------------------------')
            for i in range(9,0,-1):
                if i>1:
                print(str(i) + ' |' + ' .  '*9)
                print('  |                                   |' )
                if i==1:
              print(str(i) + ' |' + ' .  '*9 )
            print('--|-----------------------------------')
            print('  | 1   2   3   4   5   6   7   8   9')
            return(afficher_damier_ascii())
            
def état_partie(self):

    url_base = 'https://python.gel.ulaval.ca/quoridor/api/lister'
    rep = requests.get(url_base+'lister/', params={'idul': idul})
    if rep.status_code == 200:
        rep = rep.json()
        return(rep) 
    else:
        RuntimeError('il y a forcement Boom')
        
        """
        Produire l'état actuel de la partie.

        :returns: une copie de l'état actuel du jeu sous la forme d'un dictionnaire:
        {
            'joueurs': [
                {'nom': nom1, 'murs': n1, 'pos': (x1, y1)},
                {'nom': nom2, 'murs': n2, 'pos': (x2, y2)},
            ],
            'murs': {
                'horizontaux': [...],
                'verticaux': [...],
            }
        }
        
        où la clé 'nom' d'un joueur est associée à son nom, la clé 'murs' est associée 
        au nombre de murs qu'il peut encore placer sur ce damier, et la clé 'pos' est 
        associée à sa position sur le damier. Une position est représentée par un tuple 
        de deux coordonnées x et y, où 1<=x<=9 et 1<=y<=9.

        Les murs actuellement placés sur le damier sont énumérés dans deux listes de
        positions (x, y). Les murs ont toujours une longueur de 2 cases et leur position
        est relative à leur coin inférieur gauche. Par convention, un mur horizontal se
        situe entre les lignes y-1 et y, et bloque les colonnes x et x+1. De même, un
        mur vertical se situe entre les colonnes x-1 et x, et bloque les lignes y et y+1.
        """
def partie_terminée(self):
    url_base = 'https://python.gel.ulaval.ca/quoridor/api/jouer'
    rep = requests.post(url_base+'jouer/', data={'id_partie': id_partie, 'type_coup': type_coup, 'position': position})
    rep.json()
    if rep.status_code == 200:
        rep = rep.json()
        print(rep) 
    else:
        raise RuntimeError('il y a forcement une erreur dans le code')
    if id_partie or type_coup or position == None:
        raise StopIteration('Vous avez gagné')

        """
        Déterminer si la partie est terminée.

        :returns: le nom du gagnant si la partie est terminée; False autrement.
        """
        jeu = Quoridor(joueur 1, joueur 2)






        raise QuoridorError if l'argument 'joueurs' n'est pas itérable.
        raise QuoridorError if l'itérable de joueurs en contient un nombre différent de deux.
        raise QuoridorError if le nombre de murs qu'un joueur peut placer est >10, ou négatif.
        raise QuoridorError if la position d'un joueur est invalide.
        raise QuoridorError if l'argument 'murs' n'est pas un dictionnaire lorsque présent.
        raise QuoridorError if le total des murs placés et plaçables n'est pas égal à 20.
        raise QuoridorError if la position d'un mur est invalide.







import networkx as nx


def construire_graphe(joueurs, murs_horizontaux, murs_verticaux):
    """
    Crée le graphe des déplacements admissibles pour les joueurs.

    :param joueurs: une liste des positions (x,y) des joueurs.
    :param murs_horizontaux: une liste des positions (x,y) des murs horizontaux.
    :param murs_verticaux: une liste des positions (x,y) des murs verticaux.
    :returns: le graphe bidirectionnel (en networkX) des déplacements admissibles.
    """
    graphe = nx.DiGraph()

    # pour chaque colonne du damier
    for x in range(1, 10):
        # pour chaque ligne du damier
        for y in range(1, 10):
            # ajouter les arcs de tous les déplacements possibles pour cette tuile
            if x > 1:
                graphe.add_edge((x, y), (x-1, y))
            if x < 9:
                graphe.add_edge((x, y), (x+1, y))
            if y > 1:
                graphe.add_edge((x, y), (x, y-1))
            if y < 9:
                graphe.add_edge((x, y), (x, y+1))

    # retirer tous les arcs qui croisent les murs horizontaux

for x, y in murs_verticaux:
        graphe.remove_edge((x-1, y), (x, y))
        graphe.remove_edge((x, y), (x-1, y))
        graphe.remove_edge((x-1, y+1), (x, y+1))
        graphe.remove_edge((x, y+1), (x-1, y+1))

    # retirer tous les arcs qui pointent vers les positions des joueurs
    # et ajouter les sauts en ligne droite ou en diagonale, selon le cas
    for joueur in map(tuple, joueurs):

        for prédécesseur in list(graphe.predecessors(joueur)):
            graphe.remove_edge(prédécesseur, joueur)

            # si admissible, ajouter un lien sauteur
            successeur = (2*joueur[0]-prédécesseur[0], 2*joueur[1]-prédécesseur[1])

            if successeur in graphe.successors(joueur) and successeur not in joueurs:
                # ajouter un saut en ligne droite
                graphe.add_edge(prédécesseur, successeur)

            else:
                # ajouter les liens en diagonal
                for successeur in list(graphe.successors(joueur)):
                    if prédécesseur != successeur and successeur not in joueurs:
                        graphe.add_edge(prédécesseur, successeur)

    # ajouter les noeuds objectifs des deux joueurs
    for x in range(1, 10):
        graphe.add_edge((x, 9), 'B1')
        graphe.add_edge((x, 1), 'B2')
    return graphe
    %matplotlib inline
    import matplotlib.pyplot as plt


positions = {'B1': (5, 10), 'B2': (5, 0)}
colors = {
    'B1': 'red', 'B2': 'green', 
    tuple(état['joueurs'][0]['pos']): 'red', 
    tuple(état['joueurs'][1]['pos']): 'green',
}
sizes = {
    tuple(état['joueurs'][0]['pos']): 300, 
    tuple(état['joueurs'][1]['pos']): 300
}

nx.draw(
    graphe, 
    pos={node: positions.get(node, node) for node in graphe},
    node_size=[sizes.get(node, 100) for node in graphe],
    node_color=[colors.get(node, 'gray') for node in graphe],
)
plt.show()
list(graphe.successors((5,6)))
nx.has_path(graphe, (5,6), 'B1')
nx.shortest_path(graphe, (5,6), 'B1')








    