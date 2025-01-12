from Game import Game

if __name__ == '__main__':
    game = Game()
    cards = game.deal()
    game.play()
    # print(cards[0].rank.name, cards[0].suit.name, cards[0].value)
#