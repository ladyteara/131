"""
TARA WALTON
tara1984

Purpose: to practice working with Python's higher order funcions and ternary operator
"""

#Let a be a list of values produced by list(range(1,11))
a = list(range(1, 11))
print(a)

#1- using map and lambda, write an expression that produces a list of the cubes of the values in a
    #assign to m and print
'''m = map(lambda x: x**3 for x in range(len(a)))
print(m(a))'''

#2- using filter function and lambda, write an expression that produces a list of 3|a.
    #assign to f1 and print
#from functools import reduce


#3- use reduce function and lambda argument, return the result of concaatenating all digits in a
    #assign to r1 and print #output should be '12345678910'
'''r1 = functools.reduce(lambda x,y : x + y)
print(r1(a))'''

#use list comprehension to produce the same list in 1
cubes = [x**3 for x in a]
print(cubes)

#use list comprehension to produce the same list in 2
div3 = [x for x in a if x%3==0]
print(div3)

#use list comprehension to produce a list containing the cubes of the values of a
    #that are divisible by 3. #output should be [27, 216, 729]
cubes3 = [ x**3 for x in div3]
print(cubes3)

#(2pts) write a func named evenFilter that takes an arguement of a dict element indexed
    #by integer keys. Using only a list comprehension, return the value of of elemenst
    #associated with the keys divisible by 2.  (example)
def evenFilter (d):
    
    

#(2pts) Write a func called findMin(x, y) that uses the ternary operator to find the
    #and return the min of its two arguments.  Write code to test this function.
