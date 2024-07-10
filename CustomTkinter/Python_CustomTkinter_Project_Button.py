import customtkinter as ctk
from PIL import Image

# Tạo hàm xử lí event chung cho cửa số chính
def app_handle_event(event):
    button.configure(fg_color = "#f1c40f")

# Khởi tạo cửa sổ giao diện chính với màu, kích thước, không cho thay đổi kích thước, đặt tên cửa sổ
app = ctk.CTk(fg_color = "#FFBF00")
app.geometry("1280x720")
app.resizable(False,False)
app.title("Button")

# Chưa rõ lí do nhưng Button không thể đổi màu khi nhấn giữ nếu không chạy các hàm sau
app.bind_all("<Enter>", app_handle_event)
app.bind_all("<Configure>", app_handle_event)

# THêm hình ảnh
# Tạo đối tượng hình ảnh từ tệp ảnh
img_data = Image.open("open-folder.png")
img = ctk.CTkImage(dark_image=img_data, light_image=img_data, size=(50, 50))

# Các hàm xử lí event cho nút nhấn
def button_callback():
    pass

def button_Press(event):
    button.configure(fg_color = "#f39c12")
    button.place(x=101, y=101)
    print("Button Press")
    print(event.type)

def button_Release(event):
    button.configure(fg_color = "#f1c40f")
    button.place(x=100, y=100)
    print("Button Release")

# Tạo nút nhấn
button = ctk.CTkButton(app, text="Import", text_color="#227093", font=("Tahoma", 14, "bold"), image=img, width=80, height=50, border_width=2, command=button_callback,fg_color = "#f39c12", hover_color="#f39c12", border_color="#4e4e4e")
button.pack(padx=20, pady=20)
button.place(x=100,y=100)

# Tạo event theo chuỗi format có sẵn,chi tiết https://dafarry.github.io/tkinterbook/tkinter-events-and-bindings.htm#events
# Add hàm xử lí event khi nhấn và nhả nút nhấn
button.bind("<ButtonPress-1>", button_Press) 
button.bind("<ButtonRelease-1>", button_Release)

app.mainloop()
