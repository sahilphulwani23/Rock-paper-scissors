import turtle
import random

Glist = ["Rock","Paper","Scissors"]
score = 0
compscore = 0
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
z.color("grey")
z.speed(0)
z.ht()
z.penup()
z.goto(-490,220)
z.write("Sahilpoint: 0 & Computerpoint: 0")

def Rock(score):
    compinput= Glist[random.randint(0,2)]
    if compinput == "Rock":
         y.clear()
         y.goto(-490,280)
         y.write("Lets play Rock, Paper & Scissors....!!!!",font=20)
         y.goto(-490,260)
         y.write("For Rock,Paper & Scissors Press R , P & S ",font=20)
         y.goto(100,0)
         y.write("You Won !!! ",font= 50)
         score += 10
         z.write("Sahilpoint = {} ||  Computerpoint = {}".format(score,compscore),font= 80)
    if compinput != "Rock":
         y.clear()
         y.goto(-490,280)
         y.write("Lets play Rock, Paper & Scissors....!!!!",font=20)
         y.goto(-490,260)
         y.write("For Rock,Paper & Scissors Press R , P & S ",font=20)
         y.goto(100,0)
         y.write("Ooooppps! You Lose !",font= 50)
         compscore += 10
         z.write("Sahilpoint = {} ||  Computerpoint = {}".format(score,compscore),font= 80)

def Paper(score,compscore):
     compinput= Glist[random.randint(0,2)]
     if compinput == "Paper":
         y.clear()
         y.goto(-490,280)
         y.write("Lets play Rock, Paper & Scissors....!!!!",font=20)
         y.goto(-490,260)
         y.write("For Rock,Paper & Scissors Press R , P & S ",font=20)
         y.goto(100,0)
         y.write("You Won !!! ",font= 50)
         score += 10
         z.write("Sahilpoint = {} ||  Computerpoint = {}".format(score,compscore),font= 80)
     if compinput != "Paper":
         y.clear()
         y.goto(-490,280)
         y.write("Lets play Rock, Paper & Scissors....!!!!",font=20)
         y.goto(-490,260)
         y.write("For Rock,Paper & Scissors Press R , P & S ",font=20)
         y.goto(100,0)
         y.write("Ooooppps! You Lose !",font= 50)
         compscore += 10
         z.write("Sahilpoint = {} ||  Computerpoint = {}".format(score,compscore),font= 80)


def Scissors():
     compinput= Glist[random.randint(0,2)]
     if compinput == "Scissors":
         y.clear()
         y.goto(-490,280)
         y.write("Lets play Rock, Paper & Scissors....!!!!",font=20)
         y.goto(-490,260)
         y.write("For Rock,Paper & Scissors Press R , P & S ",font=20)
         y.goto(100,0)
         y.write("You Won !!! ",font= 50)
         score += 10
         z.write("Sahilpoint = {} ||  Computerpoint = {}".format(score,compscore),font= 80)
     if compinput != "Scissors":
         y.clear()
         y.goto(-490,280)
         y.write("Lets play Rock, Paper & Scissors....!!!!",font=20)
         y.goto(-490,260)
         y.write("For Rock,Paper & Scissors Press R , P & S ",font=20)
         y.goto(100,0)
         y.write("Ooooppps! You Lose !",font= 50)
         compscore += 10
         z.write("Sahilpoint = {} ||  Computerpoint = {}".format(score,compscore),font= 80)


x.listen()
x.onkey(Rock, "r")
x.onkey(Paper, "p")
x.onkey(Scissors, "s")

while True:
    x.update()

