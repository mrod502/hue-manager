from typing import Tuple

from .shape import Shape
from .point import Point
class Quadrilateral(Shape):
  
  def __init__(self, coords:Tuple[Point]):
    return
  
  def dimensionality(self) -> int:
    return 2
  
  def contains(self, point: Point) -> bool:
    
    if self.dimensionality() != point.dimensionality():
      raise TypeError("dimension mismatch")
    
    
    
    return True