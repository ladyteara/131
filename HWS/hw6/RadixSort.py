"""
Tara Walton // tara1984
hw 6 - Due Apr 27, 15

Description: Write a program for radix sort. The input will consist of 3 digit
    positive integers. The program must read from a text file called and store
    in a file called radix.out. 

Input:  radix.in (text file)
Output: radix.out (text file)
"""
from collections import deque
#built-in deque methods (append(x), appendleft(x), clear(), count(x),
#extend(iterable), extendleft(iterable), pop(), popleft(), remove(value),
#reverse() - returns None, rotate(n)

def readFile(fname):
    try:
        data = []
        f = open(fname)
        for line in f:
            data += line.strip().split('\n')
        for i in range(len(data)):
            data[i] = list(map(int, data[i].split()))  
        #return data
    except EOFError:
        print("End of file reached.")
    finally:
        print(fname, ": File read completed.\n")
    #if data is not empty, print initial information
    if len(data) > 0:
        print("Initial data: ")
        for l in range(len(data)):
            for i in range(len(data[l])):
                print(str(data[l][i]), end = " ")
            print()
    return data

def writeFile(text, fname):
    fout = open(fname, 'w')
    if len(text) > 0:
        print("\nWriting sorted values to file...")
        for l in range(len(text)):
            for i in range(len(text[l])):
                fout.write(str(text[l][i]) + " ")
                print(str(text[l][i]), end = " ")
            fout.write('\n')
            print()
        print ("\nWriting complete to file:", fname)
    else:
        print ("No data written to file", fname)
    fout.close()

def main():
    fileIn = "radix.in.txt"
    fileOut = "radix.out.txt"
    data = readFile(fileIn)
    sort = deque()
    for i in range(len(data)):
        sort.append(radixSort(data[i])) 
    writeFile(sort, fileOut)

def radixSort(data):
    tmp = 0
    place = 1
    if len(data) > 0:
        sort = False
    else:
        sort = True
    while not sort:
        sort = True
        #initialize empty queues
        queue = [deque() for i in range(10)]
        #split between queues
        for i in data:
            temp = i // place           #1, 10, 100
            queue[temp%10].append(i)    #mod 10 to get single digit value
            if sort and temp > 0:
                sort = False
        #dump back into original list
        a=0
        for j in range(10):             #10 queues
            q = queue[j]
            for each in q:              #each value in queue
                data[a] = each          #replace values in original list
                a += 1                  #next value
        place *= 10
    return data
    
main()
