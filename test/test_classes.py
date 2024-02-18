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

class TestGame():
    def test_chek_players(self):
        game = Game(users=0, comps=2)
        assert len(game.chek_players()) == 2

    def test_check_gamer(self):
        game = Game(users=0, comps=2)
        assert game.check_gamer() == True

    def test_winner_and_loss(self):
        game = Game(users=0, comps=2)
        assert game.winners == []
        assert game.lose == []