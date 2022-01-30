

class Blackjack():
    def __init__(self):
        self.cards = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,
            6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,
            11,11,11,11,12,12,12,12,13,13,13,13]
        self.player_hand = []
        self.dealer_hand = []
        self.wins = 0
        self.losses = 0
        self.wallet = 0
        self.winnings = 0
        self.bet = 0
        self.possible_winnings = 0
        

    def shuffle_deck(self):
        import random
        random.shuffle(self.cards)


    def collect_cards(self):
        self.cards = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,
            6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,
            11,11,11,11,12,12,12,12,13,13,13,13]
        self.player_hand = []
        self.dealer_hand = []
        self.bet = 0
        self.possible_winnings = 0


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
            player_card = self.cards.pop()
            self.player_hand.append(player_card)
            dealer_card = self.cards.pop()
            self.dealer_hand.append(dealer_card)
            player_card = self.cards.pop()
            self.player_hand.append(player_card)
            dealer_card = self.cards.pop()
            self.dealer_hand.append(dealer_card)

            print(f"Your hand: {self.player_hand}  Total: {sum(self.player_hand)}")
            print(f"Dealer's hand: {self.dealer_hand[0]}")

            if sum(self.player_hand) < 21:
                if self.wallet >= self.bet:
                    double_down = input("Would you like to double down?  Yes | No  ")
                    if double_down.lower() == 'yes':
                        double_bet = self.bet
                        self.bet += double_bet
                        self.possible_winnings += int(double_bet * (3/2))
                        self.wallet -= double_bet
                        bet_formatted = format(self.bet, ",")
                        poss_winnings_formatted = format(self.possible_winnings, ",")
                        wallet_formatted = format(self.wallet, ",")
                        print(f"Bet: ${bet_formatted}")
                        print(f"Possible winnings:  ${poss_winnings_formatted}")
                        print(f"Wallet: ${wallet_formatted}")


    def hit_or_stand(self):
        if self.bet > 0:
            while sum(self.player_hand) < 21:
                decision = input("What would you like to do? Hit | Stand  ")        
                if decision.lower() == 'stand':
                    print("Player stands")
                    break
                elif decision.lower() == 'hit':
                    print("Player hits")
                    player_card = self.cards.pop()
                    self.player_hand.append(player_card)
                    print(f"Your hand: {self.player_hand}  Total: {sum(self.player_hand)}")
                elif sum(self.player_hand) == 21:
                    print("Player stands")
                    break
        

    def dealer_time(self):
        if self.bet > 0:
            if sum(self.player_hand) == 21 and len(self.player_hand) == 2:
                print("\n---  Blackjack!  ---")
            elif sum(self.player_hand) > 21:
                print("\n---  Bust. Better luck next time.  ---")
            elif sum(self.player_hand) < 22:
                print(f"Dealer's hand: {self.dealer_hand}  Total: {sum(self.dealer_hand)}")
                while sum(self.dealer_hand) < 17:
                    print("Dealer hits")
                    dealer_card = self.cards.pop()
                    self.dealer_hand.append(dealer_card)
                    print(f"Dealer's hand: {self.dealer_hand}  Total: {sum(self.dealer_hand)}")
     

    def results_time(self):
        if self.bet > 0:
            if sum(self.player_hand) == 21 and len(self.player_hand) == 2:
                self.wins += 1
                self.winnings += self.possible_winnings
                self.wallet += self.bet
                self.wallet += self.possible_winnings
            elif sum(self.player_hand) > 21:
                self.losses += 1
                self.winnings -= self.bet
            elif sum(self.dealer_hand) > 21:
                print("\n---  Dealer busts. You win!  ---")
                self.wins += 1
                self.winnings += self.possible_winnings
                self.wallet += self.bet
                self.wallet += self.possible_winnings
            elif sum(self.dealer_hand) > sum(self.player_hand):
                print(f"\n---  Dealer has {sum(self.dealer_hand)}. Sorry.  ---")
                self.losses += 1
                self.winnings -= self.bet
            elif sum(self.dealer_hand) < sum(self.player_hand):
                print(f"\n---  Dealer has {sum(self.dealer_hand)}. You win!  ---")
                self.wins += 1
                self.winnings += self.possible_winnings
                self.wallet += self.bet
                self.wallet += self.possible_winnings
            elif sum(self.dealer_hand) == sum(self.player_hand):
                print("\n---  It's a tie.  ---")
                self.wallet += self.bet
            winnings_formatted = format(self.winnings, ",")
            wallet_formatted = format(self.wallet, ",")
            print(f"\nWins: {self.wins}  |  Losses: {self.losses}")
            print(f"Wallet: ${wallet_formatted}  Winnings: ${winnings_formatted}\n")


blackjack_player = Blackjack()

def play_blackjack():
    game_active = True
    print("Let's play Blackjack!")
    while game_active:
        answer = input("What would you like to do?  Load Wallet  |  Play  | Quit ")
        if answer.lower() == 'load wallet':
            blackjack_player.load_wallet()
        if answer.lower() == 'play':
            blackjack_player.shuffle_deck()
            blackjack_player.place_bet()
            blackjack_player.first_deal()
            blackjack_player.hit_or_stand()
            blackjack_player.dealer_time()
            blackjack_player.results_time()
            blackjack_player.collect_cards()
        elif answer.lower() == 'quit':
            print("Thanks for playing!")
            game_active = False

play_blackjack()
