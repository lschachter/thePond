from Player import *

class Players:
    '''Deals with all the players in a given level'''
    def __init__(self,players):
        self.players = players

    def getPlayers(self):
        '''Returns the list of player items'''
        return self.players

    def checkAll(self):
        '''Returns a bool of whether they're all altruists
           and a bool of whether they're all egoists'''
        allAlt = True
        allEgo = True
        for player in self.players:
            if player.state == 0:
                allAlt = False
            else:
                allEgo = False
        return allAlt,allEgo

    def turnOff(self):
        '''deactivates all players'''
        for player in self.players:
            player.deactivate()

    def turnOn(self):
        '''activates all players'''
        for player in self.players:
            player.activate()


