# Nguyễn Duy Hiếu; Msv: 245752021610054
#Khai báo hàm và mở file để đọc
def read_last_lines(fname, n):
    with open(fname, 'r', encoding='utf-8') as file:
        lines = file.readlines()
#Lấy n dòng cuối cùng và in ra
        last_lines = lines[-n:]
        for line in last_lines:
            print(line.strip())
read_last_lines('D:/a.txt', 1)          
    
