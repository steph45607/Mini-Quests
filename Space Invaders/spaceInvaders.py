import turtle
import random

#screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
wn.bgpic("Space Invaders/space_invaders_background.gif")

turtle.register_shape("Space Invaders/invader.gif")
turtle.register_shape("Space Invaders/gdsccat.gif")

#border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
#make the square border
for side in range(4):
    border_pen.forward(600)
    border_pen.left(90)
border_pen.hideturtle() #hide the arrow thingy

#score
score = 0
scorepen = turtle.Turtle()
scorepen.speed(0)
scorepen.color("white")
scorepen.penup()
scorepen.setposition(-290,280)
scorestring = f"Score: {score}"
scorepen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
scorepen.hideturtle()

#player
player = turtle.Turtle()
player.color("blue")
player.shape("Space Invaders/gdsccat.gif")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)


#gun
gun = turtle.Turtle()
gun.color("yellow")
gun.shape("triangle")
gun.penup()
gun.speed(0)
gun.setheading(90)
gun.shapesize(0.5,0.5)
gun.hideturtle()

gunspeed = 20
#gun state
gunstate = "ready"
badnum = 5
#bad list
badguys = []

#add bad guys
for i in range(badnum):
    #create more bad guys
    badguys.append(turtle.Turtle())

for bad in badguys:
    #bad guy
    bad.color("red")
    bad.shape("Space Invaders/invader.gif")
    bad.penup()
    bad.speed(0)
    x = random.randint(-200,200)
    y = random.randint(100,250)
    bad.setposition(x,y)

badspeed = 2


#move player use arrow keys
playerspeed = 15 #how far the player move
def left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)

def right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

#gun function
def fire():
    global gunstate #declare gunstate as a global var
    if gunstate == "ready":
        gunstate = "fire"
        #move gun above the player
        x = player.xcor()
        y = player.ycor()
        gun.setposition(x,y + 10)
        gun.showturtle()

#collision
def collision(t1: turtle.Turtle,t2: turtle.Turtle):
    # distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    distance = t1.distance(t2)
    if distance < 15:
        return True
    else:
        return False


#keyboard bindings
turtle.listen()
turtle.onkey(left,"Left") #assign "Left" key to run function left()
turtle.onkey(right,"Right") #assign "Right" key to run function right()
turtle.onkeyrelease(fire, "space") #assign "space" key to run function fire()

#game loop
while True:
    for bad in badguys:
        # move bad guy
        x = bad.xcor()
        x += badspeed
        bad.setx(x)

        # move bad guy back
        if bad.xcor() > 280:
            # move all bad guys down
            for b in badguys:
                y = b.ycor()
                y -= 40
                b.sety(y)
            # change bad guys direction
            badspeed *= -1 
        
        if bad.xcor() < -280:
            # move all bad guys down
            for b in badguys:
                y = b.ycor()
                y -= 40
                b.sety(y)
            # change bad guys direction
            badspeed *= -1
            # check collision between gun and bad

        if collision(gun, bad):
            # reset gun
            gun.hideturtle()
            gunstate = "ready"
            gun.setposition(0,-400)
            # reset bad
            x = random.randint(-200,200)
            y = random.randint(100,250)
            bad.setposition(x,y)
            # update score
            score += 10
            scorestring = f"Score: {score}"
            scorepen.clear()
            scorepen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))

        
        if collision(player,bad):
            player.hideturtle()
            bad.hideturtle()
            break

    # move gun
    if gunstate == "fire":
        y = gun.ycor()
        y += gunspeed
        gun.sety(y)

    # check gun position top
    if gun.ycor() > 275:
        gun.hideturtle()
        gunstate = "ready"
    
print("Game Over")




delay = input("Press enter to finish")