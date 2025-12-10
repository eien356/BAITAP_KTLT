# Nguyễn Duy Hiếu; Msv: 245752021610054
#Định nghĩa hàm và khai báo biến
def Senquetial_Search(dlist, item):
    pos = 0
    found = False
#lặp các phần tử để kiểm tra
    while pos < len(dlist) and not found:
        if dlist[pos] == item:
            found = True
        else:
            pos += 1
    return found, pos + 1 if found else -1
#Nhập danh sách từ người dùng
if __name__ == "__main__":
    n = int(input("Nhập số phần tử của danh sách: "))
dlist = []
for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i+1}: "))
    dlist.append(x)
#Nhập phần tử cần tìm và gọi hàm tìm kiếm
item = int(input("Nhập phần tử cần tìm: "))
found, position = Senquetial_Search(dlist, item)
if found:
    print(f"Phần tử (item) được tìm thấy tại vị trí (position).")
else:
    print(f"Phần tử (item) không có trong danh sách. ")
