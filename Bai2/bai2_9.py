# Nguyễn Duy Hiếu; Msv: 245752021610054
# Nhập dữ liệu đầu vào và tạo thêm từ điển rỗng
str=input("Enter a String")
dict={}
# duyệt từng ký tự và đếm số lần uất hiện
for i in str:
    dict[i]=str.count(i)
print(dict)
