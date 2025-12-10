# Nguyễn Duy Hiếu; Msv: 245752021610054
#Khai báo hàm, mở file đọc và lưu vào biến content
def find_longest_words(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
#Tách nội dung, tìm độ dài lớn nhất và tạo danh sách các từ vừa tìm được
        words = content.split()
        max_len = max(len(word) for word in words)
        longest_words = [word for word in words if len(word) == max_len]
    print("Các từ dài nhất là:", longest_words)
find_longest_words('D:/a.txt')
