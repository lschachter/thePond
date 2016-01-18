from ButtonClass import *
from drawings import *
import webbrowser
from Players import *

        
def welcome(win):
    ####Instructions####
    intro = Text(Point(0,30),"Welcome to the Pond! \n\nYou are a community leader\
 in this pond-side village, with the power to change a single--\n\n\
but perhaps very influential-- villager\'s tendencies\n\n\
from egoistic to altruistic or vice versa. You want what\'s best for the \
village, \n\nso your goal is to make it so that everyone wants to be an\
altruist. \n\nBut be careful: if everyone's an egoist, no one's happy.\
\n\nLet's play!")
    intro.draw(win)
    intro.setFill('firebrick')
    intro.setSize(20)
    intro2=Text(Point(0,-43),"Note: Altruists put 1 positivity point in the world,\
 at a cost of 0.3 to themselves. \n\nEgoists put nothing into the world, but at \
no cost to themselves")
    intro2.draw(win)
    intro2.setFill('firebrick')
    intro2.setSize(16)
    ####Buttons!####
    gameB=Button(win, Point(-30,-20),30,20,'gray','Play Game')
    testB = Button(win,Point(30,-20),30,20,'gray','Infinity Round')
    gameB.setTextSize(20)
    gameB.setColor('tomato')
    gameB.setTextColor('white')
    testB.setTextSize(20)
    testB.setColor('tomato')
    testB.setTextColor('white')
    ####gets click for while loop######
    pt=win.getMouse()
    while not gameB.isClicked(pt) and not testB.isClicked(pt):
        pt=win.getMouse()

    intro.undraw()
    intro2.undraw()
    if gameB.isClicked(pt):
        testB.die()
        gameB.die()
        return 6,1,True
    else:
        ###if Infinity round was picked, get user inputs###
        inst1 = Text(Point(-30,30),"Enter the number of people in your village:  ")
        inst1.draw(win)
        inst1.setFill('firebrick')
        inst1.setSize(20)
        getN = Entry(Point(20,30),10)
        getN.draw(win)
        getN.setFill('tomato')
        getN.setTextColor('white')
        inst2 = Text(Point(-30,10),"Enter the depth* of each neighborhood:  ")
        inst2.draw(win)
        inst2.setFill('firebrick')
        inst2.setSize(20)
        inst3= Text(Point(0,-40),"* the number of people on each side of you that effect your score")
        inst3.draw(win)
        inst3.setFill('firebrick')
        inst3.setSize(16)
        getNei = Entry(Point(20,10),10)
        getNei.draw(win)
        getNei.setFill('tomato')
        getNei.setTextColor('white')
        getN.setText(10)
        getNei.setText(1)
        testB.die()
        gameB.move(30,0)
        errorText=Text(Point(0,50),'')
        errorText.draw(win)
        errorText.setFill("firebrick")
        errorText.setSize(20)
        pt=win.getMouse()
        ready = False
        ###Continues to get input until both are numbers###
        while not ready:
            if gameB.isClicked(pt):
                try:
                    n = round(eval(getN.getText()))
                    nei = round(eval(getNei.getText()))
                    ready=True
                    break
                except NameError:
                    errorText.setText("You did not enter in a number. Try again.")

                except SyntaxError:
                    errorText.setText("You did not enter in a number. Try again.")
            pt=win.getMouse()

        gameB.die()
        inst1.undraw()
        inst2.undraw()
        inst3.undraw()
        getN.undraw()
        getNei.undraw()
        errorText.undraw()
        return n,nei, False


def level(win,inst,factor,struct1,struct2,n,numNei,switched,sender,gob,dispb,quitb,backb,maxHits):
    ###sets up the instructions of the level###
    inst.setText(struct1)
    inst2 = Text(Point(0,-40),struct2)
    inst2.draw(win)
    inst2.setFill('firebrick')
    inst2.setSize(20)
    alt=''
    ego=''
    x = 1
    y = 1
    ###creates pond###
    pond = Oval(Point(x*factor,y*factor),Point(x*-1*factor,y*-1*factor))
    pond.draw(win)
    pond.setFill('dodgerblue')
    pond.setOutline('dodgerblue')
    for i in range (4):
        wave(win,Point(randrange(x*-1*factor*.6,x*factor*.6),randrange(y*-1*factor*.5,y*factor*.5)),'dodgerblue',2)

    ###creates players, initiates players class###
    plays=[]
    for i in range(1,n+1):
        xLoc = floor((factor+factor*.5)*cos(((pi*2)/n)*i)+x)
        yLoc = floor((factor+factor*.5)*sin(((pi*2)/n)*i)+y)
        p = Player(win,1,Point(xLoc,yLoc),.3,i-1)
        plays.append(p)
    
    playing = Players(plays)
    players = playing.getPlayers()

    ###creates set of neighbors for each player###
    for i in range(len(players)):
        neis=[]
        for j in range(1,numNei+1):
            nei=players[(i-j)%len(players)]
            if nei not in neis and nei != players[i]:
                neis.append(nei)
            nei = players[(i+j)%len(players)]
            if nei not in neis and nei != players[i]:
                neis.append(nei)
            
        players[i].setNeis(neis)
    ###switches the given set of players to egoists###
    for i in switched:
        players[i].switch()

     
    pt=win.getMouse()
    nextText = Text(Point(0,-48),"")
    nextText.draw(win)
    nextText.setSize(20)
    nextText.setFill('firebrick')
    numHits=0
    ###runs game based on click###
    while not quitb.isClicked(pt):
        if numHits >=maxHits:
            playing.turnOff()
            numHits=0
        if dispb.isClicked(pt):
            for i in range(len(players)):
                players[i].payoff()
                players[i].displayPayoff()

            dispb.deactivate()
        elif backb.isClicked(pt):
                n,numNei, game = welcome(win)
        elif gob.isClicked(pt):
            ###if they won, send to next level###
            if alt ==True:
                for p in players:
                    p.undraw()
                nextText.setText("")
                level(win,inst,factor+10,"You can now change two people's choices each round. \n\n\
Each person's neighborhood has also gotten bigger: two people on each side.","",10,2,[0,1,2,6],'YOU WON!',gob,dispb,quitb,backb,2)
                return ''
            ###if they lost, reset the current level###
            elif ego ==True:
                nextText.setText("")
                inst2.undraw()
                for p in players:
                    p.undraw()
                gob.setText('GO')
                level(win,inst,factor,inst.getText(),inst2.getText(),n,numNei,switched,sender,gob,dispb,quitb,backb,maxHits)
                return ''

            ###averages the players (checking payoff and reseting it after)###
            for p in players:
                p.payoff()
            for p in players:
                p.avg()
            for p in players:
                p.payoff()
            playing.turnOn()
            dispb.activate()
            ###checks if won or lost###
            alt,ego = playing.checkAll()
            ###displays win/loss information###
            if alt == True:
                inst.setText("")
                inst2.undraw()
                nextText.setText("Congratulations! Everyone's an altruist. "+sender)
                if sender =="YOU WON!":
                    gob.deactivate()
                else:
                    gob.setText('NEXT')
            if ego == True:
                nextText.setText("Everyone's miserable. Try again.")
                playing.turnOff()
                gob.setText("RETRY")
        ###switches clicked player/s###             
        for p in players:
            if p.isClicked(pt):
                p.switch()
                numHits+=1
        pt=win.getMouse()

    win.close()


def infinite(win,factor,inst,n,numNei,gob,dispb,quitb,backb):
    ###does much of the same as above with just enough changes that I
    ###copied and altered
    inst.setText("Play to your heart's content! \n\nBe sure to look \
for patterns by pressing 'GO' twice without changing anything-- if you \n\n\
find one that switches back and forth every time, you've found an                           ")
    x = 1
    y = 1
    offset = 0
    absb = Button(win,Point(56,45),28,10,'yellowgreen',"'Absorbing Set!'")
    absb.setTextSize(20)
    absb.setTextColor('firebrick')
    if n > 10:
        factor+=10
        offset = 6

    pond = Oval(Point(x*factor,y*factor),Point(x*-1*factor,(y*-1*factor)-offset))
    pond.draw(win)
    pond.setFill('dodgerblue')
    pond.setOutline('dodgerblue')

    for i in range (4):
        wave(win,Point(randrange(x*-1*factor*.6,x*factor*.6),randrange(y*-1*factor*.5,y*factor*.5)),'dodgerblue',2)

    players=[]
    for i in range(1,n+1):
        xLoc = floor((factor+factor*.5)*cos(((pi*2)/n)*i)+x)
        yLoc = floor((factor+factor*.5)*sin(((pi*2)/n)*i)+y)
        p = Player(win,1,Point(xLoc,yLoc-offset),.3,i-1)
        players.append(p)

    for i in range(len(players)):
        neis=[]
        for j in range(1,numNei+1):
            nei=players[(i-j)%len(players)]
            if nei not in neis and nei != players[i]:
                neis.append(nei)
            nei = players[(i+j)%len(players)]
            if nei not in neis and nei != players[i]:
                neis.append(nei)

        players[i].setNeis(neis)
    pt=win.getMouse()
    while not quitb.isClicked(pt):
        ###offers the link###
        if absb.isClicked(pt):
            webbrowser.open_new("http://isites.harvard.edu/fs/docs/icb.topic881116.files/2052_2011_lecture%2012.pdf")
        elif backb.isClicked(pt):
            n,numNei, game = welcome(win)
        elif dispb.isClicked(pt):
            for i in range(len(players)):
                players[i].payoff()
                players[i].displayPayoff()

            dispb.deactivate()
        elif gob.isClicked(pt):

            for p in players:
                p.avg()

            for p in players:
                p.payoff()
            dispb.activate()
                
        for p in players:
            if p.isClicked(pt):
                p.switch()
        pt=win.getMouse()

    win.close()

def makeWindow():
    ###Sets up window and instructions for later use###
    win = GraphWin("The Pond",800,600)
    win.setCoords(-75,-55,75,75)
    win.setBackground('yellowgreen')
    for i in range(25):
        grass(win, Point(randrange(-70,70),randrange(-50,70)))
    inst = Text(Point(0,55),"")
    inst.draw(win)
    inst.setSize(20)
    inst.setFill('firebrick')
    ####Returns whether the user chose inifinity round or game###
    n,numNei, game= welcome(win)
    quitb = Button(win, Point(-68,-45),10,10,'firebrick','Quit')
    gob=Button(win,Point(62,0),10,10,'firebrick','GO')
    dispb=Button(win,Point(-62,0),10,10,'firebrick','Display\nPayoffs')
    backb = Button(win,Point(68,-48),10,10,'firebrick','Back')
    backb.die()
    ####Plays user's choice###
    if game == False:
        infinite(win,factor,inst,n,numNei,gob,dispb,quitb,backb)
    else:
        level(win,inst,20,"You can change one person's choice each round. \n\n\
When you click 'GO', each villager will look at his/her neighborhood--\
\n\nin this case, the person on either side of them-- and average the \
amount \n\nthat egoists in their neighborhood receive vs the amount\
altruists receive.", "If the average of the other type is higher than his/hers,\n\
that player will switch when you press go. Hit 'Display Payoffs' for help.",n,numNei,[0,3],"Click 'NEXT'.",gob,dispb,quitb,backb,1)

