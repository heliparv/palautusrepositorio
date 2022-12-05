class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0
        self.score_names = {0:"Love", 1:"Fifteen", 2:"Thirty", 3:"Forty"}

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score += 1
        else:
            self.player2_score += 1

    def get_score(self):
        score = ""
        temp_score = 0

        if self.player1_score == self.player2_score:
            return self.score_equal()

        elif max(self.player1_score, self.player2_score) >= 4:
            if self.player1_score > self.player2_score:
                return self.scores_high("player1")
            else:
                return self.scores_high("player2")
            
        else:
            return f"{self.score_names[self.player1_score]}-{self.score_names[self.player2_score]}"

    def score_equal(self):
        if self.player1_score < 3:
            return f"{self.score_names[self.player1_score]}-All"
        else:
            return "Deuce"

    def scores_high(self, player):
        minus_result = abs(self.player1_score - self. player2_score)

        if minus_result == 1:
            return f"Advantage {player}"
        else:
            return f"Win for {player}"
