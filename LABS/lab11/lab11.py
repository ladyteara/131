"""
Tara Walton  // tara1984
lab 11 - Due 4/30

Description: practice using grids and arrays
"""

from arrays import Array
from grid import Grid
from random import randint

def countNumbers():
    '''generates and counts numbers 0-9'''
    import random
    counts = Array(10, 0)       
    for i in range(1000):
        num = randint(0, 9)
        counts[num] += 1
    print("%-6s\t%-6s" % ("Number", "Counts"))
    for i in range(len(counts)):
        print("%-6d\t%-6d" % (i, counts[i]))
    
def shuffle(array):
    '''shuffles elements of an array'''
    for i in range(len(array)):
       r = randint(0,9)
       array[i], array[r] = array[r], array[i]
    return array

def sumColumn(m, columnIndex):
    '''returns the sum of elements in a col of grid'''
    sumCol=0
    for row in m:
        sumCol += row[columnIndex]
    return sumCol
    
#code below by Dr. Jamil Saquer
def main():
    print("Testing the countNumbers function")
    countNumbers()

    print("\nTesting the shuffle function")
    A = Array(10)
    for i in range(10):
        A[i] = randint(1,100)
    print("Original array:", A)
    shuffle(A)
    print("After shuffling:", A)

    print("\nTesting the sumColumn function")
    matrix = Grid(4,5,0)
    for r in range(matrix.getHeight()):
        for c in range(matrix.getWidth()):
            matrix[r][c] = int(str(r) + str(c))
    print("matrix is\n", matrix)

    print("%6s\t%3s" % ("Column", "Sum"))
    for column in range(matrix.getWidth()):
        print("%6d\t%3d"  % (column, sumColumn(matrix,column))) 

main()
