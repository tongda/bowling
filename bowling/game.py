from functools import reduce
import itertools

from .round import Round
from .round import FinalRound


class Game(object):
    def __init__(self, round_num):
        self.rounds = list(map(lambda _: Round(), range(round_num - 1)))
        self.rounds.append(FinalRound())

    def score(self):

        hits = list(itertools.chain(*(map(lambda r: r.hits, self.rounds))))

        def calc_score(hs):
            return hs[0].score + sum(
                map(lambda h: h.score, hs[1:1 + hs[0].count_next]))

        return reduce(lambda total, hs: total + calc_score(hs),
                      itertools.zip_longest(hits, hits[1:], hits[2:]),
                      0)
