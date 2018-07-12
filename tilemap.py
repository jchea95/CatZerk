
#### -------------  Julie: Creating Map Class -------------  ####
class Map:
        
    def __init__(self, fileName):
        self.maze = [] 
        self.mazeSize = 11
        self.tileSize = 50
        self.fileName = fileName
        #opening file
        file = open(self.fileName, 'r')
        # loop through all lines of input file
        for line in file:
            lines = line.split( )
            #make them into int
            row = []
            for numStr in lines:
                #turn into integer
                num = int(numStr)
                row.append(num)
        
            self.maze.append(row)
            
        # update maze size but remember you can only use square map ((( make sure this is right))
        self.mazeSize = len(self.maze)
            
    # x and y are the same because it's a square
    def getPixSize(self):
        return self.mazeSize * self.tileSize
        
    # receives x coords in pixels and returns int value to indicate where in map column is occupied
    def pixelXToCol(self, pixelX):
        return pixelX // self.tileSize
    
    def colToPixelX(self, col):
        return self.tileSize * col
    
    # receives y coords in pixels and returns int values to indicate where in map the row is occupied
    def pixelYToRow(self, pixelY):
        return pixelY // self.tileSize
    
    def rowToPixelY(self, row):
        return self.tileSize * row
            
    # returns how many tiles are horizontal/vertical. map will always be sqyare        
    def getMazeSize(self):
        return self.mazeSize
    
    # returns int value of tile located at map squarerow, column
    def getTileValue(self, r, c):
        return self.maze[r][c]
    
    # returns the int of the empty tile
    def getPassableTileValue(self):
        return 0
    
    # checks to see if the tile that the sprite is on isn't a "wall" tile
    def isPassable(self, tileValue):
        if self.tileValue == 0:
            return true
        else:
            return false
    
        
