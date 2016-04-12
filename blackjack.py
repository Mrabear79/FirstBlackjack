import random
import itertools

suit = 'scdh'
rank = '23456789TJQKA'
deck = tuple(''.join(card) for card in itertools.product(rank, suit))
val = []
for a in range(9):
    val += [a+2] * 4
for _ in range(3):
    val += [10] * 4
val += [1] * 4
deckval = dict(zip(deck, val))
counter = 0


def shuffle():

    global s_deck
    s_deck = random.sample(deck, 52)


class Hand:

    global counter, s_deck

    def __init__(self):

        global counter
        self.cards = list(s_deck[counter:counter + 2])
        counter += 2
        self.hand_sum = 0
        self.init_sum = 0

    def sum_hand(self):

        self.hand_sum = 0
        self.init_sum = 0
        for b in range(len(self.cards)):
            self.init_sum += deckval[self.cards[b]]
        if ('As' in self.cards or 'Ac' in self.cards or 'Ad' in self.cards or
            'Ah' in self.cards)\
           and self.cards and self.init_sum + 10 <= 21:
            self.hand_sum = self.init_sum + 10
        else:
            self.hand_sum = self.init_sum

    def draw(self):

        global counter
        self.cards += list(s_deck[counter:counter + 1])
        counter += 1

    def hit_or_stay(self, dealer):

        self.bust(dealer)
        print("\n\nDealer's hand:", dealer.cards[0], "--")
        print("Your hand:", self.cards, "   Your total:", self.hand_sum, "\n")
        choice = input("Hit or Stay? ").lower()
        if choice == 'h':
            self.draw()
            self.hit_or_stay(dealer)
        elif choice == 's':
            self.total(dealer)
        else:
            print("Please enter hit or stay")
            self.hit_or_stay(dealer)

    def total(self, dealer):

        if self.hand_sum > dealer.hand_sum:
            print("You won!")
        elif self.hand_sum < dealer.hand_sum:
            if dealer.hand_sum <= 21:
                print("Sorry you lost")
            else:
                print("Dealer busted!")
        else:
            print("Tied with Dealer")
        print("Dealer's hand:", dealer.cards, "Dealer's sum:", dealer.hand_sum)
        print("Your hand:", self.cards, "Your sum:", self.hand_sum)
        print("\n*******************\n")

    def bust(self, dealer):

        self.sum_hand()
        if self.hand_sum > 21:
            print("BUSTED!!\n")
            self.hand_sum = 0
            self.total(dealer)
        else:
            pass


class Dealer(Hand):

    def __init__(self):
        Hand.__init__(self)
        self.logic()

    def logic(self):

        self.sum_hand()
        while self.hand_sum < 17:
            self.draw()
            self.sum_hand()


class Game:

    def __init__(self):

        x = input("Are you in this hand?").lower()
        if x == "y":
            shuffle()
            player = Hand()
            dealer = Dealer()
            player.hit_or_stay(dealer)
        else:
            pass

if __name__ == '__main__':
    game = Game()
