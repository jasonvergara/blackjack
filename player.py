from cards import Cards


class Player():
    def __init__(self, bankroll=20):
        self.bankroll = bankroll
        self.hand = []
        self.bet = 0

    def __repr__(self):
        return f'Welcome! You now have ${self.bankroll}.00 in your bankroll.'

    def place_bet(self):
        self.bet = int(input("Place bet: "))
        if self.bet > self.bankroll:
            print("Insufficient funds!")
            return 0
        self.bankroll -= self.bet
        return self.bet

    def new_hand(self, cards):
        self.hand = cards

    def show_hand(self):
        print('\nPlayer hand:')
        for (face, suit) in self.hand:
            print(f'{face} of {suit}')

    def action(self):
        choice = ''
        while choice not in ['hit', 'stay']:
            choice = input("Hit or Stay? ").lower()
        return choice

    def update_hand(self, card):
        self.hand.append(card[0])

    def total_hand(self):
        c = Cards()
        sum = 0
        faces = [face for (face, suit) in self.hand]
        for face in faces:
            sum += c.values[face]
        if 'Ace' in faces and sum < 12:
            sum += 10
        return sum

    def win(self):
        self.bankroll += 2 * self.bet
        print(f'You win ${2 * self.bet}.00. You now have ${self.bankroll}.00 in your bankroll.')

    def is_bust(self):
        if self.total_hand() > 21:
            return True
        return False

    def draw(self):
        self.bankroll += self.bet
        print(f'Draw! You receive ${self.bet}.00 back. You now have ${self.bankroll}.00 in your bankroll.')
