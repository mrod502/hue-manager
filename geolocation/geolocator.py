
from typing import List, Tuple
from geometry.point import Point


class Geolocator(Point):
  def __init__(self, id:str, *coords:List[float]):
    Point(coords)
    self._id = id
    
    return

  def locate(self)->Tuple[float]:

    return (0,0)