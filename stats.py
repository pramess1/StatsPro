class Person():
    score = 0
    round_scores = []
    
    def get_score(self):
        return score

    def add_to_score(self, addend):
        round_scores += 1
        return score += addend

    def get_average(self):
        total = 0
        for score in round_scores:
            total += score
        return total

    def subtract_score(self, score_index):
        score_index = raw_input("Which round's score do you want to delete?")
        score_index -= 1
        if round_scores[score_index] != "undefined"
            print "Please pick a score from an already inputted round."
            return subtract_score(score_index)
        else
            del round_scores[score_index]
            print "Round " + (score_index + 1) "'s score has been deleted."
            return
