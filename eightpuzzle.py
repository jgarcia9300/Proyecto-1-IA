class State:
    def __init__(self, tiles):
        """
        Parameters
        ----------
        tiles : 2D list
            A list of lists of tiles. All are numbers except for the blank, which is " ".
            Example: [[2, 6, 1], [7, " ", 3], [5, 8, 4]]
        """
        self.tiles = tiles
        self.prev = None

    def __repr__(self):
        """
        Returns
        -------
        str
            Printable string representation of the board
        """
        s = ""
        for i in range(len(self.tiles)):
            for j in range(len(self.tiles[i])):
                s += "{} ".format(self.tiles[i][j])
            s += "\n"
        return s

    def __lt__(self, other):
        """
        Overload the less-than operator so that ties can be broken
        automatically in a heap without crashing.

        Parameters
        ----------
        other : State
            Another state

        Returns
        -------
        bool
            Result of < comparison between string representations
        """
        return str(self) < str(other)

    def copy(self):
        """
        Return a deep copy of this state
        """
        tiles = []
        for i in range(len(self.tiles)):
            tiles.append([])
            for j in range(len(self.tiles[i])):
                tiles[i].append(self.tiles[i][j])
        return State(tiles)

    def is_goal(self):
        """
        Returns
        -------
        bool
            True if this is a goal state, False otherwise
        """
        res = True
        N = len(self.tiles)
        # TODO: fill this in
        return res

    def get_neighbs(self):
        """
        Get this state's neighboring states

        Returns
        -------
        list of State
            A list of neighboring states
        """
        N=len(self.tiles)
        neighbs = []
      
        ## Step 1: find the row and col of the blank
        row = 0
        col = 0
        for i in range (N):
            for j in range(N):
                if self.tiles[i][j] == " ":
                    row = i
                    col = j
        # Step 2: Swap this index with neighbor
        ## that it can be swapped with
        for [i, j] in [[row-1, col], [row+1, col], [row, col-1], [row, col+1]]:
          if i>= 0 and j>= 0 and i < N and j < N:
              n = self.copy()
              ## Swap(rol, col) with(i, j)
              

        print(row, col)
        return neighbs


    def solve(self):
        """
        Find a shortest path from this state to a goal state

        Returns
        -------
        list of State
            A path from this state to a goal state, where the first element
            is this state and the last element is the goal
        """
        visited = {}
        queue = [self]
        finished = False
        # TODO: fill this in

        solution = []
        return solution


# Example usage:
state = State([[5, 6, 8], [" ", 4, 7], [1, 3, 2]])
state.get_neighbs()
print(state)
