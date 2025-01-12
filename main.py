from Game import Game

if __name__ == '__main__':
    game = Game()
    card = game.deal()
    print(card.rank.name, card.suit.name)
