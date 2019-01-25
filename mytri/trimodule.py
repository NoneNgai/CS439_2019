import math
class Triangle(object):
    def __init__(self,w,h):
        self.w = w
        self.h = h
    def area(self):
        return self.w*self.h*0.5
    def perimeter(self):
        if self.w!=self.h:
            a = (self.w/2.0)**2
            b = self.h**2.0
            c = math.sqrt(a+b)
            per = self.w+(c*2)
        elif self.w==self.h:
            per = self.w*3
            
        return per

class Equilateral(Triangle):
    def __init__(self,w):
        self.w = w
        self.h = w
    def __str__(self):
        return f'Equilateral Triangle width:{self.w}, area:{self.area()}, perimeter:{self.perimeter()}';
        
class Isosceles(Triangle):
    def __init__(self,w,h):
        self.w = w
        self.h = h
    def __str__(self):
        return f'Isosceles Triangle width:{self.w}, height:{self.h}, area:{self.area()}, perimeter:{self.perimeter()}';