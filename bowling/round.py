
STRIKE = 0
SPARE = 1
COUNT_SELF = 2
NON_START = -1

class Round(object):
    def __init__(self, hit_num=2):
        self.state = NON_START
        self.hit_scores = [0 for _ in range(hit_num)]
        self.hit_times = 0

    @property
    def score(self):
        return sum(self.hit_scores)

    def hit(self, score):
        self.hit_scores[self.hit_times] = score
        if self.hit_times == 0:
            if self.score == 10:
                self.state = STRIKE
            else:
                self.state = COUNT_SELF
        elif self.hit_times == 1 and self.state != STRIKE:
            if self.score == 10:
                self.state = SPARE
            else:
                self.state = COUNT_SELF
        else:
            raise Exception("Invalid")

        self.hit_times += 1


class FinalRound(Round):
    def __init__(self):
        super().__init__(hit_num=3)

    def hit(self, score):
        if self.hit_times == 0:
            self.hit_scores[0] = score
        elif self.hit_times == 1:
            self.hit_scores[1] = score
        elif self.hit_times == 2 and self.score >= 10:
            self.hit_scores[2] = score
        else:
            raise Exception("Invalid")

        self.state = COUNT_SELF
        self.hit_times += 1