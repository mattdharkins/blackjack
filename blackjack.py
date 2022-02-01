

class Blackjack():
    def __init__(self):
        self.cards = {'Cards': {'2 of Clubs': 2, '3 of Clubs': 3, '4 of Clubs':4, '5 of Clubs': 5, '6 of Clubs': 6, 
            '7 of Clubs': 7 ,'8 of Clubs': 8, '9 of Clubs': 9, '10 of Clubs': 10, 'Jack of Clubs':10, 'Queen of Clubs': 10, 
            'King of Clubs': 10, 'Ace of Clubs': 11, '2 of Diamonds': 2, '3 of Diamonds': 3, '4 of Diamonds':4, 
            '5 of Diamonds': 5, '6 of Diamonds': 6, '7 of Diamonds': 7 ,'8 of Diamonds': 8, '9 of Diamonds': 9, '10 of Diamonds': 10, 
            'Jack of Diamonds':10, 'Queen of Diamonds': 10, 'King of Diamonds': 10, 'Ace of Diamonds': 11,'2 of Hearts': 2, 
            '3 of Hearts': 3, '4 of Hearts':4, '5 of Hearts': 5, '6 of Hearts': 6, '7 of Hearts': 7 ,'8 of Hearts': 8, '9 of Hearts': 9,
            '10 of Hearts': 10, 'Jack of Hearts':10, 'Queen of Hearts': 10, 'King of Hearts': 10, 'Ace of Hearts': 11, '2 of Spades': 2, 
            '3 of Spades': 3, '4 of Spades':4, '5 of Spades': 5, '6 of Spades': 6, '7 of Spades': 7 ,'8 of Spades': 8, '9 of Spades': 9, 
            '10 of Spades': 10, 'Jack of Spades':10, 'Queen of Spades': 10, 'King of Spades': 10, 'Ace of Spades': 11}}
            
        self.deck = ['2 of Clubs', '3 of Clubs', '4 of Clubs', '5 of Clubs', '6 of Clubs', '7 of Clubs','8 of Clubs', '9 of Clubs', 
            '10 of Clubs', 'Jack of Clubs', 'Queen of Clubs', 'King of Clubs', 'Ace of Clubs', '2 of Diamonds', '3 of Diamonds', 
            '4 of Diamonds', '5 of Diamonds', '6 of Diamonds', '7 of Diamonds','8 of Diamonds', '9 of Diamonds', '10 of Diamonds', 
            'Jack of Diamonds', 'Queen of Diamonds', 'King of Diamonds', 'Ace of Diamonds','2 of Hearts', '3 of Hearts', '4 of Hearts', 
            '5 of Hearts', '6 of Hearts', '7 of Hearts','8 of Hearts', '9 of Hearts','10 of Hearts', 'Jack of Hearts', 'Queen of Hearts', 
            'King of Hearts', 'Ace of Hearts', '2 of Spades', '3 of Spades', '4 of Spades', '5 of Spades', '6 of Spades', '7 of Spades',
            '8 of Spades', '9 of Spades', '10 of Spades', 'Jack of Spades', 'Queen of Spades', 'King of Spades', 'Ace of Spades']

        self.player_hand = []
        self.player_total = 0
        self.dealer_hand = []
        self.dealer_total = 0
        self.wins = 0
        self.losses = 0
        self.wallet = 0
        self.winnings = 0
        self.bet = 0
        self.possible_winnings = 0
        self.double_down = 0
        self.ace_tracker_player = 0
        self.ace_tracker_dealer = 0
        self.stand = 0
        self.ace_tracker_player_midgame = 0
        self.ace_tracker_dealer_midgame = 0
        

    def shuffle_deck(self):
        import random
        random.shuffle(self.deck)
        

    def collect_cards(self):
        self.deck = ['2 of Clubs', '3 of Clubs', '4 of Clubs', '5 of Clubs', '6 of Clubs', '7 of Clubs','8 of Clubs', '9 of Clubs', 
            '10 of Clubs', 'Jack of Clubs', 'Queen of Clubs', 'King of Clubs', 'Ace of Clubs', '2 of Diamonds', '3 of Diamonds', 
            '4 of Diamonds', '5 of Diamonds', '6 of Diamonds', '7 of Diamonds','8 of Diamonds', '9 of Diamonds', '10 of Diamonds', 
            'Jack of Diamonds', 'Queen of Diamonds', 'King of Diamonds', 'Ace of Diamonds','2 of Hearts', '3 of Hearts', '4 of Hearts', 
            '5 of Hearts', '6 of Hearts', '7 of Hearts','8 of Hearts', '9 of Hearts','10 of Hearts', 'Jack of Hearts', 'Queen of Hearts', 
            'King of Hearts', 'Ace of Hearts', '2 of Spades', '3 of Spades', '4 of Spades', '5 of Spades', '6 of Spades', '7 of Spades',
            '8 of Spades', '9 of Spades', '10 of Spades', 'Jack of Spades', 'Queen of Spades', 'King of Spades', 'Ace of Spades']
        self.player_hand = []
        self.player_total = 0
        self.dealer_hand = []
        self.dealer_total = 0
        self.bet = 0
        self.possible_winnings = 0
        self.double_down = 0
        self.ace_tracker_player = 0
        self.ace_tracker_dealer = 0
        self.stand = 0
        self.ace_tracker_player_midgame = 0
        self.ace_tracker_dealer_midgame = 0


    def load_wallet(self):
        load = int(input("How much would you like to load to your wallet?  "))
        self.wallet += load
        wallet_formatted = format(self.wallet, ",")
        print(f"Wallet: ${wallet_formatted}")


    def place_bet(self):
        if self.wallet > 0:
            betting_active = True
            while betting_active:
                bet = int(input("How much would you like to bet?  "))
                if bet <= self.wallet:
                    self.bet += bet
                    self.wallet -= bet
                    self.possible_winnings += int(bet * (3/2))
                    bet_formatted = format(self.bet, ",")
                    poss_winnings_formatted = format(self.possible_winnings, ",")
                    wallet_formatted = format(self.wallet, ",")
                    print(f"Bet: ${bet_formatted}")
                    print(f"Possible winnings:  ${poss_winnings_formatted}")
                    print(f"Wallet: ${wallet_formatted}")
                    betting_active = False
                else:
                    print("You do not have that amount available in your wallet.")
        
        else:
            print("You will need funds in your wallet before you can play.")


    def first_deal(self):
        if self.bet > 0:
            player_card = self.deck.pop()
            self.player_hand.append(player_card)
            player_card_value = self.cards['Cards'].get(player_card)
            self.player_total += player_card_value
            if player_card_value == 11:
                self.ace_tracker_player += 1
            dealer_card = self.deck.pop()
            self.dealer_hand.append(dealer_card)
            dealer_card_value = self.cards['Cards'].get(dealer_card)
            self.dealer_total += dealer_card_value
            if dealer_card_value == 11:
                self.ace_tracker_dealer += 1
            player_card = self.deck.pop()
            self.player_hand.append(player_card)
            player_card_value = self.cards['Cards'].get(player_card)
            self.player_total += player_card_value
            if player_card_value == 11:
                self.ace_tracker_player += 1
            dealer_card = self.deck.pop()
            self.dealer_hand.append(dealer_card)
            dealer_card_value = self.cards['Cards'].get(dealer_card)
            self.dealer_total += dealer_card_value
            if dealer_card_value == 11:
                self.ace_tracker_dealer += 1
    
            print(f"Your hand: {self.player_hand}  Total: {self.player_total}")
            print(f"Dealer's hand: {self.dealer_hand[0]}")
        
            if self.player_total < 21:
                if self.wallet >= self.bet:
                    double_down = input("Would you like to double down?  Yes | No  ")
                    if double_down.lower() == 'yes':
                        double_bet = self.bet
                        self.bet += double_bet
                        self.possible_winnings += int(double_bet * (3/2))
                        self.wallet -= double_bet
                        self.double_down += 1
                        print("Player doubles down")
                        player_card = self.deck.pop()
                        self.player_hand.append(player_card)
                        player_card_value = self.cards['Cards'].get(player_card)
                        self.player_total += player_card_value
                        print(f"Your hand: {self.player_hand}  Total: {self.player_total}")
                        bet_formatted = format(self.bet, ",")
                        poss_winnings_formatted = format(self.possible_winnings, ",")
                        wallet_formatted = format(self.wallet, ",")
                        print(f"Bet: ${bet_formatted}")
                        print(f"Possible winnings:  ${poss_winnings_formatted}")
                        print(f"Wallet: ${wallet_formatted}")


    def hit_or_stand_ace(self):
        if self.bet > 0 and self.double_down == 0:
            if self.ace_tracker_player > 0:
                while self.player_total < 21:
                    decision = input("What would you like to do? Hit | Stand  ")        
                    if decision.lower() == 'stand':
                        self.stand += 1
                        print("Player stands")
                        break
                    elif decision.lower() == 'hit':
                        print("Player hits")
                        player_card = self.deck.pop()
                        self.player_hand.append(player_card)
                        player_card_value = self.cards['Cards'].get(player_card)
                        self.player_total += player_card_value
                        print(f"Your hand: {self.player_hand}  Total: {self.player_total}")
                    elif self.player_total == 21:
                        print("Player stands")
                        break
          

    def player_ace_bust(self):
        if self.bet > 0 and self.double_down == 0:
            if self.ace_tracker_player > 0:
                if self.player_total > 21:
                    print("Player's Ace is now valued at 1 instead of 11.")
                    self.player_total -= 10
                    print(f"Your hand: {self.player_hand}  Total: {self.player_total}")
    

    def hit_or_stand(self):
        if self.bet > 0 and self.double_down == 0:
            if self.stand == 0:
                while self.player_total < 21:
                    decision = input("What would you like to do? Hit | Stand  ")        
                    if decision.lower() == 'stand':
                        self.stand += 1
                        print("Player stands")
                        break
                    elif decision.lower() == 'hit':
                        print("Player hits")
                        player_card = self.deck.pop()
                        self.player_hand.append(player_card)
                        player_card_value = self.cards['Cards'].get(player_card)
                        self.player_total += player_card_value
                        if player_card_value == 11 and self.ace_tracker_player == 0:
                            self.ace_tracker_player_midgame += 1
                        print(f"Your hand: {self.player_hand}  Total: {self.player_total}")
                    elif self.player_total == 21:
                        print("Player stands")
                        break


    def hit_or_stand_ace_bust(self):
        if self.bet > 0 and self.double_down == 0:
            if self.ace_tracker_player == 0 and self.ace_tracker_player_midgame == 1:
                if self.player_total > 21:
                    print("Player's Ace is now valued at 1 instead of 11.")
                    self.player_total -= 10
                    print(f"Your hand: {self.player_hand}  Total: {self.player_total}")

    
    def hit_or_stand_again_ace(self):
        if self.bet > 0 and self.double_down == 0:
            if self.ace_tracker_player == 0 and self.ace_tracker_player_midgame == 1:
                if self.stand == 0:
                    while self.player_total < 21:
                        decision = input("What would you like to do? Hit | Stand  ")        
                        if decision.lower() == 'stand':
                            print("Player stands")
                            break
                        elif decision.lower() == 'hit':
                            print("Player hits")
                            player_card = self.deck.pop()
                            self.player_hand.append(player_card)
                            player_card_value = self.cards['Cards'].get(player_card)
                            self.player_total += player_card_value
                            print(f"Your hand: {self.player_hand}  Total: {self.player_total}")
                        elif self.player_total == 21:
                            print("Player stands")
                            break

    
    def dealer_time_with_ace(self):
        if self.bet > 0:
            if self.ace_tracker_dealer > 0:
                if self.player_total < 22:
                    print(f"Dealer's hand: {self.dealer_hand}  Total: {self.dealer_total}")
                    while self.dealer_total < 17:
                        print("Dealer hits")
                        dealer_card = self.deck.pop()
                        self.dealer_hand.append(dealer_card)
                        dealer_card_value = self.cards['Cards'].get(dealer_card)
                        self.dealer_total += dealer_card_value
                        print(f"Dealer's hand: {self.dealer_hand}  Total: {self.dealer_total}")


    def dealer_busts_with_ace(self):
        if self.bet > 0:
            if self.ace_tracker_dealer > 0:
                if self.dealer_total > 21:
                    print("Dealer's Ace is now valued at 1 instead of 11.")
                    self.dealer_total -= 10
                    print(f"Dealer's hand: {self.dealer_hand}  Total: {self.dealer_total}")


    def dealer_time(self):
        if self.bet > 0:
            if self.player_total == 21 and len(self.player_hand) == 2:
                print("\n---  Blackjack!  ---")
            elif self.player_total > 21:
                print("\n---  Bust. Better luck next time.  ---")
            elif self.player_total < 22:
                if self.ace_tracker_dealer == 0:
                    print(f"Dealer's hand: {self.dealer_hand}  Total: {self.dealer_total}")
                while self.dealer_total < 17:
                    print("Dealer hits")
                    dealer_card = self.deck.pop()
                    self.dealer_hand.append(dealer_card)
                    dealer_card_value = self.cards['Cards'].get(dealer_card)
                    self.dealer_total += dealer_card_value
                    if dealer_card_value == 11 and self.ace_tracker_dealer == 0:
                        self.ace_tracker_dealer_midgame += 1
                    print(f"Dealer's hand: {self.dealer_hand}  Total: {self.dealer_total}")


    def dealer_busts_midgame_ace(self):
        if self.bet > 0:
             if self.ace_tracker_dealer == 0 and self.ace_tracker_dealer_midgame == 1:
                if self.dealer_total > 21:
                    print("Dealer's Ace is now valued at 1 instead of 11.")
                    self.dealer_total -= 10
                    print(f"Dealer's hand: {self.dealer_hand}  Total: {self.dealer_total}")


    def dealer_time_after_ace_bust_midgame(self):
        if self.bet > 0:
            if self.ace_tracker_dealer == 0 and self.ace_tracker_dealer_midgame == 1:
                while self.dealer_total < 17:
                    print("Dealer hits")
                    dealer_card = self.deck.pop()
                    self.dealer_hand.append(dealer_card)
                    dealer_card_value = self.cards['Cards'].get(dealer_card)
                    self.dealer_total += dealer_card_value
                    print(f"Dealer's hand: {self.dealer_hand}  Total: {self.dealer_total}")


    def results_time(self):
        if self.bet > 0:
            if self.player_total == 21 and len(self.player_hand) == 2:
                self.wins += 1
                self.winnings += self.possible_winnings
                self.wallet += self.bet
                self.wallet += self.possible_winnings
            elif self.player_total > 21:
                self.losses += 1
                self.winnings -= self.bet
            elif self.dealer_total > 21:
                print("\n---  Dealer busts. You win!  ---")
                self.wins += 1
                self.winnings += self.possible_winnings
                self.wallet += self.bet
                self.wallet += self.possible_winnings
            elif self.dealer_total > self.player_total:
                print(f"\n---  Dealer has {self.dealer_total}. Sorry.  ---")
                self.losses += 1
                self.winnings -= self.bet
            elif self.dealer_total < self.player_total:
                print(f"\n---  Dealer has {self.dealer_total}. You win!  ---")
                self.wins += 1
                self.winnings += self.possible_winnings
                self.wallet += self.bet
                self.wallet += self.possible_winnings
            elif self.dealer_total == self.player_total:
                print("\n---  It's a tie.  ---")
                self.wallet += self.bet
            winnings_formatted = format(self.winnings, ",")
            wallet_formatted = format(self.wallet, ",")
            print(f"\nWins: {self.wins}  |  Losses: {self.losses}")
            print(f"Wallet: ${wallet_formatted}  Winnings: ${winnings_formatted}\n")

    def show_rules(self):
        print("\nThe goal of blackjack is to beat the dealer's hand without going over 21.\
\nEach player starts with two cards, one of the dealer's cards is hidden until the end.\
\nTo 'Hit' is to ask for another card. To 'Stand' is to hold your total and end your turn.\
\nIf you go over 21 you bust, and the dealer wins regardless of the dealer's hand.\
\nIf you are dealt 21 from the start, you got a blackjack.\nDealer will hit until his/her cards\
 total 17 or higher.\nDoubling is like a hit, only the bet is doubled and you only get one more card.")


blackjack_player = Blackjack()

def play_blackjack():
    game_active = True
    print("Let's play Blackjack!")
    while game_active:
        answer = input("What would you like to do?  Rules  |  Load Wallet  |  Play  | Quit ")
        if answer.lower() == 'rules':
            blackjack_player.show_rules()
        elif answer.lower() == 'load wallet':
            blackjack_player.load_wallet()
        elif answer.lower() == 'play':
            blackjack_player.shuffle_deck()
            blackjack_player.place_bet()
            blackjack_player.first_deal()
            blackjack_player.hit_or_stand_ace()
            blackjack_player.player_ace_bust()
            blackjack_player.hit_or_stand()
            blackjack_player.hit_or_stand_ace_bust()
            blackjack_player.hit_or_stand_again_ace()
            blackjack_player.dealer_time_with_ace()
            blackjack_player.dealer_busts_with_ace()
            blackjack_player.dealer_time()
            blackjack_player.dealer_busts_midgame_ace()
            blackjack_player.dealer_time_after_ace_bust_midgame()
            blackjack_player.results_time()
            blackjack_player.collect_cards()
        elif answer.lower() == 'quit':
            print("Thanks for playing!")
            game_active = False
        else:
            print("Input not recognized. Try again.")

play_blackjack()
