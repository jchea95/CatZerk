### most recent


from boid import Boid
from flock import Flock
from player import Player
from tileMap import Map

flock = Flock()

#### ------------- Julie: constants to create map ------------- ####
TILE_SIZE_PIXELS = 50
MAP_SIZE_TILES = 11
MAP_SIZE_PIXELS = MAP_SIZE_TILES * TILE_SIZE_PIXELS

PASSABLE_TILE = 0

#### -------------  Julie: to switch from start screen to gameplay ------------- ####
stage = 1

def setup():
    global spriteList
    global flatLand
    global winSize
    
    global time
    global score 
    score = 0
    global gameFont
    global startFont
    
    gameFont = createFont("Arial", 16, True)
    startFont = createFont("Arial", 40, True)
    
    global playerLoc
    global player
    global healthAmt
    
    healthAmt = 100
    
    global tileMap
    global playerRow
    global playerCol
    
    global startScreen
 
    #### ------------- Julie: Creating Start Screen ------------- ####   
    startScreen = loadImage("catzerk_start.png")
    image( startScreen, 0, 0, width, height)
    
    

    player = Player(width / 3, height / 3, "Right0000.png")
    playerLoc = player.getLocation()
    projectile = player.projectile
    # Add an initial set of boids into the system
    for i in range(8):
        flock.addBoid(Boid(width / 2, height / 2))

    
    winSize = 500
    
    ####------------- Julie: Creating Map -------------  ####

    spriteList = []
    
    size(MAP_SIZE_PIXELS, MAP_SIZE_PIXELS)
    
    # these need to be loaded into sketch, just go back in here and look into list like spriteNames[i] w loop
    # Tile values -    0              1
    spriteNames = [ "floor.png", "treeTile.png", "Right0000.png" ]
    
    for name in spriteNames:
        img = loadImage(name)
        spriteList.append(img)


    flatLand = Map("zombTile.txt")


def draw():
    frameRate(60)
    global spriteList
    #global flatLand
    

    global tileMap
    global playerRow
    global playerCol
    global healthAmt
    
    
    global time 
    time = ((second()-60)*-1)
    global score
    score = millis()
    global gameFont
    global startFont
    global stage
    
    
    #### ------------- Julie: Displaying start screen -------------  ####

    if (stage == 1):
        #START
        fill(75)
        rect (78, 186, 390, 158, 7)
        textAlign(CENTER)
        fill(200)
        textFont(startFont)
        text("CLICK TO START", 275, 275)
        
        if (mousePressed and (mouseButton == LEFT)):
            if(mouseX >78 and mouseX < 468 and mouseY > 186 and mouseY < 390):
                stage = 2
    
    #### -------------  Julie: Start game upon click -------------  ####            
                        
    if (stage == 2):
        fill(255)
        numRows = len(flatLand.maze)
        numCols = len(flatLand.maze[0])

        
        # draw first tile at top left
        x = 0
        y = 0
        
        # go through text file and each number at each point 
        for r in range(numRows):
            for c in range(numCols):
                tileNumber = flatLand.getTileValue(r,c)
                image(spriteList[tileNumber], x, y)
                x = x + 50
            # at end of row, move down one tile size in pixels 
            y =  y + 50
            x =  0
        
    # image( spriteList[2], playerCol*TILE_SIZE_PIXELS, playerRow*TILE_SIZE_PIXELS)        
        player.run(flatLand)
        flock.run(playerLoc, flatLand)
        
        
        #### ------------- Chase: Losing Screen -------------  ####
        
        fill(255,0,0)
        if healthAmt < 100:
            if healthAmt > 0:
                health = rect(width-200, height-50, healthAmt, 25)
            else:
                health = rect(width-200, height-50, 0, 25)
                fill(255) # white
                rect(0,0,width,height)
                
                fill(0) # black text
                text("yo  you  dead", width/2-110, height/2-20)
                player.run(flatLand)
                
            
        else:
            
            healthAmt = 100
            health = rect(width-200, height-50, healthAmt, 25)
        for b in flock.boids:     
            if b.isCollides(playerLoc):
                healthAmt-=5

    
    #### ------------- Chase: Next Level -------------  ####
            
        if score > 10000 and time == 1:
            frameRate(1)
            textFont(gameFont, 32)
            fill(255, 0, 0)
            text("S P A W N", width/2-100, height/2-10)
            textFont(gameFont, 12)
            text("pick up the pace", width/2-65, height/2+20)
            flock.addBoid(Boid(width/2, height/2))
            for b in flock.boids:
                b.increaseSpeed()
            
    
        
        textFont(gameFont, 16)
        fill(255)
        text("countdown: " + str(time), width/2-50, 40)
        text("score: "+str(score), width/2-50, 20)
        
    
        
    
    
    
