# Nguyễn Duy Hiếu; Msv: 245752021610054
#Khai báo hàm và mở file để đọc
def count_lines(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
#In số dòng có ở trong file
        print("Số dòng trong file là:", len(lines))

# Gọi hàm với đường dẫn file
count_lines('D:/a.txt')
