# Nguyễn Duy Hiếu; Msv: 245752021610054
#Khai báo hàm và mở file để ghi nội dung
def file_read (fname):
    from itertools import islice
    with open(fname, "w") as myfile:
#Ghi dữ liệu vào file và mở lại file để đọc
        myfile.write("Python Exercises\n")
        myfile.write("Java Exercises")
    txt = open(fname)
    print(txt.read())
file_read('abc.txt')
