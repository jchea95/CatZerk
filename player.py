from tileMap import Map

class Player(object):

    def __init__(self):
        self.name = "none"

    def __init__(self, x, y, file):
        self.location = PVector(x, y)
        self.speed = 20
        self.side = 50
        self.file = file
        self.sprite = loadImage(file)
        self.projectileX = self.location.x
        self.projectileY = self.location.y
        self.projectile = ellipse(self.projectileX, self.projectileX, 10, 10)
        
        
        
    def getLocation(self):
        return self.location
    
    def run(self, theMap):
        #fill(255)
        #stroke(255)
        image(self.sprite, self.location.x-self.side/2, self.location.y-self.side/2)
        #self.projectile = ellipse(self.projectileX, self.projectileY, 10, 10)
        moveDX = 0
        moveDY = 0

        if (keyPressed and key == CODED):
             if (keyCode == UP):
                 #self.location.y -= 20
                 moveDY = -15
             elif (keyCode == LEFT):
                 #self.location.x -= 20
                 moveDX = -15                
             elif (keyCode == DOWN):
                 #self.location.y += 20
                 moveDY = 15
                 moveD = 3
             elif (keyCode == RIGHT):
                 #self.location.x += 20
                 moveDX = 15
                    
             probeX = self.location.x + moveDX
             probeY = self.location.y + moveDY
             
             row = theMap.pixelYToRow(probeY)
             row = int(row)
             col = theMap.pixelXToCol(probeX)
             col = int(col)
            
             if theMap.getTileValue(row,col) == theMap.getPassableTileValue():
                self.location.x = probeX
                self.location.y = probeY
  
