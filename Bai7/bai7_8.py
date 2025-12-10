# Nguyễn Duy Hiếu; Msv: 245752021610054
#Nhập danh sách phần tử cần ghi vào file
my_list = ['Python', 'Java', 'C++', 'JavaScript']
#Mở file và ghi phần tử hiện tại vào file
with open('D:/a.txt', 'w', encoding='utf-8') as f:
    for item in my_list:
        f.write(item + '\n')  # Ghi từng phần tử trên một dòng
        print(item)
