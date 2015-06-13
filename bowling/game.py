import itertools

from .round import Round
from .round import FinalRound


class Game(object):
    def __init__(self, round_num):
        self.rounds = [Round() for _ in range(round_num - 1)]
        self.rounds.append(FinalRound())

    def score(self):

        hits = list(itertools.chain(*(map(lambda r: r.hits, self.rounds))))

        def calc_score_new(hs):
            return hs[0].score + sum(
                map(lambda h: h.score, hs[1:1 + hs[0].count_next]))

        return sum([calc_score_new(hs) for hs in
                    itertools.zip_longest(hits, hits[1:], hits[2:])], 0)
