# Nguyễn Duy Hiếu; Msv: 245752021610054
#Khởi tạo lớp WordReverser nhận một chuỗi văn bản
class WordReverser:
    def __init__(self, text):
        self.text = text
#Tách chuỗi và đảo ngược từ sau đó nối lại cách nhau bởi dấu cách
    def reverse_words(self):
        words = self.text.split()
        reversed_words = words[::-1]
        return ' '.join(reversed_words)
s = WordReverser("hello .py")
print(s.reverse_words())  
