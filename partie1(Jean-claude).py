import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, ArrowStyle
import numpy as np

class GrapheOriente:
    def __init__(self):
        self.G = nx.DiGraph()
        self.types_noeuds_possibles = [
            "VILLE", "VOYAGEUR", "CHAUFFEUR", "FOURNISSEUR", "RECEPTEUR",
            "PRODUIT", "COMPAGNIE DE TRANSPORT", "BUS", "DEPOT", "LIEU"
        ]
        self.relations_possibles = [
            "EST_SITUE_A", "APPARTIENT_A", "EST_LIE", "FOURNIT", "EST_RECU_PAR",
            "EST_STOCKE_DANS", "VOYAGE_AVEC", "HABITE_A", "CONDUIT"
        ]
        
    def creer_graphe_personnalise(self):
        print("\n" + "═"*50)
        print("Création d'un graphe personnalisé".center(50))
        print("═"*50)
        
        nb_noeuds = int(input("\nCombien de nœuds voulez-vous ajouter dans votre graphe ? : "))
        types_noeuds = {}
        
        for i in range(nb_noeuds):
            nom = input(f"\nNom du nœud {i+1}/{nb_noeuds}: ")
            print("\nTypes de nœuds disponibles :")
            for idx, type_noeud in enumerate(self.types_noeuds_possibles):
                print(f"  {idx+1}. {type_noeud}")
            choix_type = int(input("→ Sélectionnez l'indice du type : "))
            while not 1 <= choix_type <= len(self.types_noeuds_possibles):
                print("Indice invalide.")
                choix_type = int(input("→ Sélectionnez l'indice du type : "))
            type_noeud = self.types_noeuds_possibles[choix_type - 1]
            self.G.add_node(nom, type=type_noeud)
            if type_noeud not in types_noeuds:
                types_noeuds[type_noeud] = []
            types_noeuds[type_noeud].append(nom)
        
        nb_relations = int(input("\nCombien de relations voulez-vous ajouter ? "))
        for i in range(nb_relations):
            print("\n" + "-"*30)
            print(f"Relation {i+1}/{nb_relations}")
            print("-"*30)
            print("\nNœuds disponibles par type :")
            for type_noeud, noms in types_noeuds.items():
                print(f"\n{type_noeud}:")
                for idx, nom in enumerate(noms):
                    print(f"  {idx+1}. {nom}")
            print("\nSélection du nœud source :")
            tous_noeuds = list(self.G.nodes())
            for idx, noeud in enumerate(tous_noeuds):
                type_noeud = self.G.nodes[noeud]['type']
                print(f"  {idx+1}. {noeud} ({type_noeud})")
            choix_source = int(input("→ Sélectionnez l'indice du nœud source : "))
            while not 1 <= choix_source <= len(tous_noeuds):
                print("Indice invalide.")
                choix_source = int(input("→ Sélectionnez l'indice du nœud source : "))
            source = tous_noeuds[choix_source - 1]
            print("\nSélection du nœud cible :")
            for idx, noeud in enumerate(tous_noeuds):
                type_noeud = self.G.nodes[noeud]['type']
                print(f"  {idx+1}. {noeud} ({type_noeud})")
            choix_cible = int(input("→ Sélectionnez l'indice du nœud cible : "))
            while not 1 <= choix_cible <= len(tous_noeuds):
                print("Indice invalide.")
                choix_cible = int(input("→ Sélectionnez l'indice du nœud cible : "))
            cible = tous_noeuds[choix_cible - 1]
            print("\nTypes de relation disponibles :")
            for idx, rel in enumerate(self.relations_possibles):
                print(f"  {idx+1}. {rel}")
            choix_relation = int(input("→ Sélectionnez l'indice de la relation : "))
            while not 1 <= choix_relation <= len(self.relations_possibles):
                print("Indice invalide.")
                choix_relation = int(input("→ Sélectionnez l'indice de la relation : "))
            relation = self.relations_possibles[choix_relation - 1]
            self.G.add_edge(source, cible, label=relation)