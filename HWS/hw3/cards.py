"""
Tara Walton  // tara1984
Homework 3 - Due 3/18/15

Description: Allows the user to play a memory game using a self defined
    number of rows and columns totalling an even number of cards.
    Cards are selected through a coordinate system.
"""
class Card(object):
    """ Creates a memory card with ranks row*column/2 """    
    def __init__(self, rank, faceUp=False):
        """Creates a card with the given rank and face up/down."""
        self._rank = rank
        self._faceUp = faceUp

    def __str__(self):
        if self._faceUp:
            return '%3s' % str(self._rank)
        else:
            return '%3s' % '*'

    def getVal(self):
        return str(self._rank)
                 
class Deck(object):
    """ Creates a deck of cards (2 of each card)"""
    def __init__(self, rows, cols):
        self._cards = []
        for rank in range(1, (rows*cols//2)+1):
            c = Card(rank, False)
            self._cards.append(c) #appends card
            self._cards.append(c) #appends matching card to first
    
    def __str__(self):
        """ Returns a string representation of the deck """
        self.deck = ''
        for c in self._cards:
            self.deck = self.deck + str(c) + ' '
        return self.deck

    def __len__(self):
        return len(self._cards)

    def shuffle(self):
        """ Shuffles the cards """
        import random
        random.shuffle(self._cards)
        
    def deal(self):                 
        """ deals cards to the game board """
        if len(self) == 0:
            return None
        else:
            return self._cards.pop(0)           

    def remaningCards(self):
        """ Returns the number of cards left in the deck """
        return len(self._cards)

class Game(object):
    """ Creates and plays a game of memory """
    def __init__(self, rows, cols):
        self._rows = rows
        self._cols = cols
        self._deck = Deck(rows, cols)
        self._deck.shuffle()
        self._board = []
    
    def __str__(self):  #doesn't work
        for r in range(self._rows):
            for c in range(self._cols):
                print(self._board[r][c], end=" ")
            print()

    def populateBoard(self):
        self._board = [None] * self._rows
        for row in range(self._rows):
            self._board[row] = [0] * self._cols
        for r in range(self._rows):
            for c in range(self._cols):
                self._board[r][c] = self._deck.deal()
        return self._board

    def displayBoard(self):
        return Game.__str__(self)


    def isGameOver(self, remCards):
        if remCards > 0:
            return True
        else:
            print('***Congratulations! You completed the board!***') 
        return False
    
    def play(self):
        board = self.populateBoard()
        remainingCards = self._rows*self._cols
        #test print, deck has nothing in it?
        cont = self.isGameOver(remainingCards)
        while cont:
            self.displayBoard()
            #verify coordinate 1
            try:
                coord1= input("Enter coordinates for first card:  ")
                coord1 = list(map(int, coord1.split()))
                r1 = coord1[0]
                c1 = coord1[1]
                if (r1 <= self._rows) and (c1 <= self._cols):
                    r1 -= 1 #adjust for index starting at 0
                    c1 -= 1
            except IndexError:
                print('***Index out of range, try again.***')
            except ValueError:
                print('***Coordinates must be numeric! Try again.***')
            #verify coordinate 2
            try:
                coord2= input("Enter coordinates for second card: ")
                coord2 = list(map(int, coord2.split()))
                r2 = coord2[0]
                c2 = coord2[1]
                if (r2 <= self._rows) and (c2 <= self._cols):
                    r2 -= 1 #adjust for index starting at 0
                    c2 -= 1
            except IndexError:
                print('***Index out of range, try again.***')
            except ValueError:
                print('***Coordinates must be numeric! Try again.***')
            else:
                if coord1 == coord2:
                    print('***Invalid entry - Cannot use the same coordinates!***')  
            #compare cards
            card1 = board[r1][c1]
            card2 = board[r2][c2]
            if card1 == card2:
                card1._faceUp = True
                card2._faceUp = True
                print("***MATCH!*** Found", str(card1), "at (", r1+1, ", ", c1+1, ")", \
                      "and", str(card2), "at (", r2+1, ", ", c2+1, ")")
                remainingCards -= 2
                cont = self.isGameOver(remainingCards)
            else:
                print('*** NO MATCH! Try again***')

