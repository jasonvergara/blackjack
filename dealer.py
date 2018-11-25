from player import Player


class Dealer(Player):
    def __init__(self):
        super().__init__()

    def __repr__(self):
        return f'Hi! I am your dealer! Welcome to Blackjack!'

    def show_one_card(self):
        print("\nDealer's Card:")
        print("***** of *****")
        face, suit = self.hand[1]
        print(f'{face} of {suit}')

    def show_hand(self):
        print('\nDealer hand:')
        for (face, suit) in self.hand:
            print(f'{face} of {suit}')

    def show_last_card(self):
        face, suit = self.hand[-1]
        print(f'{face} of {suit}')
