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
x.bgcolor("black")
x.setup(1000,600)

y = turtle.Turtle()
y.color("white")
y.speed(0)
y.penup()
y.goto(-490,280)
y.write("Lets play Rock, Paper & Scissors....!!!!",font=20)
y.goto(-490,260)
y.write("For Rock,Paper & Scissors Press R , P & S ",font=20)

z = turtle.Turtle()
z.color("white")
z.speed(0)
z.penup()
z.goto(-490,220)
z.write("Sahilpoint = {} ||  Computerpoint = {}".format(score,compscore),font= 80)

def Rock():
    compinput= Glist[random.randint(0,2)]
    global abc
    if compinput == "Rock":
         abc = 10
         y.clear()
         y.goto(-490,280)
         y.write("Lets play Rock, Paper & Scissors....!!!!",font=20)
         y.goto(-490,260)
         y.write("For Rock,Paper & Scissors Press R , P & S ",font=20)
         y.goto(100,0)
         y.write("You Won !!! ",font= 50)
    if compinput != "Rock": 
         abc = -10
         y.clear()
         y.goto(-490,280)
         y.write("Lets play Rock, Paper & Scissors....!!!!",font=20)
         y.goto(-490,260)
         y.write("For Rock,Paper & Scissors Press R , P & S ",font=20)
         y.goto(100,0)
         y.write("Ooooppps! You Lose !",font= 50)

def Paper():
     compinput= Glist[random.randint(0,2)]
     global abc
     if compinput == "Paper":
         abc = 20
         y.clear()
         y.goto(-490,280)
         y.write("Lets play Rock, Paper & Scissors....!!!!",font=20)
         y.goto(-490,260)
         y.write("For Rock,Paper & Scissors Press R , P & S ",font=20)
         y.goto(100,0)
         y.write("You Won !!! ",font= 50) 
     if compinput != "Paper":
         abc = -20
         y.clear()
         y.goto(-490,280)
         y.write("Lets play Rock, Paper & Scissors....!!!!",font=20)
         y.goto(-490,260)
         y.write("For Rock,Paper & Scissors Press R , P & S ",font=20)
         y.goto(100,0)
         y.write("Ooooppps! You Lose !",font= 50)

def Scissors():
     compinput= Glist[random.randint(0,2)]
     global abc
     if compinput == "Scissors":
         abc = 30 
         y.clear()
         y.goto(-490,280)
         y.write("Lets play Rock, Paper & Scissors....!!!!",font=20)
         y.goto(-490,260)
         y.write("For Rock,Paper & Scissors Press R , P & S ",font=20)
         y.goto(100,0)
         y.write("You Won !!! ",font= 50)
     if compinput != "Scissors":
         abc = -30
         y.clear()
         y.goto(-490,280)
         y.write("Lets play Rock, Paper & Scissors....!!!!",font=20)
         y.goto(-490,260)
         y.write("For Rock,Paper & Scissors Press R , P & S ",font=20)
         y.goto(100,0)
         y.write("Ooooppps! You Lose !",font= 50)


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
