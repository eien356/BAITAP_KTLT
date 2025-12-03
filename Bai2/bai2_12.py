# Nguyễn Duy Hiếu; Msv: 245752021610054
# Tọa hàm kiểm tra mật khẩu và cách điều kiện
import re

def kiem_tra_mat_khau(password):
    
    if len(password) < 6 or len(password) > 12:
        return False
    
    if not re.search("[a-z]",password):
        return False
    
    if not re.search("[A-Z]",password):
        return False
    
    if not re.search("[0-9]",password):
        return False
    
    if not re.search("[$-@]",password):
        return False
    
    return True

# Nhập dữ liệu và tạo không gian hợp lệ
chuoi = input("nhap mat khau (cach nhau bang dau phay):").split(",")
hop_le=[]
# duyệt mật khẩu
for matkhau in chuoi:
    if kiem_tra_mat_khau(matkhau.strip()):
        hop_le.append(matkhau.strip())
        
print("mat khau hop le:",",".join(hop_le))
    
