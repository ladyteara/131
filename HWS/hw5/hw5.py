"""
Tara Walton  // tara1984
hw 5 - Due 4/17/15

Description: Using recursion - navigate a game board with n positive integers in
    in a row, the first number being zero. The numbers represent the cost to enter
    that "square". There are two moves, move to the adjacent "square", or jump over
    the adjacent column and land in the next "square". Lowest cost is desirable.
Requirements: must read from input.dat and must send output to stdout (monitor).
    Each line in the file corresponds to a game board.
"""
def play(self):
    cost = 0
    if len(self) == 1:
        return cost + self[0]
    elif len(self) == 2:
        return cost + self[1]
    else:
        cost = min(self[0] + play(self[1:]), self[1] + play(self[2:]))
    return cost
    
def readfile():
    try:
        data=[]
        f = open("input.dat")
        for line in f:
            data += line.strip().split('\n')
        for i in range(len(data)):
            data[i] = list(map(int, data[i].split()))
        return data
    except EOFError:
        print("End of file reached.")
    finally:
        pass

def main():
    data = readfile()
    for i in range(len(data)):
        #print(data[i])
        cost = play(data[i])
        print(cost)
    

main()
