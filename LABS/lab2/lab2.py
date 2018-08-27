"""
TARA WALTON
LAB 2

This program will accept values from a user into a 3x4 matrix (2D list).
It will show the matrix and then calculate the sum of each column.

Input : User entered numbers
Output: Matrix and column sums

Main function designed by Jamil Saquer
"""

def getMatrix():
    '''Allows the user to input values separated by spaces for each row'''
    rows = 3
    cols = 4
    flt_list = []
    matrix = [None] * rows
    for r in range(rows):
        matrix[r] = input("Enter a 3-by-4 matrix row for row " + str(r) + ":  ")
        matrix[r] = list(matrix[r].split())
        #print(matrix)
        matrix[r] = list(map(float, matrix[r])) #covert to lists of floats
    return matrix


def sumColumn(matrix, columnIndex): #needs work 
    '''Totals each column in the matrix'''
    total = 0
    for r in range(len(matrix)):
        total += float(matrix[r][columnIndex])
    #print("function total", total)

    '''for c in range(columnIndex):
        total = 0
        for r in range(len(matrix)):
            total += float(matrix[r][c])
        print(total)''' 
        

def display(matrix):
    '''Displays the matrix input by user'''
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            print(matrix[r][c], end=" ")
        print()

#all code below from Dr. Saquer
def main():
    '''Code designed by Dr. Saquer'''
    m = getMatrix()
    print("\nThe matrix is")
    display(m)
    print()
    
    for col in range(len(m[0])):
        print("Sum of elements for column %d is %.2f" % (col, sumColumn(m,col)))      
        # %d = col, %.2f is sumColumn to 2 decimals pts, float    

main()
