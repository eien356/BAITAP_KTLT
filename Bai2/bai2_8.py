# Nguyễn Duy Hiếu; Msv: 245752021610054
# khai báo 2 số F nhỏ nhất
a,b=1,2
total=0
print(a,end=" ")
# sử dụng vòng lặp while để tìm tổng
while (a<=4000000-1):
    if a%2==0:
        total +=a
    a,b=b,a+b
    print(a,end=" ")
print("\n sum of prime numbers term in fibonacci series:",total)
