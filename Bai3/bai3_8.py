# Nguyễn Duy Hiếu; Msv: 245752021610054
#dùng thư viện import math để làm tròn số và khai báo vị trí ban đầu của robot
import math

x = 0
y = 0
#nhận nhiều lệnh di chuyển, khai báo hướng di chuyển của robot 
while True:
    s = input("Nhập hướng và số bước (ENTER để dừng): ")
    if not s:
        break
    direction, steps = s.split()
    steps = int(steps)
    if direction.upper() == "UP":
        y += steps
    elif direction.upper() == "DOWN":
        y -= steps
    elif direction.upper() == "LEFT":
        x -= steps
    elif direction.upper() == "RIGHT":
        x += steps
#tính khoảng cách của robot từ vị trí hiện tại về gốc (0,0) theo công thức Euclid.
distance = math.sqrt(x**2 + y**2)
print(round(distance))
