import random
import turtle
import winsound
import time

turtle.fd(0)                #to show the window
turtle.speed(0)             #to set animation speed
turtle.bgcolor("black")     #change the background color
turtle.title("Space War")
turtle.bgpic("background3.gif")
turtle.ht()                 #hide the default turtle
turtle.setundobuffer(1)     #save memory
turtle.tracer(0)            #speed up drawing

#Create class
class Sprite(turtle.Turtle):
    def __init__(self, spriteshape, color, startx, starty):
        turtle.Turtle.__init__(self, shape = spriteshape)
        self.speed(0)
        self.penup()
        self.color(color)
        self.fd(0)
        self.goto(startx, starty)
        self.speed = 1

    def move(self):
        self.fd(self.speed)
        # Boundary detection
        if self.xcor() > 290:
            self.setx(290)
            self.rt(60)
        if self.xcor() < -290:
            self.setx(-290)
            self.rt(60)
        if self.ycor() > 290:
            self.sety(290)
            self.rt(60)
        if self.ycor() < -290:
            self.sety(-290)
            self.rt(60)

    def collision(self, other):
        if (self.xcor() >= (other.xcor() - 20)) and \
            (self.xcor() <= (other.xcor() + 20)) and \
            (self.ycor() >= (other.ycor() - 20)) and \
            (self.ycor() <= (other.ycor() + 20)):
            return True
        else:
            return False


class Player(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.shapesize(stretch_wid=0.6, stretch_len=2, outline=3)
        self.speed = 4
        self.lives = 3

    def turn_left(self):
        self.lt(45)
    def turn_right(self):
        self.rt(45)
    def acceleration(self):
        self.speed +=1
    def deceleration(self):
        self.speed -= 1

class Enemy(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.speed = 6
        self.setheading(random.randint(0, 360))

class Ally(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.speed = 8
        self.setheading(random.randint(0, 360))

    def move(self):
        self.fd(self.speed)
        # Boundary detection
        if self.xcor() > 290:
            self.setx(290)
            self.lt(60)
        if self.xcor() < -290:
            self.setx(-290)
            self.lt(60)
        if self.ycor() > 290:
            self.sety(290)
            self.lt(60)
        if self.ycor() < -290:
            self.sety(-290)
            self.lt(60)

class Missile1(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.shapesize(stretch_wid=0.1, stretch_len=0.4, outline=None)
        self.speed = 20
        self.status = "ready"
        self.goto(-1000, 1000)

    def fire(self):
        if self.status == "ready":
            winsound.PlaySound("missile1.wav", winsound.SND_ASYNC)
            self.goto(player.xcor(), player.ycor())     #set missile to player's position
            self.setheading(player.heading())           #set missile direction
            self.status = "firing"

    def move(self):

        if self.status == "ready":
            self.goto(-1000, 1000)

        if self.status == "firing":
            self.fd(self.speed)

        #Boarder check
        if self.xcor() < -290 or self.xcor() > 290 or \
            self.ycor() < -290 or self.ycor() > 290:
            self.goto(-1000, 1000)
            self.status = "ready"

class Missile12(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.shapesize(stretch_wid=0.3, stretch_len=0.4, outline=None)
        self.speed = 20
        self.status = "ready"
        self.goto(-1000, 1000)

    def fire(self):
        if self.status == "ready":
            winsound.PlaySound("missile2.wav", winsound.SND_ASYNC)
            self.goto(ally.xcor(), ally.ycor())     #set missile to ally's position
            self.setheading(ally.heading())           #set missile direction
            self.status = "firing"

    def move(self):

        if self.status == "ready":
            self.goto(-1000, 1000)

        if self.status == "firing":
            self.fd(self.speed)

        #Boarder check
        if self.xcor() < -290 or self.xcor() > 290 or \
            self.ycor() < -290 or self.ycor() > 290:
            self.goto(-1000, 1000)
            self.status = "ready"

class Particle(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.shapesize(stretch_wid=0.1, stretch_len=0.1, outline=None)
        self.goto(-1000, -1000)
        self.frame = 0

    def explode(self,startx, starty):
        self.goto(startx, starty)
        self.setheading(random.randint(0, 360))

    def move(self):
        self.fd(10)

class Game():

    def Gamesound(self):
        winsound.PlaySound("bgmusic1.wav", winsound.SND_ASYNC)

    def __init__(self):
        self.level = 1
        self.score = 0
        self.state = "playing"
        self.pen = turtle.Turtle()
        self.lives = 3

    def draw_board(self):
        self.pen.speed(0)
        self.pen.color("white")
        self.pen.pensize(3)
        self.pen.penup()
        self.pen.goto(-300, 300)
        self.pen.pendown()
        for side in range(4):
            self.pen.fd(600)
            self.pen.rt(90)
        self.pen.penup()
        self.pen.ht()
        self.pen.pendown()

    def show_status(self):
        self.pen.undo()
        msg = "Score: %s"%(self.score)
        self.pen.penup()
        self.pen.goto(-300, 310)
        self.pen.write(msg, font=("Arial", 16, "normal"))

#Create game object
game = Game()

#Draw boarder
game.draw_board()

#Show the game status
game.show_status()

# Game sound



# Create my Sprites
player = Player("triangle", "white", 0, 0)
#enemy = Enemy("circle", "red", random.randint(-290, 290), random.randint(-290, 290))
missile1 = Missile1("triangle", "yellow", 0, 0)
missile2 = Missile12("triangle", "orange", 0, 0)
#ally = Ally("square", "blue", random.randint(-290, 290), random.randint(-290, 290))

enemies = []
for i in range(6):
    enemies.append(Enemy("circle", "red", random.randint(-290, 290), random.randint(-290, 290)))

allies = []
for i in range(6):
    allies.append(Ally("square", "sky blue", random.randint(-290, 290), random.randint(-290, 290)))

particles = []
for i in range(20):
    particles.append(Particle("circle", "orange", 0, 0))

# Keyboard binding
turtle.onkey(player.turn_left, "Left")
turtle.onkey(player.turn_right, "Right")
turtle.onkey(player.acceleration, "Up")
turtle.onkey(player.deceleration, "Down")
turtle.onkey(missile1.fire, "space")
turtle.listen()

#Main game loop
while True:
    time.sleep(0.03)
    #game.Gamesound()
    turtle.update()
    player.move()
    #enemy.move()
    missile1.move()
    missile2.move()
    #ally.move()

    for enemy in enemies:
        enemy.move()

        # check for collision (player vs enemy)
        if player.collision(enemy):
            x = random.randint(-250, 250)
            y = random.randint(-250, 250)
            enemy.goto(x, y)
            game.score -= 500  # Decrease the score
            game.show_status()

        # check for collision (enemy vs missile1)
        if missile1.collision(enemy):
            winsound.PlaySound("explosion2.wav", winsound.SND_ASYNC)
            x = random.randint(-250, 250)
            y = random.randint(-250, 250)
            enemy.goto(x, y)
            missile1.status = "ready"
            game.score += 1000  # Increase the score
            game.show_status()
            # explosion
            for particle in particles:
                particle.goto(missile1.xcor(), missile1.ycor())
                particle.setheading(random.randint(0, 360))


        # check for collision (enemy vs missile2)
        if missile2.collision(enemy):
            winsound.PlaySound("explosion2.wav", winsound.SND_ASYNC)
            x = random.randint(-250, 250)
            y = random.randint(-250, 250)
            enemy.goto(x, y)
            missile2.status = "ready"
            game.score += 500  # Increase the score
            game.show_status()
            for particle in particles:
                particle.goto(missile2.xcor(), missile2.ycor())
                particle.setheading(random.randint(0, 360))

    for ally in allies:
        ally.move()
        # check for collision (player vs ally)
        if player.collision(ally):
            missile2.status = "ready"
            missile2.fire()
        # check for collision (ally vs missile1)
        if missile1.collision(ally):
            winsound.PlaySound("explosion2.wav", winsound.SND_ASYNC)
            x = random.randint(-250, 250)
            y = random.randint(-250, 250)
            ally.goto(x, y)
            game.score -= 500  # Decrease the score
            game.show_status()
            for particle in particles:
                particle.goto(missile1.xcor(), missile1.ycor())
                particle.setheading(random.randint(0, 360))

    for particle in particles:
        particle.move()

delay = raw_input("Press enter to finish. >")