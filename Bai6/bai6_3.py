# Nguyễn Duy Hiếu; Msv: 245752021610054
#Tạo lớp người và hai lớp con kế thừa từ lớp người
class Nguoi:
    def getGender(self):
        return "unknown"
class Nam(Nguoi):
    def getGender(self):
        return "Nam"
class Nu(Nguoi):
    def getGender(self):
        return "nữ"
#Nhập đối tượng cho Nam và Nu
a = Nam()
b = Nu()
print(a.getGender())
print(b.getGender())
