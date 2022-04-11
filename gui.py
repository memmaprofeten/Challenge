#TODO:  Arrow key navigation
#       Refactor away globals and make names sensible
#       Add more empty days in hand.csv. What does this mean??
#       Nicer design

from appJar import gui
from numpy import genfromtxt

DAY = 1
START = 1
DONE = False
FINNISH_ORDINALS = {'1': 'Ensimmäinen',
        '2': 'Toinen', 
        '3':'Kolmas',
        '4':'Neljäs',
        '5':'Viides',
        '6':'Kuudes',
        '7':'Seitsemäs',
        '8':'Kahdeksas'}

def getDescription(challenge,day):
    with open("Text/"+challenge+"_"+str(day)+".txt") as text:
        return text.read()

def addImage(challenge, day, width, ordinal):
    description = getDescription(challenge, day)
    app.addImage(FINNISH_ORDINALS[str(ordinal)],challenge+"_"+str(day)+".gif")
    app.addMessage(FINNISH_ORDINALS[str(ordinal)],description)
    app.setMessageWidth(FINNISH_ORDINALS[str(ordinal)],width)

def changeImage(challenge,day,ordinal):
    description = getDescription(challenge,day)
    app.setImage(FINNISH_ORDINALS[str(ordinal)],challenge+"_"+str(day)+".gif")
    app.setMessage(FINNISH_ORDINALS[str(ordinal)],description)

def dispExercise(challenge, day):
    global DONE
    global DAYS
    DAYS = genfromtxt(challenge + '.csv',delimiter=',')
    for exercise in range(1,9):
        with app.labelFrame(FINNISH_ORDINALS[str(exercise)],2,exercise-1):
            app.setLabelFrameWidth(FINNISH_ORDINALS[str(exercise)],445)
            if int(DAYS[day-1,exercise-1])==0: #What does this mean?
                addImage(challenge, day, 445, exercise)
            else:
                addImage(challenge, int(DAYS[day-1,exercise-1]), 450, exercise)#Whats with the different size?
        if int(DAYS[day-1,exercise-1])==0:
            if exercise<3:
                DONE = True
            app.hideLabelFrame(FINNISH_ORDINALS[str(exercise)])
        if DONE:
            START = 1

def changeExercise(challenge, day, start):
    global DAYS
    for x in range(1,9):
        app.hideLabelFrame(FINNISH_ORDINALS[str(x)])
    for i in range(start, start + 3):
        if i>8:
            done = True
            start = 1
            return start, done
        app.showLabelFrame(FINNISH_ORDINALS[str(i)])
        if int(DAYS[day-1,i-1])==0:
            done = True
            app.hideLabelFrame(FINNISH_ORDINALS[str(i)])
            changeImage(challenge , day, i)
        else:
            done = False
            changeImage(challenge ,int(DAYS[day-1,i-1]),i)
    if int(DAYS[day-1,start+2]) == 0:
        done = True
    if done:
        start = 1

    return start, done                   

def orient(btn):
    global DAY
    global START
    global DONE
    if btn=="<":
        DAY -= 1
        if DAY == 0:
            DAY = 30
        app.setLabel("title","Päivä "+str(DAY))
        START, DONE = changeExercise(CHALLENGE, DAY, START)
    else:
        if not DONE:
            START += 3
        else:
            DAY += 1
            if DAY == 31:
                DAY = 1
        app.setLabel("title","Päivä "+str(DAY))
        START, DONE = changeExercise(CHALLENGE, DAY,START)
    

def startChallenge(button):
    global CHALLENGE
    day = 1
    app.removeButton("Handstand")
    app.removeButton("Split")
    app.setStretch("column")
    app.setSticky("n")
    app.startLabelFrame("Controls",0,0,9)
    app.addLabel("title","Päivä " + str(DAY),0,1)
    app.addButton("<",orient,0,0)
    app.addButton(">",orient,0,2)
    app.stopLabelFrame()
    if button == "Handstand":
        CHALLENGE = "hand"
    else:
        CHALLENGE = "spagat"
    dispExercise(CHALLENGE,day)
def startApp():
    global app
    with gui("Challenge center") as app:
        app.setFont(10)
        app.setBg('white')
        app.setImageLocation("Pics/small")
        app.addButton("Handstand",startChallenge,0,0)
        app.addButton("Split",startChallenge,1,0)
        app.go()

