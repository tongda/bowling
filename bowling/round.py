from bowling.hit import Hit

STRIKE = 0
SPARE = 1
COUNT_SELF = 2
NON_START = -1

class Round(object):
    def __init__(self, hit_num=2):
        self.state = NON_START
        self.hits = []
        self.hit_scores = [0 for _ in range(hit_num)]
        self.hit_times = 0

    @property
    def score(self):
        return sum(self.hit_scores)

    def hit(self, score):

        if self.hit_times == 0 and score == 10:
            self.hits.append(Hit(score=score, count_next=2))
        elif self.hit_times == 1 and self.hits[0].score + score == 10:
            self.hits.append(Hit(score=score, count_next=1))
        else:
            self.hits.append(Hit(score=score, count_next=0))

        self.hit_times += 1


class FinalRound(Round):
    def __init__(self):
        super().__init__(hit_num=3)

    def hit(self, score):
        if self.hit_times == 0 and score == 10:
            self.hits.append(Hit(score=score, count_next=0))
        elif self.hit_times == 1 and self.hits[0].score + score == 10:
            self.hits.append(Hit(score=score, count_next=0))
        else:
            self.hits.append(Hit(score=score, count_next=0))

        self.state = COUNT_SELF
        self.hit_times += 1