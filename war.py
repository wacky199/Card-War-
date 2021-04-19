import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values={'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

class Card():
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]

    def __str__(self):
        return self.rank +" of "+ self.suit

class Deck():
    def __init__(self):
        self.deck=[]
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def shuffle(self):
        random.shuffle(self.deck)

    def __str__(self):
        return "New deck initiated"

    def distribute(self):
        deck1=self.deck[:26]
        deck2=self.deck[26:]
        return [deck1,deck2]

class Player():
    def __init__(self,name):
        self.name=name
    def card_add(self,cards,deck):
        for i in range(0,len(cards)):
            deck.append(cards[i])
    def card_pop(self,deck):
        return deck.pop(0)
    def __str__():
        return self.name
    
def check(card1,card2,deck1,deck2,player1,player2):
    mycard=[card1,card2]
    count=1
    if card1.value > card2.value:
        print("{} has bigger value card!".format(player1.name))
        player1.card_add(mycard,deck1)
        count+=1
        mycard.clear()
        return False
    elif card1.value < card2.value:
        print("{} has bigger value card!".format(player2.name))
        player2.card_add(mycard,deck2)
        count+=1
        mycard.clear()
        return False
    elif card1.value == card2.value and count!=1:
        print("both have same value card!")
        mycard.append(card1)
        mycard.append(card2)
        return True
    else:
        print("both have same value card!")
        count+=1
        return True

def ifwon(deck1,deck2):
    if len(deck1)==0 or len(deck2)==0:
        return False
    else:
        return True

""" def user_input():
    suit=input("What suit you want: ")
    rank=input("Type the rank of your card: ")
    card=Card(suit,rank)
    return card
 """
 
def wanna_play():
    answer=input("Wanna play further (Yes/No): ")
    if answer=="Yes" or answer=="yes":
        return True
    elif answer=="No" or answer=="no":
        return False
    else:
        print("Sorry, not a valid input!!! Only Yes or No is allowed.")
        wanna_play()


def game():
    #Who is our players
    name1=input("Name of first player: ")
    player1=Player(name1)
    name2=input("Name of second player: ")
    player2=Player(name2)
    #creating a new shuffled dec
    deck=Deck()
    deck.shuffle()
    #distributing the shuffled deck equally to players
    [deck1,deck2]=deck.distribute()
    play1=True
    play2=True
    while(play1 and play2):
        print("")
        #taking user input
        #card=user_input()
        card1=player1.card_pop(deck1)
        card2=player2.card_pop(deck2)
        print("{}: ".format(name1) + str(card1))
        print("{}: ".format(name2) + str(card2))

        ch=check(card1,card2,deck1,deck2,player1,player2)
        print("{} still has {} cards!".format(player1.name, len(deck1)))  
        print("{} still has {} cards!".format(player2.name, len(deck2)))
        while ch and len(deck1)!=0 and len(deck2)!=0:
            print("")
            card1=player1.card_pop(deck1)
            card2=player2.card_pop(deck2)
            print("{}: ".format(name1) + str(card1))
            print("{}: ".format(name2) + str(card2))
            ch=check(card1,card2,deck1,deck2,player1,player2)
            print("{} still has {} cards!".format(player1.name, len(deck1)))  
            print("{} still has {} cards!".format(player2.name, len(deck2)))

        play1=ifwon(deck1,deck2)

        if play1==False:
            if(len(deck1)==0):
                print("{} won!!! Congrats!!!".format(name1))
            else:
                print("{} won!!! Congrats!!!".format(name2))
        play2=wanna_play()
        

game()