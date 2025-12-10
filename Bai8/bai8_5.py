# Nguyễn Duy Hiếu; Msv: 245752021610054
import tkinter as tk
#Tạo cửa sổ Tkinter
root = tk.Tk()
root.title("Ví dụ Indicator Radio Button")
#Tạo biến IntVar để lưu lựa chọn của RadioButton
v = tk.IntVar()
v.set(1)
#Tạo danh sách các ngôn ngữ và giá trị tương ứng
languages = [
    ("Python", 1),
    ("Perl", 2),
    ("Java", 3),
    ("C++", 4),
    ("C", 5)
]
#Hàm ShowChoice() in ra lựa chọn
def ShowChoice():
    print("Bạn chọn:", v.get())
#Tạo nhãn hướng dẫn
tk.Label(root,
         text="Chọn ngôn ngữ lập trình yêu thích:",
         justify=tk.LEFT,
         padx=20).pack()
for language, val in languages:
#Tạo các RadioButton dạng nút bấm (indicatoron=0)
  tk.Radiobutton(root,
                   text=language,
                   indicatoron=0,   
                   width=20,
                   padx=20,
                   variable=v,
                   command=ShowChoice,
                   value=val).pack(anchor=tk.W)

root.mainloop()
