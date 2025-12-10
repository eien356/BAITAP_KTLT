# Nguyễn Duy Hiếu; Msv: 245752021610054
#Khai báo hàm và sử dụng thư viện để đọc file
def file_read_from_head(fname, nlines):
    from itertools import islice
#Mở file và đọc 2 dòng đầu tiên
    with open(fname) as f:
        for line in islice(f, nlines):
            print(line)
file_read_from_head('D:/a.txt', 2)
