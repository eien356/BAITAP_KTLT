# Nguyễn Duy Hiếu; Msv: 245752021610054
import tkinter as tk
#Tạo cửa sổ Tkinter
root = tk.Tk()
root.title("Thông tin cá nhân")
root.geometry("400x200")
#Tạo các Label để hiển thị thông tin
tk.Label(root, text="Họ tên: Nguyễn Duy Hiếu ", font=("Arial", 12)).pack(anchor="w")
tk.Label(root, text="Ngày sinh: 03/05/2006", font=("Arial", 12)).pack(anchor="w")
tk.Label(root, text="MSSV:245752021610054 ", font=("Arial", 12)).pack(anchor="w")
tk.Label(root, text="Ngành học: ktđktđh ", font=("Arial", 12)).pack(anchor="w")

root.mainloop()

import tkinter as tk
from tkinter import messagebox
#Tạo cửa sổ mới
root = tk.Tk()
root.title("Radio Button Demo")
root.geometry("300x200")
#Tạo biến IntVar để lưu lựa chọn
v = tk.IntVar()
v.set(1) 
#Tạo 3 RadioButton

tk.Radiobutton(root, text="Lựa chọn 1", variable=v, value=1).pack(anchor="w")
tk.Radiobutton(root, text="Lựa chọn 2", variable=v, value=2).pack(anchor="w")
tk.Radiobutton(root, text="Lựa chọn 3", variable=v, value=3).pack(anchor="w")
#Tạo hàm show_choice()
def show_choice():
    messagebox.showinfo("Thông báo", f"Bạn đã chọn: {v.get()}")
#Tạo nút Button để xem lựa chọn
btn = tk.Button(root, text="Click Me", command=show_choice)
btn.pack(pady=10)

root.mainloop()
