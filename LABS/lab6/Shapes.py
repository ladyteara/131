from geometricObject import GeometricObject

class Circle(GeometricObject):
    '''creates each instance of Circle'''
    def __init__(self, r=1.0, color="white", filled=True):
        '''creates a circle with radius r'''
        GeometricObject.__init__(self, color, filled)
        self._r = r

    def __str__(self):
        '''Circle with center (x, y) and radius radius'''
        return "Circle: radius = "+ str(self._r) + " " + GeometricObject.__str__(self)

    def getArea(self):
        import math
        '''calculates the area of a circle'''
        area = math.pi*(self._r**2)
        return area

    def getPerimeter(self):
        import math
        '''calculates the perimeter of a circle'''
        perimeter = 2*math.pi*self._r
        return perimeter
    

class Triangle(GeometricObject):
    ''' Creates each instance of Triangle'''
    def __init__(self, s1=1.0, s2=1.0, s3=1.0, color="white", filled=True):
        GeometricObject.__init__(self, color, filled)
        self._s1 = s1
        self._s2 = s2
        self._s3 = s3

    def __str__(self):
        return "Triangle: side 1 = " + str(self. _s1) + " side 2 = " + str(self._s2) +\
               " side 3 = " + str(self._s3) + " " + GeometricObject.__str__(self)

    def getArea(self):
        import math
        s = self.getPerimeter( )/2
        area = math.sqrt(s*(s-self._s1)*(s-self._s2)*(s-self._s3))
        return area


    def getPerimeter(self):
        perimeter = self._s1 + self._s2 + self._s3
        return perimeter
        


    

    
        
