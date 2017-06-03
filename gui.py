#TODO:  Arrow key navigation
#       Nicer design

from appJar import gui
from numpy import genfromtxt

day = 1
start = 1
done = False
def dispExercise():
    global day
    global days
    global done
    stufa = {'1': 'Ensimmäinen','2': 'Toinen', '3':'Kolmas','4':'Neljäs','5':'Viides','6':'Kuudes','7':'Seitsemäs','8':'Kahdeksas'}
    days = genfromtxt(challenge + '.csv',delimiter=',')
    for i in range(1,9):
        app.startLabelFrame(stufa[str(i)],2,i-1)
        app.setLabelFrameWidth(stufa[str(i)],445)
        if int(days[day-1,i-1])==0:
            with open("Text/"+challenge+"_"+str(day)+".txt") as text:
                data = text.read()
            app.addImage(stufa[str(i)],challenge+"_"+str(day)+".gif")
            app.addMessage(stufa[str(i)],data)
            app.setMessageWidth(stufa[str(i)],445)
        else:
            app.addImage(stufa[str(i)],challenge+"_"+str(int(days[day-1,i-1]))+".gif")
            with open("Text/"+challenge+"_"+str(int(days[day-1,i-1]))+".txt") as text:
                data = text.read()
            app.addMessage(stufa[str(i)],data)
            app.setMessageWidth(stufa[str(i)],450)
        app.stopLabelFrame()
        if int(days[day-1,i-1])==0:
            if i<3:
                done = True
            app.hideLabelFrame(stufa[str(i)])
        if done:
            start = 1

def changeExercise():
    global day
    global days
    global start
    global done
    stufa = {'1': 'Ensimmäinen','2': 'Toinen', '3':'Kolmas','4':'Neljäs','5':'Viides','6':'Kuudes','7':'Seitsemäs','8':'Kahdeksas',}
    for x in range(1,9):
        app.hideLabelFrame(stufa[str(x)])
        print("Hiding ",stufa[str(x)])
    for i in range(start,start+3):
        if i>8:
            done = True
            start = 1
            return
        app.showLabelFrame(stufa[str(i)])
        print("Showing ",stufa[str(i)])
        #app.showImage(stufa[str(i)])
        if int(days[day-1,i-1])==0:
            done = True
            app.hideLabelFrame(stufa[str(i)])
            #app.hideImage(stufa[str(i)])
            app.setImage(stufa[str(i)],challenge+"_"+str(day)+".gif")
            with open("Text/"+challenge+"_"+str(day)+".txt") as text:
                data = text.read()
            app.setMessage(stufa[str(i)],data)
        else:
            done = False
            app.setImage(stufa[str(i)],challenge+"_"+str(int(days[day-1,i-1]))+".gif")
            with open("Text/"+challenge+"_"+str(int(days[day-1,i-1]))+".txt") as text:
                data = text.read()
            app.setMessage(stufa[str(i)],data)
    if int(days[day-1,start+2]) == 0:
        done = True
    if done:
        start = 1

def orient(btn):
    global day
    global start
    if btn=="<":
        day -= 1
        if day == 0:
            day = 30
        app.setLabel("title","Päivä "+str(day))
        changeExercise()
    else:
        if not done:
            start += 3
            print("START is " + str(start))
        else:
            day += 1
            if day == 31:
                day = 1
        app.setLabel("title","Päivä "+str(day))
        changeExercise()
    

def startChallenge(button):
    global challenge
    app.removeButton("Handstand")
    app.removeButton("Split")
    app.setStretch("column")
    app.setSticky("n")
    app.startLabelFrame("Controls",0,0,9)
    app.addLabel("title","Päivä " + str(day),0,1)
    app.addButton("<",orient,0,0)
    app.addButton(">",orient,0,2)
    app.stopLabelFrame()
    if button == "Handstand":
        challenge = "hand"
    else:
        challenge = "spagat"
    dispExercise()

app = gui("Challenge center")
app.setFont(10)
app.setImageLocation("Pics/small")
app.addButton("Handstand",startChallenge,0,0)
app.addButton("Split",startChallenge,1,0)
app.go()
