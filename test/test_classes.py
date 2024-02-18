from moduls.classes import Card, Game


class TestCard():

    def test_init(self):
        card = Card(name='Maxim')
        assert card.name == 'Maxim'

    def test_str(self):
        card = Card(name="Maxim")
        delimiter = '--------------------------'
        card_str = str(card)
        assert card_str.count(delimiter) == 2

    def test_closed(self):
        card = Card("Maxim")
        assert card.closed() == False

    def test_eq(self):
        card_1 = Card(name='Maxim')
        card_2 = Card(name='Vera')
        assert card_1 == card_2

    def test_ne(self):
        card_1 = Card(name='Maxim')
        card_2 = Card(name='Vera')
        assert not card_1 != card_2

    def test_lt(self):
        card_1 = Card(name='Maxim')
        card_2 = Card(name='Vera')
        assert not card_1 < card_2

    def test_gt(self):
        card_1 = Card(name='Maxim')
        card_2 = Card(name='Vera')
        assert not card_1 > card_2

    def test_get_numbers_in_card(self):
        card = Card(name='Maxim')
        assert len(card.get_numbers_in_card()) == 27

class TestGame():
    #def test_check_players(self):
     #   game = Game(users=0, comps=2)
      #  assert len(game.check_players()) == 2

    def test_check_gamer(self):
        game = Game(users=0, comps=2)
        assert game.check_gamer() == True

    def test_winner_and_loss(self):
        game = Game(users=0, comps=2)
        assert game.winners == []
        assert game.lose == []

    def test_get_players2(self):
        game = Game(users=0, comps=2)
        players = game.get_players()
        assert players[1] == 'Компьютер 1'

    def test_get_players3(self):
        game = Game(users=0, comps=2)
        players = game.get_players()
        assert players[2] == 'Компьютер 2'
