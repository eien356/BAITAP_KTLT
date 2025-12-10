# Nguyễn Duy Hiếu; Msv: 245752021610054
#Tạo 1 file ở ổ D và gán lần lượt số ký tự, số từ, số dòng ban đầu bằng 0
k=open('D:/a.txt','r')
char,wc,lc=0,0,0
#Dùng vòng lặp để đọc và duyệt các ký tự trong dòng
for line in k:
    for k in range (0,len(line)):
        char +=1
        if (line[k]==' '):
            wc+=1
        if (line[k]=='\n'):
            wc,lc=wc+1,lc+1
print("Chars: %d\nWords: %d\nLines: %d" %( char, wc, lc))
