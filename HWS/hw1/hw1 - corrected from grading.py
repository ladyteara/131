"""
TARA WALTON
folder: tara1984
HW 1 - due 01/30/15

Description: Write a program that tests whether or not a 3x3 grid is a valid 
magic square. The program should read input from a txt file named input.txt.
Each line in the file contains exactly 9 numbers that correspond to the values 
in a possible magic square.  The first 3 numbers correspond to the values in the
first row, the next 3 the second row, the last three the last row.

INPUT : input.txt
OUTPUT: VALID, if a grid is a magic square, INVALID if not.
"""

file = "input.txt"

def read_file(fname):
    '''Reads numbers from a file to 2-D (3-D) list''' 
    f = open(fname, 'r')
    data = f.readlines() #1 list of 6 strings
    f.close()
    for i in range(len(data)):
        data[i] = list(map(int, data[i].split())) #1 list of 6 lists of integers
    #print(data)
    #3-D list conversion ; easier indexing options
    matrix = [0]*len(data) #zero matrix with slots for all lines in input.txt
    count = 0
    while count < len(data): 
        square = []     #blank template for each magic square
        s = 0 #start of slice
        e = 3 #end of slice
        while s <= 6:
            while e<= 9:
                square.append(data[count][s:e]) #add to square a slice of data
                s+=3    #move starting point
                e+=3    #move ending point
        for i in range(len(data)):  #when square is built, add list to matrix
            matrix[count] = list(square)
        count += 1
    print("M: ", matrix)
    return data, matrix
    
def num_magic(row):  #accepts one row at a time from sum_magic
    '''Verifies that the numbers 1-9 are used exactly once'''
    #print(row)
    for number in range(1,10):
        if number not in row:
            #print("false")
            return False 
    #print("true")
    return True


def sum_magic(d, m): #takes list data for num check, matrix for sums
    '''Verifies sumation of all  rows, columns, diagonals'''
    row = len(m[0])     #3
    col = len(m[0][0])  #3
    for i in range(len(m)): #6
        magic = " "
        if num_magic(d[i]):
            #rows
            rtot = [0, 0, 0]  #row totals
            for r in range(row):
                for c in range(col):
                    rtot[r] += m[i][r][c]
            #columns
            ctot = [0, 0, 0]  #column totals
            for c in range(col):
                for r in range(row):
                    ctot[c] += m[i][r][c]
            #diagonals
            d1 = 0  #diagonal from left to right
            d2 = 0  #diagonal from right to left
            for r in range(row):
                for c in range(col):
                    if r == c:
                        d1 += m[i][r][c]
                    if (r + c) == 2:
                        d2 += m[i][r][c]
        #is the square magic?
            #print(d1, d2, rtot, ctot)
            if d1==d2==15 and rtot[0]==rtot[1]==rtot[2]==15 \
               and ctot[0]==ctot[1]==ctot[2]==15:
                magic = "valid"
            else:
                magic = "invalid"
        else:
            magic = "invalid"
        print(magic)
        #print()
    
def main():
    '''Put it all together'''
    d, m = read_file(file)
    sum_magic(d, m)
    # sum_magic([[6, 9, 8], [7, 5, 3], [2, 1, 4]])
    # sum_magic([[6, 1, 8], [7, 5, 3], [2, 9, 4]])
    

main() #call main
