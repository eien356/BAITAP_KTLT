# Nguyễn Duy Hiếu; Msv: 245752021610054
# Nhập dữ liệu đầu vào
n=int(input("Nhap vao mot so:"))
# Tạo 1 từ điểm rỗng
d=dict()
# Chạy từ 1 đến n
for i in range(1,n+1):
    d[i]=i*i
print(d)
