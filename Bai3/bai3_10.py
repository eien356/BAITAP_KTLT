# Nguyễn Duy Hiếu, mssv 245752021610054 
#nhập thư viện 
import math

def Tinh(R):
#nếu R hợp lệ thì dùng if else để tính chu vi, diện tích hình tròn và in ra kết quả.
    if R <= 0:
        print("Bán kính hông hợp lệ! Vui lòng nhập số dương.")
    else:
        chu_vi = 2 * math.pi * R
        dien_tich = math.pi * R * R
        print("chu vi hình tròn là:", round(chu_vi, 2))
        print("Diện tich hình tròn là:", round(dien_tich, 2))

try:
    R = float(input("Nhập bán kính R: "))
    Tinh(R)
except ValueError:
    print("Giá trị nhập vào không hợp lệ! Vui lòng nhập một só.")
