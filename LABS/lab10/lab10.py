"""
Tara Walton //tara1984
lab 10 - Due 4/16
"""

def reverse(lyst):
    lst = []
    for i in range(len(lyst)-1, -1, -1):
        lst.append(lyst[i])
    return lst

def power(base, exponent):
    total = base
    for j in range(exponent-1):
        total *= base
    return total

def expo(base, exponent):
    if exponent == 0:
        return 1
    elif exponent %2 == 1:
        return base * expo(base, exponent - 1)
    elif exponent %2 == 0:
        return expo(base, exponent/2)**2
        
    

#Code below from Dr. Saquer
def main():
    lst = list(range(1, 11))
    print("List is", lst)
    print("Its reverse is", reverse(lst))

    lst = [7, 11, 43, -6, 54, 91]
    print("\nList is", lst)
    print("Its reverse is", reverse(lst))

    print("\nThe result of raising 5 to the power 4 is", power(5, 4))
    print("The result of raising 2 to the power 10 is", power(2, 10))

    print("\nexpo(7, 0) is", expo(7, 0))
    print("expo(2, 9) is", expo(2, 9))
    print("expo(2, 10) is", expo(2, 10))
    
main()

    
