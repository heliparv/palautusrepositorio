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
            score = self.score_equal()

        elif max(self.player1_score, self.player2_score) >= 4:
            if self.player1_score > self.player2_score:
                self.scores_high("player1")
            else:
                self.scores_high("player2")
            
        else:
            for i in range(1, 3):
                if i == 1:
                    temp_score = self.player1_score
                else:
                    score = score + "-"
                    temp_score = self.player2_score

                if temp_score == 0:
                    score = score + "Love"
                elif temp_score == 1:
                    score = score + "Fifteen"
                elif temp_score == 2:
                    score = score + "Thirty"
                elif temp_score == 3:
                    score = score + "Forty"

        return score

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
