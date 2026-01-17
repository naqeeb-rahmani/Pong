from turtle import Turtle, Screen
import time

p1_score = 0
p2_or_ai_score = 0


target_score = 5

game_running = False
menu = True

p_vs_p = True
ai_vs_p = False

#---Screen---#
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

#---menu_turtles---#
menu1 = Turtle()
menu1.color("Blue")
menu1.penup()
menu1.hideturtle()
menu1.goto(0,100)

menu2 = Turtle()
menu2.color("White")
menu2.penup()
menu2.hideturtle()
menu2.goto(0,-100)

#---menu-functions (game code as well)---#

def navigate_down_mm(): #mm = mode menu
    global p_vs_p, ai_vs_p
    if p_vs_p == True:
        p_vs_p = False; ai_vs_p = True
        menu1.clear()
        menu2.clear()
        menu1.color("White")
        menu2.color("Blue")
        menu1.write("Player vs Player", align = "center", font = ("Courier", 40, "normal"))
        menu2.write("AI vs Player", align = "center", font = ("Courier", 40, "normal"))

def navigate_up_mm(): #mm = mode menu
    global p_vs_p, ai_vs_p
    if ai_vs_p == True:
        p_vs_p = True; ai_vs_p = False
        menu1.clear()
        menu2.clear()
        menu1.color("Blue")
        menu2.color("White")
        menu1.write("Player vs Player", align = "center", font = ("Courier", 40, "normal"))
        menu2.write("AI vs Player", align = "center", font = ("Courier", 40, "normal"))

def confirm_mode():
    global menu, game_running
    menu1.clear(); menu2.clear()
    menu1.color("White"); menu2.color("Blue")
    #---target-score-menu---#
    setpos_target_menu()
    menu1.write("Target score", align = "center", font = ("Courier", 40, "normal"))
    menu2.write(target_score, align = "center", font = ("Courier", 40, "normal"))
    screen.listen()
    screen.onkeypress(increase_target_score, "Up")
    screen.onkeypress(decrease_target_score, "Down")
    screen.onkeypress(confirm_target_score, "Return")

def setpos_target_menu():
    menu1.goto(0,150)
    menu2.goto(0,0)

def increase_target_score():
    global target_score; target_score += 1
    menu2.clear()
    menu2.write(target_score, align = "center", font = ("Courier", 40, "normal"))

def decrease_target_score():
    global target_score
    if target_score > 1: target_score -= 1
    menu2.clear()
    menu2.write(target_score, align = "center", font = ("Courier", 40, "normal"))

def confirm_target_score():
    menu1.clear()
    menu1.goto(0,100)
    menu2.clear()
    game_running = True
    #---game-code---#
    if game_running:
        score.write( f"{p2_or_ai_score}     {p1_score}", align = "center", font = ("Courier", 80, "normal"))

        screen.listen()

        screen.onkeypress(p1_up, "Up")
        screen.onkeypress(p1_down, "Down")

        if p_vs_p:
            screen.onkeypress(p2_up, "w")
            screen.onkeypress(p2_down, "s")


            while game_running:
                if (target_score != p1_score) and (target_score != p2_or_ai_score):
                    move_ball_and_check_for_collisions()
                    check_score()
                if target_score == p1_score:
                    menu1.write("Player 1 won", align = "center", font = ("Courier", 80, "normal"))
                elif target_score == p2_or_ai_score:
                    menu1.write("Player 2 won", align = "center", font = ("Courier", 80, "normal"))

                screen.update()
                time.sleep(0.026)

        elif ai_vs_p:
             while game_running:
                if (target_score != p1_score) and (target_score != p2_or_ai_score):
                    move_ball_and_check_for_collisions()
                    # simple-ai
                    if ball.xcor() < 0:
                        if player2.ycor() < ball.ycor():
                            player2.goto(-377,player2.ycor() + 8)
                        elif player2.ycor() > ball.ycor():
                            player2.goto(-377,player2.ycor() - 8)
                    #   /simple-ai
                    check_score()
                if target_score == p1_score:
                    menu1.write("Player 1 won", align = "center", font = ("Courier", 80, "normal"))
                elif target_score == p2_or_ai_score:
                    menu1.write("AI won", align = "center", font = ("Courier", 80, "normal"))
                    
                screen.update()
                time.sleep(0.026)
            
            
            

#---player1---#
player1 = Turtle()
player1.shape("square")
player1.shapesize(4,1)
player1.color("white")
player1.penup()
player1.goto(377,0)
#---player2---#
player2 = Turtle("square")
player2.shape("square")
player2.shapesize(4,1)
player2.color("white")
player2.penup()
player2.goto(-377,0)

#---the-ball---#
ball = Turtle("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball_direction_x = 6
ball_direction_y = 6

#---paddel-move-functions---#
def p1_up():
    new_pos = player1.ycor() + 20
    if new_pos <= 250:
        player1.goto(377, new_pos)
def p1_down():
    new_pos = player1.ycor() - 20
    if new_pos >= -250:
        player1.goto(377, new_pos)

def p2_up():
    new_pos = player2.ycor() + 20
    if new_pos <= 250:
        player2.goto(-377, new_pos)
def p2_down():
    new_pos = player2.ycor() - 20
    if new_pos >= -250:
        player2.goto(-377, new_pos)

#---ball-functions---#

def move_ball_and_check_for_collisions():
    global ball_direction_y, ball_direction_x
    ball.goto(ball.xcor() + ball_direction_x, ball.ycor() + ball_direction_y)

    if ball.ycor() > 270:
        ball_direction_y *= -1
    elif ball.ycor() < -270:
        ball_direction_y *= -1
    
    if ball.distance(player1) < 40 and ball_direction_x > 0:
        ball_direction_x *= -1
    elif ball.distance(player2) < 40 and ball_direction_x < 0:
        ball_direction_x *= -1

def ball_speed_increase():
    global ball_direction_x, ball_direction_y
    if (p2_or_ai_score + p1_score) == 3:
        ball_direction_x += 2; ball_direction_y += 2
    elif (p2_or_ai_score + p1_score) == 7:
        ball_direction_x += 2; ball_direction_y += 2
    elif (p2_or_ai_score + p1_score) == 12:
        ball_direction_x += 2; ball_direction_y += 2

#---score---#
score = Turtle()
score.color("White")
score.penup()
score.hideturtle()
score.goto(0,200)

#---score-function---#

def check_score():
    global p1_score, p2_or_ai_score, ball_pause
    if ball.xcor() > 390 or ball.xcor() < -390:
        score.clear()
        if ball.xcor() > 390:
            p2_or_ai_score += 1
        elif ball.xcor() < -390:
            p1_score += 1
        score.write( f"{p2_or_ai_score}     {p1_score}", align = "center", font = ("Courier", 80, "normal"))
        ball.hideturtle()
        ball.goto(0,0)
        ball.showturtle()
        ball_speed_increase()



#---mode-menu---#

if menu == True and game_running == False:
    menu1.write("Player vs Player", align = "center", font = ("Courier", 40, "normal"))
    menu2.write("AI vs Player", align = "center", font = ("Courier", 40, "normal"))
    screen.listen()
    screen.onkeypress(navigate_down_mm, "Down")
    screen.onkeypress(navigate_up_mm, "Up")
    screen.onkeypress(confirm_mode,"Return")


#---target-menu---#


screen.exitonclick()