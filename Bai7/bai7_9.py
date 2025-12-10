# Nguyễn Duy Hiếu; Msv: 245752021610054
#Khai báo hàm, mở file nguồn để đọc và lưu vào biến data
def copy_file(source, destination):
    with open(source, 'r', encoding='utf-8') as file_nguon:
        noi_dung = file_nguon.read()
#Mở file đích bằng chế độ ghi (w) và ghi nội dung vào file đích
    with open(destination, 'w', encoding='utf-8') as file_dich:
        file_dich.write(noi_dung)
    print("Copy complete")
    
copy_file('D:/a.txt', 'D:/b.txt')
