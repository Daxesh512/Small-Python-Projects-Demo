import customtkinter as ctk
import time


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue") 

class Stopwatch(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Colorful Stopwatch")
        self.geometry("600x300")
        self.configure(bg='black') 

        frame = ctk.CTkFrame(self, fg_color="black")
        frame.pack(expand=True, fill="both")

        self.running = False
        self.start_time = 0
        self.elapsed_time = 0

        self.font_size = 72
        self.time_label = ctk.CTkLabel(frame, text="00:00:00.00", font=("Courier", self.font_size, "bold"), text_color="cyan")
        self.time_label.pack(pady=(60, 20), expand=True)

        buttons_frame = ctk.CTkFrame(frame, fg_color="black")
        buttons_frame.pack(pady=10)

        self.start_button = ctk.CTkButton(buttons_frame, text="Start", command=self.start, fg_color="green", width=80)
        self.start_button.grid(row=0, column=0, padx=10)

        self.stop_button = ctk.CTkButton(buttons_frame, text="Stop", command=self.stop, fg_color="red", width=80)
        self.stop_button.grid(row=0, column=1, padx=10)

        self.reset_button = ctk.CTkButton(buttons_frame, text="Reset", command=self.reset, fg_color="blue", width=80)
        self.reset_button.grid(row=0, column=2, padx=10)

        size_frame = ctk.CTkFrame(frame, fg_color="black")
        size_frame.pack(pady=10)

        size_label = ctk.CTkLabel(size_frame, text="Adjust Size:", font=("Courier", 14), text_color="cyan")
        size_label.grid(row=0, column=0, padx=10)

        self.size_slider = ctk.CTkSlider(size_frame, from_=24, to=144, number_of_steps=24, command=self.adjust_size)
        self.size_slider.set(self.font_size)
        self.size_slider.grid(row=0, column=1, padx=10)

        self.update_clock()

    def update_clock(self):
        if self.running:
            current_time = time.time() - self.start_time + self.elapsed_time
        else:
            current_time = self.elapsed_time

        mins, secs = divmod(current_time, 60)
        hours, mins = divmod(mins, 60)
        hundredths = int((current_time - int(current_time)) * 100)

        time_text = f"{int(hours):02}:{int(mins):02}:{int(secs):02}.{hundredths:02}"
        self.time_label.configure(text=time_text)
        self.after(10, self.update_clock)

    def start(self):
        if not self.running:
            self.start_time = time.time()
            self.running = True

    def stop(self):
        if self.running:
            self.elapsed_time += time.time() - self.start_time
            self.running = False

    def reset(self):
        self.running = False
        self.elapsed_time = 0
        self.time_label.configure(text="00:00:00.00")

    def adjust_size(self, val):
        self.font_size = int(val)
        self.time_label.configure(font=("Courier", self.font_size, "bold"))

if __name__ == '__main__':
    app = Stopwatch()
    app.mainloop()
