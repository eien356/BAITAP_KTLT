# Nguyễn Duy Hiếu; Msv: 245752021610054
#Tạo một danh sách rỗng và nhập các phần tử vào trong danh sách
lst = []
n = int(input("Nhập số lượng phần tử: "))
#Dùng vòng lặp for để nhập các phần tử và cho chạy từ 0 đến n-1
for i in range(n):
    value = float(input(f"Nhập phần tử thứ {i+1}: "))
    lst.append(value)
# tìm gia trị lớn nhất
max_value = max(lst)
min_value = min(lst)
# tìm vị trí (index) của chúng
max_index = lst.index(max_value)
min_index = lst.index(min_value)
#in kết quả
print("\n Danh sách: ", lst)
print(f"Phần tử lớn nhất: {max_value} ở vj trí {max_index}")
print(f"Phần tử nhỏ nhất: {min_value} ở vị trí {min_index}")
