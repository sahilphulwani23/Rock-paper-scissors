from tkinter import font
import turtle
import random

Glist = ["Rock","Paper","Scissors"]
score = 0
compscore = 0
abc =0
# compinput= Glist[random.randint(0,2)] #loop p work krne k liye bahar likha

x = turtle.Screen()
x.title("Rock, Paper & Scissors")
x.bgcolor("white")
x.setup(1000,600)
x.register_shape('rock.gif')
x.register_shape('paper.gif')
x.register_shape('scissors.gif')

y = turtle.Turtle()
y.color("black")
y.speed(0)
y.penup()
y.goto(-490,280)
y.write("Lets play Rock, Paper & Scissors....!!!!",font=20)
y.goto(-490,260)
y.write("For Rock,Paper & Scissors Press R , P & S ",font=20)

z = turtle.Turtle()
z.color("black")
z.speed(0)
z.penup()
z.goto(-490,220)
z.write("Sahilpoint = {} ||  Computerpoint = {}".format(score,compscore),font= 80)

myimg = turtle.Turtle()
myimg.penup()
myimg.speed(0)

compimg = turtle.Turtle()
compimg.penup()
compimg.speed(0)



def Rock():
    compinput= Glist[random.randint(0,2)]
    myimg.goto(-250,0)
    myimg.shape('rock.gif')
    global abc
    if compinput == "Rock":
         abc = 10
         y.clear()
         y.goto(-490,280)
         y.write("Lets play Rock, Paper & Scissors....!!!!",font=20)
         y.goto(-490,260)
         y.write("For Rock,Paper & Scissors Press R , P & S ",font=20)
         y.goto(100,0)
         compimg.goto(250,0)
         compimg.shape('rock.gif')
        #  y.write("You Won !!! ",font= 50)
    if compinput != "Rock": 
         abc = -10
         y.clear()
         y.goto(-490,280)
         y.write("Lets play Rock, Paper & Scissors....!!!!",font=20)
         y.goto(-490,260)
         y.write("For Rock,Paper & Scissors Press R , P & S ",font=20)
         y.goto(100,0)
         if compinput == "Paper":
             compimg.goto(250,0)
             compimg.shape('paper.gif')
         else :
             compimg.goto(250,0)
             compimg.shape('scissors.gif')

        #  y.write("Ooooppps! You Lose !",font= 50)

def Paper():
     compinput= Glist[random.randint(0,2)]
     myimg.goto(-250,0)
     myimg.shape('paper.gif')
     global abc
     if compinput == "Paper":
         abc = 20
         y.clear()
         y.goto(-490,280)
         y.write("Lets play Rock, Paper & Scissors....!!!!",font=20)
         y.goto(-490,260)
         y.write("For Rock,Paper & Scissors Press R , P & S ",font=20)
         y.goto(100,0)
         compimg.goto(250,0)
         compimg.shape('paper.gif')
        #  y.write("You Won !!! ",font= 50) 
     if compinput != "Paper":
         abc = -20
         y.clear()
         y.goto(-490,280)
         y.write("Lets play Rock, Paper & Scissors....!!!!",font=20)
         y.goto(-490,260)
         y.write("For Rock,Paper & Scissors Press R , P & S ",font=20)
         y.goto(100,0)
         if compinput == "Rock":
             compimg.goto(250,0)
             compimg.shape('rock.gif')
         else :
             compimg.goto(250,0)
             compimg.shape('scissors.gif')
        #  y.write("Ooooppps! You Lose !",font= 50)

def Scissors():
     compinput= Glist[random.randint(0,2)]
     myimg.goto(-250,0)
     myimg.shape('scissors.gif')
     global abc
     if compinput == "Scissors":
         abc = 30 
         y.clear()
         y.goto(-490,280)
         y.write("Lets play Rock, Paper & Scissors....!!!!",font=20)
         y.goto(-490,260)
         y.write("For Rock,Paper & Scissors Press R , P & S ",font=20)
         y.goto(100,0)
         compimg.goto(250,0)
         compimg.shape('scissors.gif')
        #  y.write("You Won !!! ",font= 50)
     if compinput != "Scissors":
         abc = -30
         y.clear()
         y.goto(-490,280)
         y.write("Lets play Rock, Paper & Scissors....!!!!",font=20)
         y.goto(-490,260)
         y.write("For Rock,Paper & Scissors Press R , P & S ",font=20)
         y.goto(100,0)
        #  y.write("Ooooppps! You Lose !",font= 50)
         if compinput == "Rock":
             compimg.goto(250,0)
             compimg.shape('rock.gif')
         else :
             compimg.goto(250,0)
             compimg.shape('paper.gif')

x.listen()
x.onkey(Rock, "r")
x.onkey(Paper, "p")
x.onkey(Scissors, "s")

while True:
    x.update()
    # z.write("Sahilpoint = {} ||  Computerpoint = {}".format(score,compscore),font= 80)
    if abc == 10:
        z.clear()
        score = score + 10
        z.write("Sahilpoint = {} ||  Computerpoint = {}".format(score,compscore),font= 80)
        abc = 0
    if abc == -10:
        z.clear()
        compscore = compscore + 10
        z.write("Sahilpoint = {} ||  Computerpoint = {}".format(score,compscore),font= 80)
        abc = 0
    if abc == 20:
        z.clear()
        score = score + 10
        z.write("Sahilpoint = {} ||  Computerpoint = {}".format(score,compscore),font= 80)
        abc = 0
    if abc == -20:
        z.clear()
        compscore = compscore + 10
        z.write("Sahilpoint = {} ||  Computerpoint = {}".format(score,compscore),font= 80)
        abc = 0
    if abc == 30:
        z.clear()
        score = score + 10
        z.write("Sahilpoint = {} ||  Computerpoint = {}".format(score,compscore),font= 80)
        abc = 0
    if abc == -30:
        z.clear()
        compscore = compscore + 10
        z.write("Sahilpoint = {} ||  Computerpoint = {}".format(score,compscore),font= 80)
        abc = 0
