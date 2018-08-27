"""
Tara Walton // tara1984
HW 3 - Due 3/18/15
Description : Allows the user to play a memory game using a self defined number of rows and columns
    totalling an even number of cards.  Cards are selected through a coordinate system.
Requirements: 3 classes - card, deck, game
              cards stored in a 2D list

Input : rows and columns (max 9x8 or 8x9), coordinates
Output: Game board
"""
from cards import Card, Deck, Game


#Code below written by Dr. Saquer
def main():
    while True:
        # Force user to enter valid value for number of rows
        while True:
            rows = input("Enter number of rows ")
            if rows.isdigit() and ( 1 <= int(rows) <= 9):
                rows = int(rows)
                break
            else:
                print ("    ***Number of rows must be between 1 and 9! Try again.***")
                # Adding *** and indenting error message makes it easier for the user to see

        # Force user to enter valid value for number of columns
        while True:
            columns = input("Enter number of columns ")
            if columns.isdigit() and ( 1 <= int(columns) <= 9):
                columns = int(columns)
                break
            else:
                print ("    ***Number of columns must be between 1 and 9! Try again.***")

        if rows * columns % 2 == 0:
            break
        else:
            print ("    ***The value of rows X columns must be even. Try again.***")

    game = Game(rows, columns)
    game.play()

if __name__ == "__main__":
    main()


main()
