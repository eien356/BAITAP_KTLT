with open('nguon.txt', 'r', encoding='utf-8') as file_nguon:
    noi_dung = file_nguon.read()
with open('dich.txt', 'w', encoding='utf-8') as file_dich:
    file_dich.write(noi_dung)
