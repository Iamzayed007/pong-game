import turtle



wn=turtle.Screen()
wn.title('pong by Zayed')
wn.bgcolor('gray')
wn.setup(width=800,height=600)



wn.update()




wn.tracer(0)


#function
def paddle_a_Right():
    x= paddle_a.xcor()
    x+=20
    paddle_a.setx(x)
def paddle_a_Left():
    x= paddle_a.xcor()
    x-=20
    paddle_a.setx(x)



#score
score_a = 0


#keyword binding

wn.listen()
wn.onkeypress(paddle_a_Right,'Right')
wn.onkeypress(paddle_a_Left,'Left')


#paddle A
paddle_a= turtle.Turtle()
paddle_a.speed(6)
paddle_a.shape("square")
paddle_a.color("green")
paddle_a.shapesize(stretch_wid=8 ,stretch_len=1)
paddle_a.penup()
paddle_a.setpos(0,-280)
paddle_a.seth(90)


#ball
ball= turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("yellow")
ball.penup()
ball.goto(0,0)
ball.dx = 1
ball.dy = -1




#pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
#paddle_b.shapesize(stretch_wid=1 ,stretch_len=5)
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player : 0 ", align="center", font=("Courier", 20, "normal"))

while True:
    wn.update()
    #move ball

    ball.setx(ball.xcor()+ ball.dx)
    ball.sety(ball.ycor()+ ball.dy)





#border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy*=-1
        
    if ball.ycor() < -290:
        ball.goto(0,0)
      
        ball.dy*=-1
        score_a += 1
        pen.clear()
        pen.write("Player : {}".format(score_a), align="center", font=("Courier", 20, "normal"))
        
        

    if ball.xcor() > 390:
        ball.setx(390)
  
        ball.dx*=-1
      
        pen.clear()
      
    if ball.xcor() < -390:
        ball.setx(-390)
       # ball.goto(0,0)
        ball.dx*=-1
      #  score_b += 1
        pen.clear()
       
   
   
    #paddle abd ball collisions

    

    if (ball.ycor()< -240 and ball.ycor()> -250) and (ball.xcor() < paddle_a.xcor()+70 and ball.xcor() > paddle_a.xcor() - 70 ):

        ball.sety(-240)
        ball.dy*=-1
        pen.penup()
