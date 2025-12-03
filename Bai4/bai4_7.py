# Nguyễn Duy Hiếu; Msv: 245752021610054

# nhập 1 chuỗi từ bàn phím, loại bỏ các chữ số và in ra nội dung mới
s = input("nhập chuỗi số: ")
moi = ' '
for ch in s:
    if not ch.isalpha():
        moi += ch
print("chuỗi mới:",moi)