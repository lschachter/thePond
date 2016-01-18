#ButtonClass.py
from graphics import *
import math

class Button:

    """A button is a labeled rectangle in a window.
    It is enabled or disabled with the activate()
    and deactivate() methods. The isClicked(pt) method
    returns true if the button is enabled and pt is inside it."""

    def __init__(self, win, center, width, height, color, label):
        """ Creates a rectangular button, eg:
        qb = Button(myWin, centerPoint, width, height, "black", 'Quit') """ 

        self.w,self.h = width/2.0, height/2.0
        self.center=center
        x,y = center.getX(), center.getY()
        self.xmax, self.xmin = x+self.w, x-self.w
        self.ymax, self.ymin = y+self.h, y-self.h
        self.color=color
        self.lColor='white'
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill(self.color)
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.setFill(self.lColor)
        self.rect.setOutline('tomato')
        self.label.draw(win)
        self.active = True
        self.win=win

    def isClicked(self, pt):
        "Returns true if button active and pt is inside"
        return (self.active and
                self.xmin <= pt.getX() <= self.xmax and
                self.ymin <= pt.getY() <= self.ymax)

    def getLabel(self):
        "Returns the label string of this button."
        return self.label.getText()

    def activate(self):
        "Sets this button to 'active'."
        self.rect.setOutline('tomato')
        self.active = True
        self.label.setFill(self.lColor)

    def choose(self):
        '''Alters the look of the button to show it's been selected'''
        self.rect.setFill("DarkGray")
        self.rect.setWidth(2)

    def unchoose(self):
        '''Resets the look of the button once another has been chosen'''
        self.label.setFill(self.lColor)
        self.rect.setFill(self.color)
        self.rect.setWidth(1)        

    def deactivate(self):
        "Sets this button to 'inactive'."
        self.rect.setOutline(self.color)
        self.active = False
        self.label.setFill('tomato')

    def setColor(self,color):
        '''Changes the button's color'''
        self.rect.setFill(color)

    def setText(self,label):
        '''Sets the text of the label'''
        self.label.setText(label)

    def setTextSize(self,size):
        '''Sets the size and face of the label'''
        self.label.setSize(size)

    def setTextStyle(self,style):
        '''Sets the style of the label'''
        self.label.setStyle(style)

    def setTextColor(self,color):
        '''Sets the color of the label'''
        self.lColor=color
        self.label.setFill(self.lColor)
        self.rect.setOutline('firebrick')

    def offSet(self,x,y):
        '''Offsets the label from the button'''
        self.label.move(x,y)

    def die(self):
        '''Effectively deletes the button'''
        self.active=False
        self.label.undraw()
        self.rect.undraw()

    def move(self,x1,y1):
        '''moves the button'''
        self.rect.move(x1,y1)
        self.label.move(x1,y1)
        x,y = self.xmin+self.w+x1,self.ymin+self.h+y1
        self.xmax, self.xmin = x+self.w, x-self.w
        self.ymax, self.ymin = y+self.h, y-self.h


