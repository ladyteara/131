"""
Tara Walton
taw1984
Lab 6 - Due 3/5/15

Description: Circles and Triangles

Input :
Output:
"""
from Shapes import Circle
from Shapes import Triangle
from geometricObject import GeometricObject


#code below written by Dr. Jamil Saquer
def main():
    #Testing Circle class
    c = Circle(5, "blue", False)
    print(c)
    print()
    
    print("Entering input values for a circle")
    r = float(input('Enter value for radius: '))

    c1 = Circle(r)
    
    print(c1)
    print("%.2f" % c1.getArea())
    print("%.2f" % c1.getPerimeter())
    print(c1.getColor())
    print(c1.isFilled())

    #Testing Triangle class
    print("\nEntering input values for a traingle")
    s1 = float(input('Enter value for side1: '))
    s2 = float(input('Enter value for side2: '))
    s3 = float(input('Enter value for side3: '))
    color = input('Enter color of the triangle: ')
    filled = input('Is the triangle filled (1/0)? ')
    filled = (filled == "1")
    t1 = Triangle(s1, s2, s3, color, filled)

    print(t1)
    print("%.2f" % t1.getArea())
    print("%.2f" % t1.getPerimeter())
    print(t1.getColor())
    print(t1.isFilled())

main()
