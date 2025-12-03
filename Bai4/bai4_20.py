# Nguyễn Duy Hiếu; Msv: 245752021610054

# nhập n, in n dòng đầu tiên của tam giác pascal
n = int(input("nhập n: "))
for i in range(n):
    num = 1
    for j in range(i + 1):
        print(num, end=" ")
        num = num * (i - j) // (j + 1)
    print()