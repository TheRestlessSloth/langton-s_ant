import turtle
import random as rnd

#todo: rewrite code for langtons ant in class

# Initializing the Window
window = turtle.Screen()
window.bgcolor('white')
window.screensize(1000,1000)
window.colormode(255)

# Contains the coordinate and colour
maps = {}
    # Initializing the Ant
ant = turtle.Turtle()
ant.shape('square')    
ant.shapesize(0.5)
ant.speed(10000)      

class langton:

    def __init__(self, ant, pos, step):
        self.pos = coordinate(ant)
        self.step = 10
        self.ant = turtle.Turtle()
        self.ant.shape('square')    
        self.shapesize(0.5)
        self.speed(0)#Max speed
        self.color = (rnd.randint(0,255), rnd.randint(0,255), rnd.randint(0,255))
    
    def invert(graph, ant, tile):
        if tile == "black":
            tile = "white"
            ant.left(90)
        else:
            tile = "black"
            ant.right(90)
        ant.fillcolor(tile)
        graph[coordinate(ant)] = tile

    def coordinate(ant):
        return (round(ant.xcor()), round(ant.ycor()))

    

def langton():                           
    # gives the coordinate of the ant                
    pos = coordinate(ant)                             
      
    while True:
        # distance the ant will move
        step = 10 
        if pos not in maps:
            invert(maps,ant,"white")
        else:
            invert(maps, ant, maps[pos])   

        ant.forward(step)                         
        pos = coordinate(ant)
    #stamps a copy of the ant on the canvas
        ant.stamp()                                 
  
def invert(graph, ant, tile):
    if tile == "black":
        tile = "white"
        ant.left(90)
    else:
        tile = "black"
        ant.right(90)

    ant.fillcolor(tile)
    graph[coordinate(ant)] = tile
  
def coordinate(ant):
    return (round(ant.xcor()), round(ant.ycor()))

langton()