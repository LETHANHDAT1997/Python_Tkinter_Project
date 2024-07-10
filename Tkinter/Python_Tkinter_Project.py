import tkinter as tk

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Ví dụ Tkinter")

# Đặt kích thước cửa sổ
root.geometry("1280x720")

# Thay đổi màu nền của cửa sổ
root.configure(bg="#FFBF00")

# Hàm để thay đổi văn bản của nhãn khi nút được nhấn
def on_button_click(event):
    label.config(text="Nút đã được nhấn!")

# Hàm thực thi khi nút được nhấn giữ
def on_button_press(event):
    button.config(bg="#FFBF00",fg="#FFBF00")

# Hàm thực thi khi nút được nhả
def on_button_release(event):
    button.config(bg="#FFBF00",fg="#FFBF00")

# Tạo một nhãn (label) và thiết lập màu nền của nhãn để phù hợp với cửa sổ
label = tk.Label(root, text="Xin chào, Tkinter!", bg="#ADD8E6")
label.pack(pady=0)

# Tạo đối tượng PhotoImage từ tệp ảnh
photo = tk.PhotoImage(file="open-folder_1_50x50.png")

# Tạo một nút (button) với màu nền và màu chữ tùy chỉnh khi nhấn
button = tk.Button(root , image=photo, command=on_button_click, border= 0, cursor='hand2', highlightthickness=0, bg="#FFBF00", fg="#FFBF00", relief="sunken")
button.pack(pady=0)
button.place(x=100,y=100)
button.bind("<ButtonPress-1>", on_button_press)
button.bind("<ButtonRelease-1>", on_button_release)

# Chạy vòng lặp chính
root.mainloop()
