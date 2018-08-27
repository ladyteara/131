"""
TARA WALTON
tara1984

Lab4 - Creates class named Point to represent a point in the Cartesian
       plane with x and y coordinates. Contains methods to find distance,
       compare points.
    
Due 2/9/15
"""
import math

class Point(object):
    '''A point represented by its Cartesian coordinates'''
    def __init__(self, x=0, y=0):
        '''Creates a point with Cartesian coordinates x, y'''
        self._x = x
        self._y = y

    def __str__(self):
        '''Returns a string representation of the point (x, y)'''
        return "(" + str(self._x) + ", " + str(self._y) + ")"

    def getX(self):
        '''returns the X value in a point'''
        return self._x

    def getY(self):
        '''returns the Y value in a point'''
        return self._y

    def getDistance(self, other):
        '''returns the distance from one point to another'''
        distance = math.sqrt((self._x - other._x)**2 + \
                             (self._y - other._y)**2)
        return distance
    
    #compares pts based on their distance from the origin (6 comparisons)
    def __eq__(self, other):
        '''equal to =='''
        if self is other:
            return True
        elif type(self) != type(other):
            return False
        else:
            origin = Point()
            return self.getDistance(origin) == other.getDistance(origin) \
                   and self == other
    def __ne__(self, other):
        '''not equal !='''
        return not self == other        
    def __lt__(self, other):
        '''less than <'''
        origin = Point()
        return self.getDistance(origin) < other.getDistance(origin)
    def __gt__(self, other):    
        '''greater than >'''
        return (not self < other) and (not self == other)
    def __le__(self, other):        
        '''less than or equal to <='''
        return (self < other) or (self == other)
    def __ge__(self, other):
        '''greater than or equal to >='''
        return (self > other) or (self == other)
        
#test code 
def main():
    p1 = Point(3, 4)
    print("p1: ", p1)
    p2 = Point(3, 0)
    print("p2 coordinates x: ", p2.getX(), ", y: ", p2.getY())
    print("\ndistance between p1 and p2: ", p1.getDistance(p2), "units\n")
    
    #6 comparisons of p1 and p2
    print("p1 <  p2?        ", p1 < p2)
    print("p1 == p2?        ", p1 == p2)
    print("p1  > p2?        ", p1 > p2)
    print("p1 <= p2?        ", p1 <= p2)
    print("p1 >= p2?        ", p1 >= p2)
    print("p1 != p2?        ", p1 != p2)
    print("p1 == 'Hello'?   ", p1 == 'Hello') 
    print("p1 != 'Hello'?   ", p1 != 'Hello')
    
main()

    
    
