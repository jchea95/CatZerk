

#### -------------  Chase: Creating flock class -------------  ####

class Flock(object):

    def __init__(self):
        self.boids = []  # Initialize a list for all the boids.

    def run(self, playerLoc, theMap):
        for b in self.boids:
            # Pass the entire list of boids to each boid individually.
            b.run(self.boids, playerLoc, theMap)
    
            #if b.isShot(player): 
                #b.removeBoid()

    def addBoid(self, b):
        self.boids.append(b)
        
    def removeBoid(self, b):
        self.boids.remove(b)
