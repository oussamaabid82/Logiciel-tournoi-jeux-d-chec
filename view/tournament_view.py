

class TournamentView:

    def __init__(self):
        pass

    def startView(self):
        print("\n---------------* B I E N V E N U E *---------------\n")
        print("[1] - Creez un nouveau tournoi")
        print("[2] - Rapports")
        print("[3] - Quitter")
        answer = int(input("Saisissez votre choix: "))
        return answer

    def tournamentStar(self):
        print("\nVeuillez saisir les données suivantes\n")

    def tournamentCreation(self):
        answer = input("Nom du tournoi: "), input("Lieu: "), input("Date de debut: "), input("Date de la fin: ")
        return answer

    def startMessage(self, nom):
        """Afficher à l'utilisateur le debut du tournoi"""
        print(f"\nTournoi {nom} à commencer\n")
    
    def showMatch(self, player1, player2):
        print(f"{player1} Vs {player2}")

    def endMessage(self):
        """Afficher à l'utilisateur la fin du tournoi"""
        print("Fin du tournoi")

    def chooseNumberInMenu(self):
        print("\n***** R A P P O R T *****\n")
        print("1- Liste de tous les joueurs")
        print("2- Liste de tous les tournois")
        print("3- Liste de tous les tours")
        print("4- Liste de tous les matchs")
        answer = input("\nSaisissez le numero de la liste que vous voulez afficher: ")
        return int(answer)
    
    def playerList(self):
        print("\nAfficher la liste des joueurs:\n")
        print(" 1: Par ordre Alphabetique")
        print(" 2: Par classement\n")
        answer = input("Saisissez 1 ou 2: \n")
        return int(answer)

    def messaageTournamentRaport(self):
        print("\n***** Liste des tournois *****\n")

    def showTournamentList(self, tournament_list):
        print(f" * {tournament_list}")

    def showRoundList(self, list):
        print(list)

    def messageMatchList(self):
        print("\n***** Liste des matchs *****")

    def endView(self):
        print("\n-----------------* A LA PROCHAINE *-----------------")

    """def show(self, player):
        print(player)"""
