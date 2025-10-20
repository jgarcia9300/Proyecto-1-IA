class State:
  def __init__(self, tiles):
    """"
    Parameters
    -------
    tiles: 2d list
      A list of list of tiles. All are numbers except for the blanck, which is " "
      Ex) [[2, 6, 1], [7, " ", 3], [5, 8, 4]]
    """
    self.tiles = tiles
    self.prev = None
    
    def _repr_(self):
      """
      Returns
      -------
      Printable string representation of the board
      """
      s=""
      for i in range(len(self.tiles)):
        for j in range(len(self.tiles[i])):
          s = + "{} ".format(self.tiles[i][j])
          s += "\n"
          
    
    def __lt__(self, other):

      """
      Overload the less than operator so that ties can be broken
      automitacally in a heap without crashing
      Parameters
      --------
      ohter: State
        Another state
      
      Returns
      ---------
      Results of < on string comparison of __str__ from self
      and other    
      """
      return str < str(other)