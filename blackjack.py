from random import choice

class Card:
    """This models a single card"""
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit 

    def describe_card(self):
        print(f"The {self.rank} of {self.suit}")

class Deck:
    """Models and constructs a shuffled deck of 52 cards"""
    def __init__(self):
        suits = ['Diamonds', 'Hearts', 'Clubs', 'Spades']
        ranks = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
        self.unshuffled_cards = []
        self.shuffled_cards = [] 

        for suit in suits:
            for rank in ranks:
                self.unshuffled_cards.append(Card(rank, suit)) 

        while self.unshuffled_cards:
            shuffle = choice(self.unshuffled_cards)
            self.shuffled_cards.append(shuffle)
            self.unshuffled_cards.remove(shuffle)
    
    def deal_cards(self):
        card = self.shuffled_cards.pop()
        return card
        
class Hand:
    """Models and constructs the hand of the dealer and player"""
    def __init__(self):
        self.hand = []
        
    def add_card(self, card):
        self.hand.append(card)

    def totaling_hand(self):
        score = {
            'Two' : 2,
            'Three' : 3,
            'Four' : 4,
            'Five' : 5,
            'Six' : 6,
            'Seven' : 7,
            'Eight' : 8,
            'Nine' : 9,
            'Ten' : 10,
            'Jack' : 10,
            'Queen' : 10,
            'King' : 10,
            'Ace' : 11 
        }

        self.total = 0
        ace = 0
        for card in self.hand:
            self.total += score[card.rank]
            if card.rank == 'Ace':
                ace += 1
        while self.total > 21 and ace > 0:
            self.total = self.total - 10
            ace -= 1
        
        return self.total

def player_starting_hand(player, deck):
"""This function constructs the player's starting hand"""
    print("\nPlayer Hand")
    while len(player.hand) < 2:
        player.add_card(deck.deal_cards())
    for card in player.hand:
        card.describe_card()
    
    print("\nPlayer Total:")
    print(player.totaling_hand())

def hand_handling(hand, deck):
    """Function adds and displays cards in each deck"""
    hand.add_card(deck.deal_cards())
    for card in hand.hand:
        card.describe_card()

def player_turn(player, deck):
    """Function runs player's hit/stand turn"""
    round_over = False
    answer = get_valid_input("\nDo you want to Hit or Stand? H/S - ", ['H', 'S'])
    while answer == 'H':
        hand_handling(player, deck)
        print("\nPlayer Total:")
        print(player.totaling_hand())
        if player.totaling_hand() > 21:
            round_over = True
            break
        else:
            answer = get_valid_input("\nHit or Stand? H/S - ", ['H', 'S'])
    return round_over

def dealer_turn(dealer, deck):
    print("\nDealer Hand:")
    hand_handling(dealer, deck)

    print("\nDealer Total:")
    print(dealer.totaling_hand())

    while len(dealer.hand) >= 2 and dealer.totaling_hand() < 17:
        print("\nDealer's Hand:")
        hand_handling(dealer, deck)
        print("\nDealer Total:")
        print(dealer.totaling_hand())
    
def round_outcome(player, dealer, pot, bet):
    """Function determines the winner of each round"""
    player_total = player.totaling_hand()
    dealer_total = dealer.totaling_hand()
    player_blackjack = len(player.hand) == 2 and player_total == 21
    dealer_blackjack = len(dealer.hand) == 2 and dealer_total == 21

    if player_blackjack and dealer_blackjack:
        print("\nPush! You both have Blackjack")
    elif player_blackjack:
        print("\nBlackjack!")
        print(f"You win ${bet * 3 // 2}")
        pot += bet * 3 // 2
    elif dealer_blackjack:
        print("\nDealer has Blackjack!")
        print(f"You lost ${bet}")
        pot -= bet
    elif player_total > 21:
        print("\nYou've gone bust!")
        print(f"You lost ${bet}")
        pot -= bet
    elif dealer_total > 21:
        print("\nDealer's gone bust!")
        print(f"You win ${bet}")
        pot += bet
    elif player_total > dealer_total:
        print("\nYou win!")
        print(f"You win ${bet}")
        pot += bet
    elif dealer_total > player_total:
        print("\nDealer wins!")
        print(f"You lost ${bet}")
        pot -= bet
    else:
        print("\nTie!")
    return pot

def get_valid_input(question, valid_answers):
    """Function validates player inputs throughout the game"""
    answer = input(question)
    while answer.upper() not in valid_answers:
        print(f"'{answer}' is an invalid response, try again - ")
        answer = input(question)
    return answer.upper()

def get_valid_bet(pot):
    """This function is used to validate player inputs while betting"""
    while True:
        answer = input(f"\nPlace your bet (Pot = ${pot}): ")
        try:
            bet = int(answer)
        except ValueError:
            print(f"\n'{answer}' is an invalid response, try again")
            continue
        if bet < 1:
            print("\nYou must bet at least $1")
        elif bet > pot:
            print("\nYou can't bet more than your balance")
        else:
            return bet


pot = 10000
answer = get_valid_input("Would you like to play? Y/N - ", ['Y', 'N'])

while answer == 'Y':
    deck = Deck()
    player = Hand()
    dealer = Hand()
    round_over = False

    bet = get_valid_bet(pot)

    #Player Hand Set-Up#
    player_starting_hand(player, deck)

    #Dealer Hand Set-Up#        
    dealer_turn(dealer, deck)
    if player.totaling_hand() == 21:
        dealer_turn(dealer, deck)
        round_over = True

    if not round_over:
        print("\n--Player's Turn--")
        round_over = player_turn(player, deck)

    if not round_over:
        print("\n--Dealer's Turn--")
        dealer_turn(dealer, deck)
                    

    pot = round_outcome(player, dealer, pot, bet)
    if pot <= 0:
        print("\nThere's no more money in your pot!")
        answer = 'N'
    else:
        answer = get_valid_input("\nWould you like to continue? Y/N - ", ['Y', 'N'])

print("\n--Cashing Out--")
print(f"\nYou've cashed out ${pot}. Thank you for playing!")
