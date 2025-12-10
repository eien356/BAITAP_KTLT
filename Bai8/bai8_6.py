# Nguyễn Duy Hiếu; Msv: 245752021610054
from tkinter import *
from tkinter import messagebox
#Tạo cửa sổ Tkinter
root = Tk()
root.title("Demo Menu")
root.geometry("400x300")
#Tạo thanh menu chính
menu = Menu(root)
root.config(menu=menu)
#Tạo menu File
filemenu = Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=filemenu)
#Định nghĩa các hàm xử lý
def NewFile():
    messagebox.showinfo("Thông báo", "New File!")

def OpenFile():
    messagebox.showinfo("Thông báo", "Open File!")

def Exit():
    root.quit()
#Thêm các mục vào menu File
filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open", command=OpenFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=Exit)
#Tạo menu Insert
insertmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Insert", menu=insertmenu)

def InsText():
    messagebox.showinfo("Thông báo", "Text!")

def InsPic():
    messagebox.showinfo("Thông báo", "Picture!")

insertmenu.add_command(label="Text", command=InsText)
insertmenu.add_command(label="Picture", command=InsPic)
#Tạo menu Help
helpmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=lambda: messagebox.showinfo("Thông báo", "This is a simple example of a menu"))

root.mainloop()
