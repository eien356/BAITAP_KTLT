# Nguyễn Duy Hiếu; Msv: 245752021610054
#Khai báo thư viện để vẽ đồ họa
import turtle, random
colors = ["red", "green", "orange", "purple", "pink", "yellow"]
painter = turtle.Turtle()
painter.pensize(3)
#Dùng vòng lặp vẽ hình tròn
for i in range(10):
    color = random.choice(colors)
    painter.pencolor(color)
    painter.circle(100)
    painter.right(30)
    painter.left(60)
    painter.setposition(0, 0)
