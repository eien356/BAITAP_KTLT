# Nguyễn Duy Hiếu; Msv: 245752021610054
# Khai báo lớp class với tên hinhchunhat
class Hinhchunhat:
    def __init__(self, dai, rong):
        self.dai = dai
        self.rong = rong
#Tính diện tích hình chữ nhật
    def dientich(self):
        return self.dai*self.rong
hcn = Hinhchunhat(5,3)
print("Diện tích hình chữ nhật là:", hcn.dientich())
