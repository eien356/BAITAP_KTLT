# Nguyễn Duy Hiếu; Msv: 245752021610054

# nhập số nguyên N, tạo một list gồm các số fibonacci nhỏ hơn n và in ra màn hình
n = int(input("nhập n: "))
a, b=0, 1
fib = []
while a < n:
    fib.append(a)
    a, b =b, a + b
print("dãy fibonacci nhỏ hơn", n, "là:")
print(fib)