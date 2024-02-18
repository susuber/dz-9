import unittest
from moduls.classes import Card, Game


class TestCard(unittest.TestCase):
    def test_init(self):
        card = Card(name='Maxim')
        self.assertEqual(card.name, 'Maxim')

    def test_str(self):
        card = Card(name="Maxim")
        delimiter = '--------------------------'
        card_str = str(card)
        self.assertEqual(card_str.count(delimiter), 2)

    def test_closed(self):
        card = Card("Maxim")
        self.assertFalse(card.closed())


class TestGame(unittest.TestCase):
    def test_check_gamer(self):
        game = Game(users=0, comps=2)
        self.assertTrue(game.check_gamer())

    def test_winner(self):
        game = Game(users=0, comps=2)
        self.assertListEqual(game.winners, [])

    def test_loss(self):
        game = Game(users=0, comps=2)
        self.assertListEqual(game.lose, [])


if __name__ == '__main__':
    unittest.main()
