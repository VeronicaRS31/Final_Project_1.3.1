#this is an interactive story game
# you're trapped in a house, and in order to leave you need to pick the right doors.
#  But if you dont then you need to do some tasks as punishments

# importing some modules
import turtle as trtl 
import random as rand

# seeting up variables for game and setting up turtles
eight_ball= trtl.Turtle(shape="circle")
screen_writer= trtl.Turtle()
score_keeper= trtl.Turtle()
restart_button= trtl.Turtle()
maze_runner=trtl.Turtle(shape="turtle")
maze=trtl.Turtle(shape="arrow")
timer= 60
counter_interval=1000
timer_up=False
counter=trtl.Turtle()
font_setup = ("Arial", 30, "normal")
wn= trtl.Screen()
wn.bgcolor("lavender")
screen_writer=trtl.Turtle()
wn= trtl.Screen()
wn.addshape("scissors.gif")
wn.addshape("paper.gif")
wn.addshape("rock.gif")


scissors_shape_c=trtl.Turtle()
scissors_shape_c.shape("scissors.gif")
scissors_shape_c.hideturtle()

def draw_scissors():
  scissors_shape_c.pu()
  scissors_shape_c.goto(-200,-25)
  scissors_shape_c.showturtle()
  

scissors_shape_p =trtl.Turtle()
scissors_shape_p.shape("scissors.gif")
scissors_shape_p.hideturtle()

def mine_scissors():
  scissors_shape_p.pu()
  scissors_shape_p.goto(200,-25)
  scissors_shape_p.showturtle()


rock_shape_c =trtl.Turtle()
rock_shape_c.shape("rock.gif")
rock_shape_c.hideturtle()

def draw_rock():
  rock_shape_c.pu()
  rock_shape_c.goto(-200,-25)
  rock_shape_c.showturtle()
  
rock_shape_p =trtl.Turtle()
rock_shape_p.shape("rock.gif")
rock_shape_p.hideturtle()

def mine_rock():
  rock_shape_p.pu()
  rock_shape_p.goto(200,-25)
  rock_shape_p.showturtle()
  


paper_shape_c=trtl.Turtle()
paper_shape_c.shape("paper.gif")
paper_shape_c.hideturtle()

def draw_paper():
  paper_shape_c.pu()
  paper_shape_c.goto(-200,-25)
  paper_shape_c.showturtle()

paper_shape_p=trtl.Turtle()
paper_shape_p.shape("paper.gif")
paper_shape_p.hideturtle()

def mine_paper():
  paper_shape_p.pu()
  paper_shape_p.goto(200,-25)
  paper_shape_p.showturtle()








def circles(radius):
  eight_ball.pd()
  eight_ball.begin_fill()
  eight_ball.circle(radius)
  eight_ball.end_fill()
  eight_ball.pu()

def button_click(x,y):
  restart_button.hideturtle()
  screen_writer.clear()


  
def button(re_button):
  re_button.hideturtle
  re_button.fillcolor("yellow")
  re_button.turtlesize(5)
  re_button.pu()
  re_button.shape("square")
  re_button.goto(650,150)
  restart_button.showturtle()
  screen_writer.pu()
  screen_writer.goto(450,125)
  screen_writer.write("Restart Button:",align="center",font= font_setup)
  restart_button.onclick(button_click)


def upside_down_triangle():
  eight_ball.pencolor("white")
  eight_ball.penup()
  eight_ball.goto(50,-250)
  eight_ball.pd()
  eight_ball.fillcolor("white")
  eight_ball.begin_fill()
  eight_ball.left(120)
  eight_ball.forward(350)
  eight_ball.right(120)
  eight_ball.forward(350)
  eight_ball.end_fill()


score= 30
score_update=False
def score_decrease():#this takes 1 point of your score
  global score
  score= score-1

def score_drawn(): #this updates the score
  global score_update
  score_update= True
  score_keeper.pu()
  score_keeper.goto(-400,300)
  score_keeper.write("Score:"+ str(score), font= font_setup)
  if score_update==True:
    score_keeper.clear()
    score_decrease()
    score_keeper.write("Score:"+ str(score), font= font_setup)
  

#this is the first mini game
def mini_game_1():
  eight_ball.speed(0)
  screen_writer.pu()
  screen_writer.goto(-350,250)
  screen_writer.write("This is your first punishment task, 8 ball game",font=font_setup)
  eight_ball.pu()
  eight_ball.fillcolor("black")
  eight_ball.goto(50,-350)
  circles(300)
  eight_ball.fillcolor("gray")
  eight_ball.goto(50,-250)
  circles(200)
  upside_down_triangle()
  messages=["yes","no","maybe","later","try again"]
  output= rand.choice(messages)
  screen_writer.pu()
  screen_writer.goto(-15,-85)
  screen_writer.write(output,font=font_setup)
  not_yes=False
  while not_yes== False:
    if output!="yes":
      score_drawn()
      button(restart_button)
      screen_writer.goto(-15,-85)
      output=rand.choice(messages)
      screen_writer.write(output,font=font_setup)
    elif output=="yes":
      not_yes=True



letters_words=["ALPE","OWLB","KDIS","INCO"]

def draw_timer():
  counter.pu()
  counter.goto(400,300)
  counter.write(timer,font= ("Arial",30,"normal"))

AlPE_options=["LEAP","PALE","PLEA","PEAL"]
OWLP_options=["BOWL","BLOW"]
KDIS_options=["KIDS","SKID","DISK"]
INCO_options=["ICON","COIN"]

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=("Arial",30,"normal"))
    timer_up = True
    screen_writer.clear()
    print("you lost")
  elif word_guessed== True:
    timer_up== True
  else:
    counter.write("Timer: " + str(timer), font=("Arial",30,"normal"))
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 



def mini_game_2():
  font_setup = ("Arial",30, "normal")
  score_keeper.pu()
  score_keeper.goto(-400,300)
  score_keeper.write("Score:"+ str(score), font= font_setup)
  font_setup = ("Arial", 20, "normal")
  screen_writer.pu()
  screen_writer.goto(-450,200)
  screen_writer.write("This is a punishment task, you have to unscrable the letters to make a 4 letter word", font= font_setup)
  font_setup = ("Arial", 90, "normal")
  screen_writer.goto(-125,-100)
  choice=rand.choice(letters_words)
  screen_writer.write(choice,font=font_setup)
  global word_guessed
  word_guessed=False
  while word_guessed==False and score>0:
    draw_timer()
    countdown()
    scramble_answer= input("So, What 4 letter word can you make with these letters").upper().strip()
    if choice=="ALPE":
      if scramble_answer in AlPE_options:
        print("correct")
        screen_writer.clear()
        word_guessed= True
      else:
        print("incorect")
        score_drawn()
    if choice=="KDIS":
      if scramble_answer in KDIS_options:
        print("correct")
        screen_writer.clear()
        word_guessed= True
      else:
        print("incorect")
        score_drawn()
    if choice=="INCO":
      if scramble_answer in INCO_options:
        print("correct")
        screen_writer.clear()
        word_guessed= True
      else:
        print("incorect")
        score_drawn()
    if choice=="OWLB":
      if scramble_answer in OWLP_options:
        print("correct")
        screen_writer.clear()
        word_guessed= True
      else:
        print("incorect")
        score_drawn()

def arena():
  screen_writer.pu()
  screen_writer.goto(-225,325)
  font_setup = ("Arial", 30, "normal")
  screen_writer.write("Lets play rock, paper,scissors!!", font=font_setup)
  screen_writer.pu()
  screen_writer.goto(-350,-350)
  screen_writer.pd()
  for i in range(2):
    screen_writer.forward(800)
    screen_writer.left(90)
    screen_writer.forward(600)
    screen_writer.left(90)
  screen_writer.forward(400)
  screen_writer.left(90)
  screen_writer.forward(600)
  screen_writer.pu()
  screen_writer.goto(-300,200)
  screen_writer.write("Computer Player",font=font_setup)
  screen_writer.pu()
  screen_writer.goto(175,200)
  screen_writer.write("Player 1",font=font_setup)


def mini_game_3():
  arena()
  user_input= input("What is your choice rock(rock), scissors(scissors), or paper(paper)")
  computer=["rock", "scissors","paper"]
  computer_output= rand.choice(computer)
  if user_input== computer_output:
    print("this was a tie")
    print("it was " + str(computer_output) + " from computer vs " + str(user_input) + " from your part" )
    if computer_output=="scissors":
      draw_scissors()
    elif computer_output=="rock":
      draw_rock()
    else: 
      draw_paper()
    if user_input== "scissors":
      mine_scissors()
    elif user_input== "rock":
      mine_rock()
    elif user_input== "paper":
      mine_paper()
  if user_input== "rock" and computer_output=="scissors":
    print("you won against the computer")
    print("it was " + str(computer_output) + " from computer vs " + str(user_input) + " from your part" )
    mine_rock()
    draw_scissors()
  if user_input== "scissors" and computer_output== "rock":
    score_drawn()
    print("sorry you lose against the computer")
    print("it was " + str(computer_output) + " from computer vs " + str(user_input) + " from your part" )
    mine_scissors()
    draw_rock()
  if user_input== "paper" and computer_output== "scissors":
    score_drawn()
    print("sorry you lost against the computer")
    print("it was " +str(computer_output) + " from computer vs " + str(user_input) + " from your part" )
    draw_scissors()
    mine_paper()
  if user_input== "scissors" and computer_output=="paper":
    print("you won against the computer")
    print("it was " +str(computer_output) +" from computer vs " + str(user_input) +" from your part" )
    mine_scissors()
    draw_paper()

score_keeper.hideturtle()
maze.hideturtle()
maze_runner.hideturtle()
eight_ball.hideturtle()
screen_writer.hideturtle()
def interactive_story():
  answer= input("Do you want to play yes/no")
  if answer.lower().strip() == "yes":
    print("You're trapped inside a house,trying to escape.") 
    print("You need to pick the right doors in order to escape, or else you get punishment tasks until you escape")
    answer_1= input("Do you want to escape through door A or Door B?")
    if answer_1.lower().strip() == "doora":
      print("you picked the right door no punishment task, yay")
      answer_two= input("Say yes to continue to face 2")
      if answer_two.lower().strip() == "yes":
        eight_ball.clear()
        screen_writer.clear()
        print("Good, you completed your first task now you have to pick between 2 other doors")
        answer_3=input("pick either door c or door d")
        if answer_3.lower().strip()=="doorc":
          print("Sorry wrong door, now you have to do a punishment")
          print("you have to rearanged the letters to form a 4 letter word")
          mini_game_2()
          answer_4 = input("wanna continue, next mini game isn't optional/say yes")
          if answer_4=="yes":
            print("play this final game to see your final score")
            mini_game_3()
          else:
            print("game over")
            screen_writer.clear()
        elif answer_3.lower().strip()=="doord":
          print("Good Guess, you picked the right door")
          print("Now you are going to the final face before you can escape from this house")
          answer_4= input("wanna continue, next mini game isn't optional/ say yes")
          if answer_4=="yes":
            print("play this final game to see your final score")
            mini_game_3()
          else:
            print("game over")
            screen_writer.clear()
        else:
          print("you picked neither door")
          print("game over")
      else:
        print("that's too bad")
    else:
      print("you picked the wrong door, now you have to do a punishment task")
      print("Do the task in the turtle screen")
      print("In order to continue the 8 ball has to say yes")
      mini_game_1()
      answer_two= input("Say yes to continue to face 2")
      if answer_two.lower().strip() == "yes":
        eight_ball.clear()
        screen_writer.clear()
        print("Good, you completed your first task now you have to pick between 2 other doors")
        answer_3=input("pick either door c or door d")
        if answer_3.lower().strip()=="doorc":
          print("Sorry wrong door, now you have to do a punishment")
          print("you have to rearanged the letters to form a 4 letter word")
          mini_game_2()
          answer_4= input("wanna continue, next mini game isn't optional/ say yes")
          if answer_4=="yes":
            print("play this final game to see your final score")
            mini_game_3()
          else:
            print("game over")
            screen_writer.clear()
        elif answer_3.lower().strip()=="doord":
          print("Good Guess, you picked the right door")
          print("Now you are going to the final face before you can escape from this house")
          answer_4= input("wanna continue, next mini game isn't optional/ say yes")
          if answer_4=="yes":
            print("play this final game to see your final score")
            mini_game_3()
          else:
            print("game over")
            screen_writer.clear()
        else:
          print("you picked neither door")
          print("game over")
      else:
        print("that's too bad")
  else:
    print("that's too bad, hopefully next time you play the game")


interactive_story()
print("you final score was: "+str(score))
wn.mainloop()
