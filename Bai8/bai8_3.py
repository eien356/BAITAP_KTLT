# Nguyễn Duy Hiếu; Msv: 245752021610054
#Import thư viện turtle
import turtle
#Tạo danh sách màu
colors = ["red", "blue", "green"]
#Tạo một đối tượng Turtle
painter = turtle.Turtle()
#Đặt độ dày của bút
painter.pensize(3)
#Bắt đầu vòng lặp 12 lần
for i in range(12):
#Chọn màu dựa vào số lần lặp
    color = colors[i % len(colors)]
    painter.pencolor(color)
#Vẽ một hình tròn bán kính 100
    painter.circle(100)
#Xoay hướng con rùa
    painter.right(30)
    painter.left(60)
#Đưa con rùa về tâm màn hình
    painter.setposition(0, 0)
