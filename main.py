from cards import Cards
from deck import Deck
from player import Player
from dealer import Dealer

d = Deck(Cards())
d.shuffle_deck()
dealer = Dealer()
print(dealer)
bankroll = int(input('Enter amount in the bankroll: '))
player1 = Player(bankroll)
print(player1)

while player1.bankroll > 0:
    balance = player1.bankroll
    if player1.place_bet() <= balance:
        print(f'You bet ${player1.bet}.00. You have ${player1.bankroll}.00 in your bankroll.')

        dealer.new_hand(d.deal_cards(2))
        dealer.show_one_card()

        player1.new_hand(d.deal_cards(2))
        player1.show_hand()

        # player1 turn
        while player1.action() != 'stay':
            player1.update_hand(d.deal_cards(1))
            player1.show_hand()
            if player1.is_bust():
                print(f'You have busted! You lose your ${player1.bet}.00 bet. You now have ${player1.bankroll}.00 in your bankroll.')
                break

        # dealer turn
        dealer.show_hand()
        while True:
            if dealer.total_hand() < 16:
                dealer.update_hand(d.deal_cards(1))
                dealer.show_last_card()
            elif dealer.total_hand() > 21:
                player1.win()
                break
            else:
                break

        if player1.total_hand() <= 21 and dealer.total_hand() <= 21:
            if player1.total_hand() > dealer.total_hand():
                player1.win()
            elif player1.total_hand() == dealer.total_hand():
                player1.draw()
            else:
                print(f'Dealer wins! You lose your ${player1.bet}.00 bet. You now have ${player1.bankroll}.00 in your bankroll.')

print('\nGAME OVER!\nThank you for playing Black Jack!')
