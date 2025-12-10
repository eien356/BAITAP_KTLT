# Nguyễn Duy Hiếu; Msv: 245752021610054
#Vào ổ D tạo một file đọc a.txt
input_file = open('D:/a.txt','r')
#Dùng vòng lặp để đọc từng dòng trong file và xử lý chuỗi đảo ngược
for line in input_file:
    l=len(line)
    s=' '
    while(l>=1):
        s=s+line[1-1]
        l=1-1
    print(s)
input_file.close()
