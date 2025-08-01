from customtkinter import (
    CTkFrame,
    CTkLabel,
    CTkButton,
    CTkImage,
    CTk,
    set_appearance_mode,
    set_default_color_theme
)
from PIL import Image
from config import settings
import os
class Pomodoro(CTk):
    def __init__(self):
        super().__init__()
        self.title("Pomodoro App")
        self.geometry(f"{settings.X}x{settings.Y}")
        self.work_time=25*60
        self.break_time=5*60
        self.run=False
        self.is_break=False
        self.time=self.work_time
        self.music_on=False
        self.icon_on = CTkImage(Image.open(os.path.join("images", "speaker-on.png")), size=(32, 32))
        self.icon_off = CTkImage(Image.open(os.path.join("images", "speaker-off.png")), size=(32, 32))
        set_appearance_mode("dark")
        set_default_color_theme("green")
        self.__tools_init()
    def __tools_init(self):
        # ** tools **
        self.top_frame=CTkFrame(self, fg_color="transparent")
        self.middle_frame=CTkFrame(self, fg_color="transparent")
        self.bottom_frame=CTkFrame(self, fg_color="transparent")
        self.lbl_time=CTkLabel(self.middle_frame, text="00:00",
                               font=("Arial", 48))
        self.lbl_status=CTkLabel(self.middle_frame, text="READY",
                                 font=("Arial", 20))
        self.btn_start=CTkButton(self.bottom_frame, text="START",
                                 command=self.start_timer)
        self.btn_stop=CTkButton(self.bottom_frame, text="STOP",
                                command=self.stop_timer)
        self.btn_pause=CTkButton(self.bottom_frame, text="STOP",
                                 command=self.pause_timer)
        self.btn_reset=CTkButton(self.bottom_frame, text="STOP",
                                 command=self.reset_timer)
        self.btn_speaker=CTkButton(self.top_frame, text="",
                                   image=self.icon_off,
                                   width=40, height=40,
                                   command=self.toggle_music)
        # ** tool placements **
        # - frames -
        self.top_frame.place(relx=1, rely=0,
                             anchor="ne", x=-10, y=10)
        self.middle_frame.pack(pady=40)
        self.bottom_frame.pack()
        # - labels -
        self.lbl_time.pack()
        self.lbl_status.pack()
        # - buttons -
        self.btn_speaker.pack()
        self.btn_start.grid(row=0, column=0, padx=10, pady=10)
        self.btn_stop.grid(row=0, column=1, padx=10, pady=10)
        self.btn_pause.grid(row=1, column=0, padx=10, pady=10)
        self.btn_reset.grid(row=1, column=1, padx=10, pady=10)
        
    def toggle_music(self):
        pass
    def start_timer(self):
        pass
    def stop_timer(self):
        pass
    def pause_timer(self):
        pass
    def reset_timer(self):
        pass

if __name__=="__main__":
    root=Pomodoro()
    root.mainloop()