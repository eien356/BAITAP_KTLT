# Nguyễn Duy Hiếu; Msv: 245752021610054

# nhập dãy từ bàn phím, in ra từ dài nhất, in ra mọi từ cùng độ dài
ds = input("nhập dãy số:").split()
maxlen = max(len(w) for w in ds )
for w in ds:
    if len(w) == maxlen:
        print(w)