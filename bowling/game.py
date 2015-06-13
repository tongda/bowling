from .round import Round
from .round import FinalRound
from .round import COUNT_SELF
from .round import STRIKE
from .round import SPARE

import itertools


class Game(object):
    def __init__(self, round_num):
        self.rounds = [Round() for _ in range(round_num - 1)]
        self.rounds.append(FinalRound())

    def score(self):
        def calc_score(cur, next1, next2):
            if cur.state == COUNT_SELF:
                return cur.score
            elif cur.state == STRIKE:
                if next1.state == STRIKE:
                    return cur.score + next1.hit_scores[0] + next2.hit_scores[0]
                else:
                    return cur.score + next1.hit_scores[0] + next1.hit_scores[1]
            else:
                return cur.score + next1.hit_scores[0]

        return sum([calc_score(r1, r2, r3) for r1, r2, r3 in
                    itertools.zip_longest(self.rounds,
                                          self.rounds[1:],
                                          self.rounds[2:],
                                          fillvalue=Round())])
