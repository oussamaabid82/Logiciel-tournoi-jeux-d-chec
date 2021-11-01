from tinydb import TinyDB
from controller.tour_controller import TourController
from models.match_model import MatchModel
from models.tour_model import TourModel, match_list
from view.match_view import MatchView



class ControllerMatch:
    def __init__(self):
        pass
    
    def save(self):
        db = TinyDB("db.json")
        table_match = db.table("joueurs")
        table_match.truncate()
        table_match.insert_multiple(self.serialisation_match)
        return table_match