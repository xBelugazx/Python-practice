# https://docs.python.org/3/library/turtle.html

import turtle

t = turtle.Turtle()  # 터틀 그래픽스의 객체

# 기본적으로 모니터 크기에 맞춰서 창이 나옴

# 수동 조절하고 싶은 경우
# turtle.setup(1280, 960)
# turtle.screensize(400, 300)
t.speed("slow")
t.shape("turtle")
t.turtlesize(2)
t.color("green")
t.pencolor("blue")
t.screen.bgcolor("aqua")

# square 1
for j in range(2):
    for i in range(4):
        t.forward(200)
        t.left(90)

t.left(180)
t.forward(200)

# square 2
for i in range(3):
    t.left(90)
    t.forward(200)

t.left(180)
t.forward(200)


for i in range(3):
    t.left(90)
    t.forward(200)

t.left(180)

turtle.done()
