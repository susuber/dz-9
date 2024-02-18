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

    def test_eq(self):
        card_1 = Card(name='Maxim')
        card_2 = Card(name='Vera')
        self.assertTrue(card_1 == card_2)

    def test_ne(self):
        card_1 = Card(name='Maxim')
        card_2 = Card(name='Vera')
        self.assertFalse(card_1 != card_2)

    def test_lt(self):
        card_1 = Card(name='Maxim')
        card_2 = Card(name='Vera')
        self.assertFalse(card_1 < card_2)

    def test_gt(self):
        card_1 = Card(name='Maxim')
        card_2 = Card(name='Vera')
        self.assertFalse(card_1 > card_2)

    def test_get_numbers_in_card(self):
        card = Card(name='Maxim')
        self.assertEqual(len(card.get_numbers_in_card()), 27)

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

    def test_get_players2(self):
        game = Game(users=0, comps=2)
        players = game.get_players()
        self.assertEqual(players[1], 'Компьютер 1')

    def test_get_players3(self):
        game = Game(users=0, comps=2)
        players = game.get_players()
        self.assertEqual(players[2], 'Компьютер 2')


if __name__ == '__main__':
    unittest.main()
