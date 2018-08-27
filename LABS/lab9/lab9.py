"""
Tara Walton // tara1984
Lab 9 - Due 4/9/15

Description: Using recursion to build strings

NOTE TO SELF - recursion requires a base case
"""

def stutter(string):
    '''stutters a string to repeat each character in the string'''
    result = ""
    if len(string) == 0:
        return result
    else:
        result += string[0] + string[0]
        return result + stutter(string[1:])
        
def toNumber(string):
    '''returns the sum of all digit characters in a string'''
    total = 0
    if len(string)==0:
        return total
    else:
        if string[0].isdigit():
            total += int(string[0])
            return total + toNumber(string[1:])
        else:
            return toNumber(string[1:])

def main():
    string = input("What string would you like to stutter? ")
    doubles = stutter(string)
    print("   >>> ", doubles)
    alphanum = input("What string would you like to find the numeric total? ")
    toNum = toNumber(alphanum)
    print("   >>> ", toNum)
    

main()
