import customtkinter as ctk
from PIL import Image

# Tạo hàm xử lí event chung cho cửa số chính
def app_handle_event(event):
    pass

# Khởi tạo cửa sổ giao diện chính với màu, kích thước, không cho thay đổi kích thước, đặt tên cửa sổ
app = ctk.CTk(fg_color = "#FFBF00")
app.geometry("1280x720")
app.resizable(False,False)
app.title("Entry")

# Chưa rõ lí do nhưng Button không thể đổi màu khi nhấn giữ nếu không chạy các hàm sau
app.bind_all("<Enter>", app_handle_event)
app.bind_all("<Configure>", app_handle_event)

# THêm hình ảnh
# Tạo đối tượng hình ảnh từ tệp ảnh
img_data = Image.open("open-folder.png")
img = ctk.CTkImage(dark_image=img_data, light_image=img_data, size=(50, 50))

# Hàm xử lí event khi con lăn chuột di chuyển
def Entry_Pass_Handle(event):
    print("Entry Handle")

# Tạo một entry
entry_Pass=ctk.CTkEntry(master=app, width=220, text_color="#ff5252", placeholder_text='Password', placeholder_text_color="#ff5252" , font=("Tahoma", 11, "bold"), show="*", fg_color="#f7f1e3", bg_color="transparent", border_width=2, border_color="#2C3A47")
entry_Pass.place(x=50, y=110)
# Add một xử lí event khi con lăn chuột di chuyển
entry_Pass.bind("<MouseWheel>",Entry_Pass_Handle)

app.mainloop()
