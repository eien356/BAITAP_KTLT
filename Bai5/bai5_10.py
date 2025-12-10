# Nguyễn Duy Hiếu; Msv: 245752021610054
#Khai báo hàm
def bubbleSort(arr):
    n = len(arr)
#Dùng vòng lặp để kiểm tra và so sánh các phần tử với nhau
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1): 
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
# VD sd 
data = [14, 46, 43, 27, 57, 41, 45, 21, 70]
print("Mảng ban đầu:", data)
print("Mảng sau khi sắp xếp:", bubbleSort(data))
