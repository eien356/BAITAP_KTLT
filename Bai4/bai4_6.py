# Nguyễn Duy Hiếu; Msv: 245752021610054

# Nhập tên người từ bàn phím, tách phần họ và tên riêng và in ra
hoten = input("nhập họ và tên: ").split()
# họ và tên chỉ gồm 1 âm, phần đầu là họ, phần sau là tên
ho = hoten[0]
ten = hoten[-1]
print("họ: ",ho)
print("tên: ", ten)