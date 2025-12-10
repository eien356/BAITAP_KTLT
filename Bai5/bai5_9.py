# Nguyễn Duy Hiếu; Msv: 245752021610054
#Khai báo hàm
def binary_search(arr, value):
    left = 0
    right = len(arr) - 1
#Dùng vòng lặp để tìm kiếm và so sánh phần tử đứng giữa và phần tử cần tìm
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == value:
            return True
        elif arr[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return False
#Nhập danh sách, giá trị cần tìm và gọi hàm tìm kiếm
lst = list(map(int, input("Nhập danh sách số nguyên cách nhau bởi dấu cách: ").split()))
lst.sort()
val = int(input("Nhập giá trị cần tìm: "))
if binary_search(lst, val):
    print("Giá trị tồn tại trong danh sách.")
else:
    print("Giá trị không tồn tại.")
