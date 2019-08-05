from random import shuffle

SUITE = 'H D S C'.split();
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

def index_of_card(card):
    index = RANKS.index(card)
    if index == 12:
        return 11
    elif index == 11:
        return 4
    elif index == 10:
        return 3
    elif index == 9:
        return 2
    else:
        return int(card)

def victory(player, score):
    print("{} wins with {}. Score is {}".format(player.name, score))

def game_over(player, score):
    print("{} loses with {}. Score is {}".format(player.name, score))

# mycards = [(s,r) for s SUITE for r in RANKS]

class Deck:
    def __init__(self):
        print("Creating new Deck!")
        mycards = []
        for r in RANKS:
            for s in SUITE:
                mycards.append((s,r))
        self.allcards = mycards

    def __str__(self):
        deck_str = ""
        for s in self.allcards:
            deck_str = deck_str + str(s);
        return deck_str
        
    def shuffle(self):
        print("Shuffling deck")
        shuffle(self.allcards)

    def make_a_hand(self):
        if len(self.allcards) > 2:
            hand = self.allcards[-2:]
            self.allcards = self.allcards[:-2]
            return hand
        else:
            print("No cards left")


class Hand:
    def __init__(self, cards):
        self.cards = cards

    def __str__(self):
        return "Contains {} cards".format(len(self.cards))
    
    def add(self, added_cards):
        self.cards.extend(added_cards)

    def remove_card(self):
        return self.cards.pop()

 
class Player:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand
    
    def count_score(self):
        message = "Now you have {} cards".format(len(self.hand.cards))
        score = 0
        #print(self.hand.cards)
        for card in self.hand.cards:
            #print(card)
            score = score + index_of_card(card[1])
            if score == 22 and len(self.hand.cards) == 2:
                return 21
            elif score > 21:
                return 23
        return score
            
    def asks_for_card(self, deck):
        self.hand.add(deck.allcards[-1:])
        deck.allcards = deck.allcards[:-1]
        print("Player takes card")
        print(self.hand)
        

print ('Welcome to the game')
d = Deck()
d.shuffle()

hand = d.make_a_hand()

name = input("What's your name: ")
user = Player(name, Hand(hand))
score = user.count_score()
while score <= 22:
    score = user.count_score()
    print(score)
    want_take_more_cards = input("Do you want to take one more card?")
    if want_take_more_cards.lower() == "y":
        user.asks_for_card(d)
    else:
        computer_hand = d.make_a_hand()
        comp = Player("comuter", Hand(computer_hand))
        
        print("Computer hand: ")
        print(computer_hand)
        print(comp.count_score())
        print(" VS ")
        print(user.count_score())
        print("{} hand: ".format(user.name))
        print(user.hand.cards)
        if user.count_score() > comp.count_score():
            print(user.name + " wins")
        score = 60
if score != 60:
    print(user.name + " loses, what a mess")


# # players

# name = input ("What's your name? Name: ")
# user = Player(name, Hand(half2))


