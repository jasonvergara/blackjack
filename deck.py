from random import shuffle


class Deck():
    def __init__(self, Cards):
        self.deck = [(face, suit) for suit in Cards.suits for face in Cards.faces]

    def __repr__(self):
        return f'{len(self.deck)} cards in deck.'

    def print_deck(self):
        for (face, suit) in self.deck:
            print(f'{face} of {suit}')

    def shuffle_deck(self):
        shuffle(self.deck)

    def deal_cards(self, num):
        dealt = []
        if num > len(self.deck) or len(self.deck) == 0:
            raise Exception("Insufficient card in deck.")
        for i in range(num):
            dealt.append(self.deck.pop())
        return dealt
