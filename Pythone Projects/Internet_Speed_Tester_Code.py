#pip install speedtest-cli

import customtkinter as ctk
try:
    import speedtest 
except ImportError:
    print("Error: Could not import speedtest. Please install 'speedtest-cli' via pip.")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue") 

app = ctk.CTk()
app.title("Beautiful Internet Speed Test")
app.geometry("400x300")
app.configure(bg='black')  

frame = ctk.CTkFrame(app, fg_color="black")
frame.pack(expand=True, fill="both")

download_label = ctk.CTkLabel(frame, text="Download: -- Mbps", font=("Courier", 20, "bold"), text_color="cyan")
download_label.pack(pady=10)

upload_label = ctk.CTkLabel(frame, text="Upload: -- Mbps", font=("Courier", 20, "bold"), text_color="cyan")
upload_label.pack(pady=10)

ping_label = ctk.CTkLabel(frame, text="Ping: -- ms", font=("Courier", 20, "bold"), text_color="cyan")
ping_label.pack(pady=10)

status_label = ctk.CTkLabel(frame, text="", font=("Courier", 14), text_color="yellow")  # For error messages
status_label.pack(pady=5)

def run_speed_test():
    try:
        status_label.configure(text="Testing... Please wait.")
        st = speedtest.Speedtest() 
        download_speed = round(st.download() / 1_000_000, 2)  
        upload_speed = round(st.upload() / 1_000_000, 2)      
        ping = round(st.results.ping, 2)                      
        
        download_label.configure(text=f"Download: {download_speed} Mbps")
        upload_label.configure(text=f"Upload: {upload_speed} Mbps")
        ping_label.configure(text=f"Ping: {ping} ms")
        status_label.configure(text="Test complete!")
    except Exception as e:
        status_label.configure(text=f"Error: {str(e)}. Check installation.")
        print(f"Debug: {str(e)}")  

test_button = ctk.CTkButton(frame, text="Test Speed", command=run_speed_test, fg_color="dodgerblue", width=150)
test_button.pack(pady=20)

app.mainloop()
