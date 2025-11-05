import customtkinter as ctk
from time import strftime

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Beautiful Digital Clock")
app.geometry("400x150") 

clock_label = ctk.CTkLabel(app, font=("Courier", 48, "bold"), text_color="orange")
clock_label.pack(expand=True) 

def update_time():
    current_time = strftime('%H:%M:%S %p') 
    clock_label.configure(text=current_time)
    clock_label.after(1000, update_time) 

update_time()

app.mainloop()
