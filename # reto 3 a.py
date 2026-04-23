# reto 3
import math

class point:
   def __init__(self,x: float,y: float):
      self.x = x
      self.y = y

class line:
   def __init__(self, start:point, end: point):
      self.start = start
      self.end = end 
      self.length = self.compute_length()
      self.slope = self.compute_slope()

def compute_length(self):
    dx = self.end.x - self.start.x
    dy = self.end.y - self.start.y
    return math.sqrt(dx**2 + dy**2)

def compute_slope(self):
    dx = self.end.x - self.start.x
    dy = self.end.y - self.start.y

    if dx == 0:
        return None
    pendiente = math.atan(dy/dx)
    pendiente_degrees = math.degrees (pendiente)
    return pendiente_degrees

def compute_horizontal_cross(self):
    dx = self.end.x - self.start.x
    dy = self.end.y - self.start.y
    if dx == 0:
       return None
    m = (dy/dx)
    b = self.start.y - m * self.start.x
    cross_x = -b/m
    return (cross_x, 0)

def compucompute_vertical_cross(self):
    dx = self.end.x - self.start.x
    dy = self.end.y - self.start.y
    if dx == 0:
       return None
    m = (dy/dx)
    b = self.start.y - m * self.start.x
    return (0,b)

class rectangle:
   def __init__(self,linea1,linea2,linea3, linea4):
      self.lines = [linea1,linea2,linea3,linea4]

def perimetro (self):
   return sum(line.compute_length() for line in self.lines)
    
def area (self):
   base= self.line [0].compute_length()
   altura=self.line [1].compute_length()
   return base*altura