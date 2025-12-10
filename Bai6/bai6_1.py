# Nguyễn Duy Hiếu; Msv: 245752021610054
# Khai báo lớp class
class Circle:
    def __init__(self, radius):
        self.radius = radius  # Lưu bán kính vào thuộc tính của đối tượng
# Tính diện tích hình tròn
    def area(self):
        return 3.14 * self.radius ** 2  # Tính diện tích hình tròn
hinh_tron = Circle(5)  # Tạo đối tượng hình tròn với bán kính 5
print("Diện tích:", hinh_tron.area())  # In ra diện tích
