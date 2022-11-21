from player import Player
import requests

class PlayerReader:
    def __init__(self, url):
        self.players = []
        self.get_players(url)
    
    def get_players(self, url):
        response = requests.get(url).json()
        for player_dict in response:
            player = Player(
                player_dict['name'], player_dict['nationality'], player_dict['team'], player_dict['goals'], player_dict['assists']
            )
            self.players.append(player)