# Nguyễn Duy Hiếu; Msv: 245752021610054

# Không in ra những ký tự "không nhìn thấy"
S = input('Nhập chuỗi:')
for ch in S:
    if ch not in [' ', '\t']:
        print(ch)