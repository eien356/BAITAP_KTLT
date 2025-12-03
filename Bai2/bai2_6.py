# Nguyễn Duy Hiếu; Msv: 245752021610054
# Khai báo danh sách rông để chứa
j=[]
# Sử dụng vòng lặp for
for i in range(2000,3201):
    if (i%7==0) and (i%5!=0):
        j.append(str(i))
print(','.join(j))
