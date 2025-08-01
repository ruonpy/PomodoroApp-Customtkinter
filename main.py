from customtkinter import (
    CTkLabel,
    CTkButton,
    CTk,
    set_appearance_mode,
    set_default_color_theme
)
from config import settings
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
        set_appearance_mode("dark")
        set_default_color_theme("green")
        self.__tools_init()
    def __tools_init(self):
        self.lbl_time=CTkLabel(self, text="00:00",
                               font=("Arial", 48))
        self.lbl_status=CTkLabel(self, text="READY",
                                 font=("Arial", 20))
        self.btn_start=CTkButton(self, text="START",
                                 command=self.start_timer)
        self.btn_stop=CTkButton(self, text="STOP",
                                command=self.stop_timer)
        self.btn_pause=CTkButton(self, text="STOP",
                                 command=self.pause_timer)
        self.btn_reset=CTkButton(self, text="STOP",
                                 command=self.reset_timer)
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