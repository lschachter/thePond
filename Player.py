from graphics import *
from math import *
from random import *

class Player:
    '''A Player is either an egoit or an altruist'''
    def __init__(self, win,state,center,c,i):
        '''Sets up graphical depiction and inherent info of player'''
        self.index=i
        self.state=state
        ###Info reliant on state (egoist vs altruist)###
        self.states = ['E','a']
        self.cees = [0,c]
        self.adds = [0,1]
        self.cols = ['firebrick','tomato']
        #####GUI depiction#####
        self.win = win
        self.center=center
        self.x = center.getX()
        self.y = center.getY()
        self.radius = 3
        self.pic = Circle(center,self.radius)
        self.pic.setFill(self.cols[self.state])
        self.pic.draw(win)
        self.pic.setOutline('white')
        self.label=Text(center,self.states[self.state])
        self.label.draw(win)
        self.label.setFill('white')
        ###booleans for display, state-setting, and whether or not it
        ###needs to change after all the averages have been taken###
        self.on=False
        self.active = True
        self.neighbors=[]
        self.change=False
        self.pay=0

    def switchDisplay(self):
        '''Switches the display of a changing player
        without changing his state, so that none of the
        averages are affected by the change until after
        the round finishes'''
        self.label.setText(self.states[(self.state+1)%2])
        self.pic.setFill(self.cols[(self.state+1)%2])
        self.change=True

    def switch(self):
        '''Changes everything about the player, on a manual
        click-switch'''
        self.state=(self.state+1)%2
        self.label.setText(self.states[self.state])
        self.pic.setFill(self.cols[self.state])
        self.payoff()
        ###alters the neighbors' payoffs accordingly###
        for nei in self.neighbors:
            nei.payoff()
        self.payoff()
        if self.on ==True:
            self.clearPay()
            self.displayPayoff()
            for neigh in self.neighbors:
                neigh.clearPay()
                neigh.payoff()
                neigh.displayPayoff()

    def getAdd(self):
        '''returns the add of the player'''
        return self.adds[self.state]

    def clearPay(self):
        '''Clears the payoff info from the screen
        and turns self.on off'''
        self.info.undraw()
        self.line.undraw()
        self.on = False

    def activate(self):
        '''activates it for manual switching'''
        self.active=True

    def deactivate(self):
        '''deactivates it for manual switching'''
        self.active = False

    def setNeis(self,neis):
        '''sets the neighbors of the player and finds
        the according payoff'''
        self.neighbors=neis
        self.payoff()

    def payoff(self):
        '''calculates the payoff of the player; takes into
        account whether or not the state has changed during
        the last averaging'''
        if self.change==True:
            self.state=(self.state+1)%2
            self.change=False
        self.pay=0
        for nei in self.neighbors:
            if nei.change == True:
                nei.state = (nei.state+1)%2
                nei.change=False
            self.pay += nei.getAdd()
        self.pay = self.pay - self.cees[self.state]

    def displayPayoff(self):
        '''Draws the payoff info of the player on the screen'''
        self.line = Line(Point(self.x-self.radius,self.y),Point(self.x-self.radius*2,self.y))
        self.line.draw(self.win)
        self.line.setWidth(5)
        self.line.setArrow('last')
        self.line.setFill(self.cols[self.state])
        self.info = Text(Point(self.x-self.radius*3,self.y),str(self.pay))
        self.info.setFill('firebrick')
        self.info.setStyle('bold')
        self.info.draw(self.win)
        self.on=True

    def undraw(self):
        '''undraws the player (and player info if it's on)'''
        self.pic.undraw()
        self.label.undraw()
        if self.on:
            self.line.undraw()
            self.info.undraw()

    def avg(self):
        '''averages the payoffs of your community and compares
        the egoists to the altruists. If the other state's average
        is higher than yours, self.change is set to true so that
        the payoff doesn't change before the next neighbor's payoff
        is changed, but self.payoff() knows to switch the state
        before recalculating the payoff'''
        you = []
        other = []
        you.append(self.pay)
        for nei in self.neighbors:
            if self.state == nei.state:
                you.append(nei.pay)
            else:
                other.append(nei.pay)
        youAv = sum(you)/len(you)           
        otherAv = sum(other)/(max(len(other),1))

        if self.on == True:
            self.clearPay()           
        if youAv < otherAv and len(other)!=0:
            self.switchDisplay()

    def __str__(self):
        '''returns info about the player and it's neighbors for printing'''
        neibs=''
        for nei in self.neighbors:
            neibs+= str(nei.pay)+', '
        return self.states[self.state]+'--'+str(self.index)+': '+str(self.pay)+', '+neibs


    def isClicked(self,pt):
        '''Returns whether or not the player can and has been clicked'''
        px = pt.getX()
        py = pt.getY()
        return (self.active and
                (self.x-self.radius) <= px <=(self.x+self.radius) and
            (self.y - self.radius) <=py <=(self.y+self.radius))

    
