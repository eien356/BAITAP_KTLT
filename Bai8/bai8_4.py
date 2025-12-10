# Nguyễn Duy Hiếu; Msv: 245752021610054
#Tạo cửa sổ Tkinter
from tkinter import * 
window = Tk() 
window.title("Chào mừng đến LikeGeeks app") 
window.geometry('350x200') 
#Tạo nhãn (Label) và hiển thị lên cửa sổ
lbl = Label(window, text="Xin chào") 
lbl.grid(column=0, row=0) 
#Định nghĩa hàm khi nhấn nút
def clicked(): 
    lbl.configure(text="Bạn đã nhấn nút !!") 
#Tạo nút bấm liên kết với hàm clicked()
btn = Button(window, text="Click Me", command=clicked) 
btn.grid(column=1, row=0) 
window.mainloop()
