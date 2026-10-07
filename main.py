"""
Nom: Damien Thibodeau
Groupe: 4-1234
Projet: Combat de monsstres; faire combattre des monstres virtuels à l'utilisateur
"""
import random
Jouer = True


def choix_nom_monstres():
    liste_noms = ["Ogre","Dragon","Vampire","Loup-garou","Minotaure","Cyclope","Troll","Kraken","Basilic","Griffon", "Ornythorinque"]
    liste_adjectifs = [" Féroce"," Terrifiant"," Sombre"," Cruel"," Implacable"," Monstrueux"," Sauvage"," Mystique"," Ancien"," Redoutable", " sociopathe"]
    nom_complet = liste_noms[random.randint(1,10)] + liste_adjectifs[random.randint(1,10)]
    return nom_complet

def choix_difficultee():
    reponse = input (" Voulez-vous faire cette grotte dans une difficultée: (1) - Façile, (2) - Normale ou (3) - Diffiçile : ")
    if reponse == "1":
        return 1
    elif reponse == "2":
        return 2
    elif reponse == "3":
        return 3
    else:
        print(" Vous n'avez pas entré une réponse valide. Réessayez")
        return choix_difficultee()

while Jouer:
    print("\u001b[0;92m Bonjour cher aventurier! Dans ce jeu, tu devras parcourir une grotte effrayante dans le but de trouver un trésor. Bonne chance!")

    vie_joueur = 100
    attaque_joueur = random.randint(15,50)
    tour = 0
    difficultee = choix_difficultee()
    min_vie_monstres = difficultee * 5
    max_vie_monstres = difficultee * 35
    min_attaque_monstres = difficultee * 5
    max_attaque_monstre = difficultee * 15
    tour_max = difficultee * random.randint(2,10)

    while vie_joueur > 0 and tour < tour_max :
        nom_monstre = choix_nom_monstres()
        vie_monstre = random.randint(min_vie_monstres,max_vie_monstres)
        attaque_monstre = random.randint(min_attaque_monstres, max_attaque_monstre)

        print(f"\u001b[0;94m Tour #{tour + 1}. Points de vie: {vie_joueur}. Attaque: {attaque_joueur}")
        print(f"\u001b[0;91m Oh non! tu tombes sur un {nom_monstre} il fait {attaque_monstre} dégats/manche et a {vie_monstre} pvs")
        choix = input(f"\u001b[0;90m Veux tu (1)- Fuir, tu perderas {attaque_monstre/2} pvs ou (2)- combattre ")
        if choix == "1":
            if vie_joueur - (attaque_monstre/2) > 0:
                vie_joueur -= (attaque_monstre/2)
                tour += 1
            else:
                print("\u001b[1;91m ZUT! il semble qu'il ne vous reste plus de pvs!")
                print(f"\u001b[1;96m Score final: {tour} tours réussis.")
                vie_joueur -= (attaque_monstre / 2)

        elif choix == "2":

            while vie_joueur > 0:
                if (vie_monstre - attaque_joueur) > 0:
                    vie_monstre -= attaque_joueur
                    print(f"\u001b[0;93m Vous attaquez le {nom_monstre}! Il lui reste {vie_monstre} pvs")

                    if (vie_joueur - attaque_monstre) > 0:
                        vie_joueur -= attaque_monstre
                        print(f"\u001b[1;93m La créature vous attaque! Il vous reste {vie_joueur} pvs")

                    else:
                        print(f"\u001b[1;93m La créature vous attaque!")
                        print("\u001b[1;91m ZUT! il semble qu'il ne vous reste plus de pvs!")
                        print(f"\u001b[1;96m Score final: {tour} tours réussis.")
                        break

                else:
                    print(f"\u001b[0;93m Vous attaquez le {nom_monstre}!")
                    print(f"\u001b[1;32m Vous avez vaincu le monstre!")
                    break

            attaque_joueur += tour
            tour += 1
            print("\n" * 2)

    if vie_joueur > 0:
        print("\u001b[1;36m FÉLICITATIONS! Vous avez réussis à vous rendre au bout de cette grotte!")
    rejouer = input("\u001b[1;36m Voulez-vous recommencer? (1)-Oui, (2)-Non")

    if rejouer == "1":
        Jouer = True
        print("\n" * 20)
    else:
        print(" Au revoir!")
        Jouer = False