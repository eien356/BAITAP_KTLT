# Nguyễn Duy Hiếu; Msv: 245752021610054
# tính lãi kép
def benefit(t, n, k):
    return n * (1 + t/100)**k
#chuyển dữ liệu nhập vào là số thực và kết quả trả về được gán vào biến tong_tien
t = float(input("Nhập lãi suất (%/tháng): "))
n = float(input("Nhập số vốn ban đầu: "))
k = float(input("Nhập số tháng gửi: "))

tong_tien = benefit(t, n, k)
print(f"Số tiền nhận được sau {k} tháng là: {tong_tien:.2f}")
