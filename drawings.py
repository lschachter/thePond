from graphics import *

def grass(win, point):
    ##draws 'grass'
    x = point.getX()
    y = point.getY()

    addx = -4
    addy = 3
    for i in range(4):
        line = Line(point, Point(x+addx,y+addy))
        line.draw(win)
        line.setFill('greenyellow')
        addx+=3



def wave(win,point,color,radius):
    ##draws 'waves'
    x = point.getX()
    y = point.getY()
    arc = Circle(Point(x-radius,y),radius)
    arc.draw(win)
    arc.setOutline('lightskyblue')
    arc = Circle(Point(x+radius,y),radius)
    arc.draw(win)
    arc.setOutline('lightskyblue')
    rect = Rectangle(Point(x-radius*2,y),Point(x+radius*2,y+radius))
    rect.draw(win)
    rect.setOutline(color)
    rect.setFill(color)
    
