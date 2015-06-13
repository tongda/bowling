from bowling.game import Game
import unittest

class GameTestCase(unittest.TestCase):

    def setUp(self):
        self.game = Game(10)

    def test__non_start_game_should_have_score_0(self):
        self.assertEqual(0, self.game.score())

    def test__after_some_rounds_should_have_scores(self):
        self.game.rounds[0].hit(5)
        self.game.rounds[0].hit(3)

        self.game.rounds[1].hit(4)
        self.game.rounds[1].hit(2)

        self.assertEqual(14, self.game.score())

    def test__one_strike(self):
        self.game.rounds[0].hit(10)

        self.game.rounds[1].hit(4)
        self.game.rounds[1].hit(2)

        self.assertEqual(22, self.game.score())

    def test__double_strike(self):
        self.game.rounds[0].hit(10)

        self.game.rounds[1].hit(10)

        self.game.rounds[2].hit(5)
        self.game.rounds[2].hit(3)

        self.assertEqual(51, self.game.score())

    def test__one_spare(self):
        self.game.rounds[0].hit(5)
        self.game.rounds[0].hit(5)

        self.game.rounds[1].hit(5)
        self.game.rounds[1].hit(4)

        self.assertEqual(24, self.game.score())

    def test__double_spare(self):
        self.game.rounds[0].hit(5)
        self.game.rounds[0].hit(5)

        self.game.rounds[1].hit(5)
        self.game.rounds[1].hit(5)

        self.game.rounds[2].hit(6)
        self.game.rounds[2].hit(3)

        self.assertEqual(40, self.game.score())

    def test__one_strike_and_one_spare(self):
        self.game.rounds[0].hit(10)

        self.game.rounds[1].hit(5)
        self.game.rounds[1].hit(5)

        self.game.rounds[2].hit(6)
        self.game.rounds[2].hit(3)

        self.assertEqual(45, self.game.score())

    def test__one_spare_and_one_strike(self):
        self.game.rounds[0].hit(5)
        self.game.rounds[0].hit(5)

        self.game.rounds[1].hit(10)

        self.game.rounds[2].hit(6)
        self.game.rounds[2].hit(3)

        self.assertEqual(48, self.game.score())

    def test__all_strikes(self):
        for round in self.game.rounds[:-1]:
            round.hit(10)

        self.game.rounds[-1].hit(10)
        self.game.rounds[-1].hit(10)
        self.game.rounds[-1].hit(10)

        self.assertEqual(300, self.game.score())

    def test__sample(self):
        self.game.rounds[0].hit(1)
        self.game.rounds[0].hit(4)
        self.game.rounds[1].hit(4)
        self.game.rounds[1].hit(5)
        self.game.rounds[2].hit(6)
        self.game.rounds[2].hit(4)
        self.game.rounds[3].hit(5)
        self.game.rounds[3].hit(5)
        self.game.rounds[4].hit(10)
        self.game.rounds[5].hit(0)
        self.game.rounds[5].hit(1)
        self.game.rounds[6].hit(7)
        self.game.rounds[6].hit(3)
        self.game.rounds[7].hit(6)
        self.game.rounds[7].hit(4)
        self.game.rounds[8].hit(10)
        self.game.rounds[9].hit(2)
        self.game.rounds[9].hit(8)
        self.game.rounds[9].hit(6)

        self.assertEqual(133, self.game.score())

