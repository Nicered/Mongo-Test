from client import client

class MFlixSampleModel:
    def __init__(self):
        db = client["mflixTest"]
        self.movies = db.movies
        self.comments = db.comments
        self.sessions = db.sessions
        self.theaters = db.theaters
        self.users = db.users