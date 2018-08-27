"""
TARA WALTON, tara1984
HW2 - Due 2/11/15
Description: Creates a class Circle2D that allows a circle to be defined by its
    center and radius.  Will also allow a user to set and get values and compare
    two circles.  Main function design by Professor Jamil Saquer
INPUT : user defined x, y, and r for two circles
OUTPUT: various comparisons of two entered circles
"""
import math
class Circle2D(object):
    def __init__(self, x=0, y=0, r=0):
        '''creates a circle with center x, y and radius r'''
        self._x = x
        self._y = y
        self._r = r

    def __str__(self):
        '''Circle with center (x, y) and radius radius'''
        return "Circle with center (" + str(self._x) + ", " + \
               str(self._y) + ") and radius " + str(self._r)

    def setRadius(self, r):
        '''allows the radius to be reset'''
        self._r = r
        
    def getRadius(self):
        '''returns the radius value'''
        return self._r

    def getX(self):
        '''returns the center x value'''
        return self._x

    def getY(self):
        '''returns the center y value'''
        return self._y
    
    def getArea(self):
        '''calculates the area of a circle'''
        area = math.pi*(self._r**2)
        return area

    def getPerimeter(self):
        '''calculates the perimeter of a circle'''
        perimeter = 2*math.pi*self._r
        return perimeter
    
    def distance(self, x, y):
        '''calculates the distance between 2 points'''
        distance = math.sqrt((self._x - x)**2 + \
                             (self._y - y)**2)
        return distance

    def containsPoint(self, x, y): 
        '''returns True if a center point of circle2 lies inside circle1'''
        #d < R (not on perimeter)
        return self.distance(x, y) < self._r

    def contains(self, anotherCircle): 
        '''returns True if circle2 is inside his circle1'''
        #R - d >= r
        distance = self.distance(anotherCircle.getX(), anotherCircle.getY())
        return (self._r - distance) >=  anotherCircle._r
                                                                  
    def overlaps(self, anotherCircle):
        '''returns true if circle2 overlaps circle1, but is not completely contained'''
        #R + r >= d
        return (self._r + anotherCircle._r) >= \
               self.distance(anotherCircle.getX(), anotherCircle.getY()) and not \
               self.contains(anotherCircle)

    def __contains__(self, anotherCircle): 
        '''returns True if anotherCircle is contained ; tests operator in'''
        #overload of 'in' operator
        return self.contains(anotherCircle)
    
    #comparison methods (based on radii only)
    def __eq__(self, other):
        '''tests =='''
        if self is other:
            return True
        elif type(self) != type(other):
            return False
        else:
            return self._r == other._r
        
    def __ne__(self, other):
        '''tests !='''
        return not self == other
    
    def __lt__(self, other):
        '''tests <'''
        return self._r < other._r
    
    def __le__(self, other):
        '''tests <='''
        return (self <other) or (self == other)
    
    def __gt__(self, other):
        '''tests >'''
        return (not self < other) and (not self == other)
    
    def __ge__(self, other):
        '''tests >='''
        return (self > other) or (self == other)

#Code below by Dr Jamil Saquer
def main():
    x = float(input("Enter x coordinate for the center of circle 1: "))
    y = float(input("Enter y coordinate for the center of circle 1: "))
    r = float(input("Enter the radius of circle 1: "))
    c1 = Circle2D(x, y, r)
    print(c1)
    
    x = float(input("\nEnter x coordinate for the center of circle 2: "))
    y = float(input("Enter y coordinate for the center of circle 2: "))
    r = float(input("Enter the radius of circle 2: "))
    c2 = Circle2D(x, y, r)
    print(c2)

    #Test the getArea() and getPerimeter() methods
    print("\nArea of a %s is %0.2f" % (c1, c1.getArea()))
    print("Perimeter of a %s is %0.2f" % (c1, c1.getPerimeter()))

    print("\nArea of a %s is %0.2f" % (c2, c2.getArea()))
    print("Perimeter of a %s is %0.2f" % (c2, c2.getPerimeter()))
    #-------------------

    #Test containsPoint() method
    print("\nResult of c1.containsPoint(c2.getX( ), c2.getY( )) is",
          c1.containsPoint(c2.getX( ), c2.getY( )))

    #Test contains() method
    if c1.contains(c2):
        print("\n%s contains %s" % (c1, c2))
    else: 
        print("\n%s does not contain %s" % (c1, c2))
                                          
    print("\nResult of c2.contains(c1) is",
           c2.contains(c1))
    #----------------

    #Test overlap() method
    if c1.overlaps(c2):
        print("\n%s overlaps with %s" % (c1,c2))
    else: 
        print("\n%s does not overlap with %s" % (c1,c2))
    #--------------

    #Test overloaded in operator                                     
    print("\nResult of c2 in c1 is", c2 in c1)                     

    #Testing overloaded comparison and equality operators
    #Something similar to this
    print("\nTesting overloaded comparison operators...")
    print("c1 == c2?", c1 == c2)
    print("c1 != c2?", c1 != c2)
    print("c1 < c2?", c1 < c2)
    print("c1 <= c2?", c1 <= c2)
    print("c1 > c2?", c1 > c2)
    print("c1 >= c2?", c1 >= c2)
    print('c1 == "Hello"?', c1 == "Hello")
    print('c1 != "Hello"?', c1 != "Hello")
    
main()
