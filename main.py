from model.Deck import Deck
from model.Player import Player


def game_on():
    deck = Deck()
    deck.shuffleCards()
    playerOne = Player('Tom')
    playerTwo = Player('Jerry')
    playerOne.addCards(deck.all_cards[:26])
    playerTwo.addCards(deck.all_cards[26:])
    playerOne.displayCards()
    playerTwo.displayCards()
    print("Game On")
    round = 0
    war = []
    while True:
        round += 1
        print(f'Round {round}')
        war.extend([playerOne.all_cards[0], playerTwo.all_cards[0]])
        if playerOne.all_cards[0].value == playerTwo.all_cards[0].value:
            pass
        elif playerOne.all_cards[0].value > playerTwo.all_cards[0].value:
            print(f"Advantage for player {playerOne.name}")
            playerOne.addCards(war)
            war = []
        else:
            print(f"Advantage for player {playerTwo.name}")
            playerTwo.addCards(war)
            war = []
        playerOne.removeCard()
        playerTwo.removeCard()
        print(f"{playerOne.name}: {len(playerOne.all_cards)}, {playerTwo.name}: {len(playerTwo.all_cards)}")
        if len(playerOne.all_cards) == 0:
            print(f"{playerTwo.name} wins!")
            break
        elif len(playerTwo.all_cards) == 0:
            print(f"{playerOne.name} wins!")
            break

if __name__ == '__main__':
    game_on()
