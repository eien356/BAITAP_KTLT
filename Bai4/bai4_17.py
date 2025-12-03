# Nguyễn Duy Hiếu; Msv: 245752021610054

# nhập số n, in ra màn hình các số nguyên dương nhỏ hơn n có tổng các ước số lớn hơn chính nó
n = int(input("nhập n:"))
for i in range(1, n):
    tong_uoc = sum(j for j in range(1, i) if i % j == 0)
    if tong_uoc >i:
        print(i)