

from typing import List, Tuple


class Point:
  def __init__(self, *args:List[float]):
    self._dimensions:int = len(args)
    self._coords:Tuple[float] = tuple(args)
    
    return
  
  def loc(self)->Tuple[float]:
    return self._coords
  
  def dimensions(self)->int:
    return self._dimensions