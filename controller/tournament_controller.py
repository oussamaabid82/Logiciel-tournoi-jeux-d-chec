from tinydb import TinyDB
from view.tournament_view import TournamentView
from models.tournament_model import TournamentModels
from view.description_view import DescriptionView


class TournamentContoller:
    def __init__(self, players="", round="", matchs=""):
        self.round = round
        self.matchs = matchs
        self.players = players
        self.tournament = TournamentModels()
        self.tournament_view = TournamentView()
        self.descriptions = DescriptionView()

    def startTournament(self):
        """Affiche le debut du tournoi"""
        answer = self.tournament_view.showstartMenu()
        return answer

    def creationTournement(self):
        """Insialisation d'un tournoi"""
        list = self.tournament_view.initializationOfATournament()
        self.tournament.nom = list[0]
        self.tournament.lieu = list[1]
        self.tournament.date_debut = list[2]
        self.tournament.date_fin = list[3]

    def chooseRaportMenu(self):
        """Affichage du menu de"""
        answer = self.tournament_view.showRaportMenu()
        return answer

    def showStartTournament(self):
        """Veuillez saisir les données suivantes"""
        self.tournament_view.tournamenMessage()

    def createList(self):
        """Importation des liste"""
        self.tournament.players_list = self.players
        self.tournament.tours_list = self.round
        self.tournament.match_list = self.matchs

    def tournamentDescriptionsController(self):
        description = self.descriptions.showDescription()
        self.tournament.tournamentDescriptionsModel(description)

    def save(self):
        db = TinyDB("save/db.json")
        tournament_table = db.table("Tournament")
        tournament_table.insert(self.tournament.serialization_tournoi())
        return tournament_table

    def getTournament(self):
        """Affiche tous les tournoi créer"""
        db = TinyDB("save/db.json")
        tournament_table = db.table("Tournament")
        self.tournament_view.titelTournamentRaport()
        n = 0
        for i in tournament_table:
            n += 1
            self.tournament_view.showTournamentList(n, i["nom"])

    def listTournamentWitnNumbers(self):
        """Affiche la liste des tounois numéroter"""
        number_tournament = []
        list_of_tournament = []
        db = TinyDB("save/db.json")
        tournament_table = db.table("Tournament")
        [number_tournament.append(number + 1) for number in range(len(tournament_table))]
        [list_of_tournament.append(tournament["nom"]) for tournament in tournament_table]
        liste = tuple(zip(number_tournament, list_of_tournament))
        return liste

    def getPlayersInTournamentAlphbetical(self):
        """Afficher la liste des joueurs dans un tournoi choisi"""
        name_list = []
        db = TinyDB("save/db.json")
        tournament_table = db.table("Tournament")
        for i in self.listTournamentWitnNumbers():
            self.tournament_view.showListTournamentWithNumber(i[0], i[1])
        number = self.tournament_view.chooseNumberOfTournament()
        result = (tournament_table.get(doc_id=number))["list des joueurs"]
        for i in result:
            name_list.append((i[0], i[1]))
        list = name_list
        list_sort = (sorted(list, key=lambda list: list))
        self.tournament_view.titelPlayerSortedInTournament()
        n = 0
        for player in list_sort:
            n += 1
            self.tournament_view.showPlayerName(n, player[0], player[1])

    def getRound(self):
        """Afficher la liste des tours d'un tournoi choisi"""
        db = TinyDB("save/db.json")
        tournament_table = db.table("Tournament")
        self.tournament_view.messageRoundsInTournament()
        for i in self.listTournamentWitnNumbers():
            self.tournament_view.showListTournamentWithNumber(i[0], i[1])
        number = self.tournament_view.chooseNumberOfTournament()
        result = (tournament_table.get(doc_id=number))["liste des tours"]
        self.tournament_view.titelRoundsRaport()
        for round in result:
            self.tournament_view.show(round)

    def getMatchs(self):
        """Afficher la liste des match d'un tournoi choisi"""
        number_match = []
        list_of_tournament = []
        db = TinyDB("save/db.json")
        tournament_table = db.table("Tournament")
        [number_match.append(number + 1) for number in range(len(tournament_table))]
        [list_of_tournament.append(tournament["nom"]) for tournament in tournament_table]
        liste = tuple(zip(number_match, list_of_tournament))
        self.tournament_view.messageMatchInTournament()
        for i in liste:
            self.tournament_view.showListTournamentWithNumber(i[0], i[1])
        number = self.tournament_view.chooseNumberOfTournament()
        result = (tournament_table.get(doc_id=number))["liste des matchs"]
        self.tournament_view.messageMatchList()
        for i in result:
            self.tournament_view.showMatch(i[0], i[1])

    def showEndTournament(self):
        self.tournament_view.endView()
