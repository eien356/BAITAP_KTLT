# Nguyễn Duy Hiếu; Msv: 245752021610054

# nhập chuỗi đầu vào và in ra màn hình theo thứ tự cổ điển
chuoi = input("nhập chuỗi số các từ tiếng anh:")
ds = chuoi.split()
ds.sort()
print("Các từ theo thứ tự từ điển:")
for w in ds:
    print(w)