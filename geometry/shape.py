from abc import ABC, abstractmethod
from typing import Tuple
from geometry.point import Point


class Shape(ABC):


  @abstractmethod
  def dimensionality(self, *coords:Tuple[Point])->int:
    pass
  
  @abstractmethod
  def contains(self, point:Point)->bool:
    pass
  
