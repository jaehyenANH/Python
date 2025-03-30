import turtle

turtle.shape('turtle')


turtle.pensize(3)
turtle.speed(3)

# 자음/모음 구성 요소 함수
def draw_ㅇ():
    turtle.pendown()
    turtle.circle(10)
    turtle.penup()
    turtle.right(90)
    turtle.forward(20)

def draw_ㅏ():
    turtle.pendown()
    turtle.left(90)
    turtle.forward(20)
    turtle.right(180)
    turtle.forward(40)
    turtle.left(180)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(20)
    turtle.penup()
    turtle.left(180)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(20)

def draw_ㄴ():
    turtle.left(90)
    turtle.pendown()
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(30)
    turtle.penup()
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(50)

def draw_ㅈ():
    turtle.right(90)
    turtle.pendown()
    turtle.forward(30)
    turtle.right(130)
    turtle.forward(40)
    turtle.left(180)
    turtle.forward(20)
    turtle.right(80)
    turtle.forward(20)
    turtle.penup()
    turtle.left(30)
    turtle.forward(10)


def draw_ㅐ():
    turtle.left(90)
    turtle.pendown()
    turtle.forward(40)
    turtle.right(180)
    turtle.forward(60)
    turtle.left(180)
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(30)
    turtle.left(180)
    turtle.forward(60)
    turtle.penup()
    turtle.right(90)
    turtle.forward(30)

def draw_ㅎ():
    turtle.pendown()
    turtle.forward(30)
    turtle.right(90)
    turtle.penup()
    turtle.forward(10)
    turtle.right(90)
    turtle.pendown()
    turtle.forward(40)
    turtle.right(180)
    turtle.forward(50)
    turtle.right(180)
    turtle.forward(25)
    turtle.left(90)
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()
    turtle.right(90)
    turtle.circle(10)
    turtle.right(180)
    turtle.penup()

def draw_ㅕ():
     turtle.forward(30)
     turtle.pendown()
     turtle.forward(10)
     turtle.left(90)
     turtle.forward(10)
     turtle.right(180)
     turtle.forward(20)
     turtle.right(90)
     turtle.forward(10)
     turtle.left(180)
     turtle.forward(10)
     turtle.right(90)
     turtle.forward(10)
     turtle.right(90)
     turtle.penup()
     turtle.forward(20)
    
def draw_안():
    draw_ㅇ()
    draw_ㅏ()
    draw_ㄴ()
    

def draw_재():
    draw_ㅈ()
    draw_ㅐ()
   

def draw_현():
    draw_ㅎ()
    draw_ㅕ()
    draw_ㄴ()
    
   
# 전체 이름 그리기
def draw_name():
    draw_안()
    draw_재()
    draw_현()
    
# 시작 위치 설정 및 실행
turtle.penup()
turtle.setheading(0)
turtle.backward(100)     
turtle.setheading(90)
draw_name()

turtle.exitonclick()


