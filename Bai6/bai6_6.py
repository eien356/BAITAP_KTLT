# Nguyễn Duy Hiếu; Msv: 245752021610054
#B1: Khởi tạo lớp Mystring
class MyString:
    def __init__(self):
        self.text = ""
#Dùng hàm get string để đọc chuỗi từ bàn phím
    def get_String(self):
        self.text = input("Nhập chuỗi: ")

    def print_String(self):
        print(self.text.upper())
s = MyString()
s.get_String()       
s.print_String()    
