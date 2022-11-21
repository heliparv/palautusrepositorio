from player import Player
from operator import attrgetter
from playerreader import PlayerReader

class PlayerStats:
    def __init__(self, reader: PlayerReader):
        self.players = reader.players
    
    def top_scorers_by_nationality(self, nationality):
        print(f'Players from {nationality} in descending order by points')
        subgroup = []
        for player in self.players:
            if player.nationality == 'FIN':
                subgroup.append(player)
        subgroup = sorted(subgroup, key=attrgetter('points'), reverse=True)
        return subgroup