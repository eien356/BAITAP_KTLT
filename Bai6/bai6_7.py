# Nguyễn Duy Hiếu; Msv: 245752021610054
#Khai báo thư viện tên Circle
class Circle:
    def __init__(self, radius):
        self.radius = radius
#Sử dụng công thức tính diện tích và chu vi hình tròn
    def dientich(self):
        return self.radius * 3.14 ** 2
    def chuvi(self):
        return self.radius * 3.14 * 2
hinh_tron = Circle(5)
print("Diện tích: ", hinh_tron.dientich())
print("Chu vi:", hinh_tron.chuvi())
