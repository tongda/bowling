from bowling.hit import Hit

STRIKE = 0
SPARE = 1
COUNT_SELF = 2
NON_START = -1


class Round(object):

    def __init__(self, hit_num=2):
        self.hits = []
        self.hit_times = 0

    @property
    def score(self):
        return sum(map(lambda h: h.score, self.hits), 0)

    def hit(self, score):
        conds = {
            (0, 10): lambda: Hit(score=score, count_next=2),
            (1, 10): lambda: Hit(score=score, count_next=1),
        }

        self.hits.append(
            conds.get((self.hit_times, self.score + score),
                      lambda: Hit(score=score, count_next=0))())

        self.hit_times += 1


class FinalRound(Round):
    def __init__(self):
        super().__init__(hit_num=3)

    def hit(self, score):
        self.hits.append(Hit(score=score, count_next=0))

        self.state = COUNT_SELF
        self.hit_times += 1
