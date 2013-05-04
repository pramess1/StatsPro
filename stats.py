class Person(object):
    """ person object that collects multiple values and a total score """
    
    def __init__(self):
        score = 0
        round_scores = []
    
    def get_score(self):
        """ returns the score """
        return score

    def add_to_score(self, addend):
        """ add new score value """
        # add new score value to list of all score values
        round_scores.append(addend)

        # we should also add the value to the total score
        score += addend

        # return info string
        return "You added " + addend + " to this quizzers score."

    def get_average(self):
        """ calculates the average of all scores """
        total = 0
        for score in round_scores:
            total += score
        return total

    def subtract_score(self, score_index):
        """ deletes a score from all scores """
        score_index = raw_input("Which round's score do you want to delete?")
        score_index -= 1
        if round_scores[score_index] != "undefined":
            print "Please pick a score from an already inputted round."
            return subtract_score(score_index)
        else:
            # remove value from round_scores list and subtract it from total score
            del round_scores[score_index]
            score -= round_scores[score_index]
            print "Round " + (score_index + 1) "'s score has been deleted."
            return
