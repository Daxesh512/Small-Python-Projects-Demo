import customtkinter as ctk
import math
from datetime import datetime

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class ResponsiveAnalogClock(ctk.CTkCanvas):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.hand_items = []
        self.day_text_item = None
        self.date_text_item = None
        self.bind('<Configure>', self.on_resize)
        self.center_x = self.winfo_reqwidth() // 2
        self.center_y = self.winfo_reqheight() // 2
        self.radius = min(self.center_x, self.center_y) - 40

    def on_resize(self, event):
        self.center_x = event.width // 2
        self.center_y = event.height // 2
        self.radius = min(self.center_x, self.center_y) - 40
        self.configure(bg="black")
        self.draw_clock_face()

    def draw_clock_face(self):
        self.delete("all")  
        bark_color = "#4B3621"  
        self.create_oval(self.center_x - self.radius, self.center_y - self.radius,
                         self.center_x + self.radius, self.center_y + self.radius,
                         fill=bark_color, outline="#654321", width=8)

        tick_color = "#A0522D"  
        for i in range(12):
            angle = math.pi / 6 * i
            x_start = self.center_x + (self.radius - 24) * math.sin(angle)
            y_start = self.center_y - (self.radius - 24) * math.cos(angle)
            x_end = self.center_x + self.radius * math.sin(angle)
            y_end = self.center_y - self.radius * math.cos(angle)
            self.create_line(x_start, y_start, x_end, y_end, fill=tick_color, width=4)

        for i in range(1, 13):
            angle = math.pi / 6 * (i - 3)
            x = self.center_x + (self.radius - 45) * math.cos(angle)
            y = self.center_y + (self.radius - 45) * math.sin(angle)
            self.create_text(x, y, text=str(i), fill="#D2B48C", font=("Arial", max(int(self.radius/14), 15), "bold"))

        self.draw_day_and_date()
        self.update_clock()

    def draw_day_and_date(self):
        now = datetime.now()
        day = now.strftime('%A')
        full_date = now.strftime('%B %d, %Y')
        day_y = self.center_y - self.radius * 0.7
        date_y = self.center_y + self.radius * 0.7

        if self.day_text_item:
            self.delete(self.day_text_item)
        if self.date_text_item:
            self.delete(self.date_text_item)

        self.day_text_item = self.create_text(
            self.center_x, day_y,
            text=day, fill="#DEB887",
            font=("Arial", max(int(self.radius/10), 25), "bold")
        )
        self.date_text_item = self.create_text(
            self.center_x, date_y,
            text=full_date, fill="#DEB887",
            font=("Arial", max(int(self.radius/12), 18))
        )

    def update_clock(self):
        for item in self.hand_items:
            self.delete(item)
        self.hand_items.clear()

        now = datetime.now()
        hour = now.hour % 12
        minute = now.minute
        second = now.second + now.microsecond / 1_000_000

        colors = {"hour": "#8B4513", "minute": "#DEB887", "second": "#CD5C5C"}

        hour_angle = (hour + minute / 60.0) * math.pi / 6
        minute_angle = (minute + second / 60.0) * math.pi / 30
        second_angle = second * math.pi / 30

        hx = self.center_x + 0.5 * self.radius * math.sin(hour_angle)
        hy = self.center_y - 0.5 * self.radius * math.cos(hour_angle)
        mx = self.center_x + 0.75 * self.radius * math.sin(minute_angle)
        my = self.center_y - 0.75 * self.radius * math.cos(minute_angle)
        sx = self.center_x + 0.9 * self.radius * math.sin(second_angle)
        sy = self.center_y - 0.9 * self.radius * math.cos(second_angle)

        self.hand_items.append(self.create_line(self.center_x, self.center_y, hx, hy, fill=colors["hour"], width=max(int(self.radius/35), 10)))
        self.hand_items.append(self.create_line(self.center_x, self.center_y, mx, my, fill=colors["minute"], width=max(int(self.radius/60), 5)))
        self.hand_items.append(self.create_line(self.center_x, self.center_y, sx, sy, fill=colors["second"], width=max(int(self.radius/90), 3)))

        r = max(int(self.radius/25), 10)
        self.hand_items.append(self.create_oval(self.center_x - r, self.center_y - r, self.center_x + r, self.center_y + r, fill="#8B4513", outline=""))

        self.draw_day_and_date()
        self.after(50, self.update_clock)

if __name__ == "__main__":
    app = ctk.CTk()
    app.title("Responsive Analog Clock")
    app.geometry("800x800")
    clock = ResponsiveAnalogClock(app)
    clock.pack(expand=True, fill='both')
    app.mainloop()
