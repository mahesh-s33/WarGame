from model.Card import Card

class Player:
    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def displayCards(self):
        for card in self.all_cards:
            print(card)
        print(f'Total cards in hand: {len(self.all_cards)}')

    def removeCard(self):
        self.all_cards.pop(0)

    def addCards(self, cards):
        if self.all_cards:
            self.all_cards.extend(cards)
        else:
            self.all_cards = cards