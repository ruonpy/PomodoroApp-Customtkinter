from customtkinter import (
    CTkFrame,
    CTkSlider,
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
from pygame import mixer
from threading import Thread
from time import sleep
class Pomodoro(CTk):
    def __init__(self):
        super().__init__()
        self.title("Pomodoro App")
        self.geometry(f"{settings.X}x{settings.Y}")
        self.pomodoro_count=0
        self.work_time=25*60
        self.break_time=5*60
        self.run=False
        self.is_break=False
        self.break_text="Recharging..."
        self.ready_text="Ready to Start"
        self.work_text="Productivity Mode"
        self.pause_text="On Hold"
        self.current_time=self.work_time
        mixer.init()
        self.music_folder=os.path.join("musics")
        self.music_list=[file for file in os.listdir(self.music_folder) if file.endswith(".mp3")]
        self.music_on=False
        self.music_index=0
        self.paused_time=0
        self.icon_on = CTkImage(Image.open(os.path.join("images", "speaker-on.png")), size=(32, 32))
        self.icon_off = CTkImage(Image.open(os.path.join("images", "speaker-off.png")), size=(32, 32))
        set_appearance_mode("dark")
        set_default_color_theme("green")
        self.__tools_init()
        self.after(1000, self.check_music_end)
    def __tools_init(self):
        # ** tools **
        self.top_frame=CTkFrame(self, fg_color="transparent")
        self.middle_frame=CTkFrame(self, fg_color="transparent")
        self.bottom_frame=CTkFrame(self, fg_color="transparent")
        self.lbl_time=CTkLabel(self.middle_frame, text="25:00",
                               font=("Arial", 48))
        self.lbl_status=CTkLabel(self.middle_frame, text=self.ready_text,
                                 font=("Arial", 20))
        self.btn_start=CTkButton(self.bottom_frame, text="START",
                                 font=("Arial bold", 24),
                                 command=self.start_timer)
        self.btn_pause=CTkButton(self.bottom_frame, text="PAUSE",
                                 font=("Arial bold", 24),
                                 command=self.pause_timer)
        self.btn_reset=CTkButton(self.bottom_frame, text="RESET",
                                 font=("Arial bold", 24),
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
        # - sliders -
        self.volume_slider=CTkSlider(self.top_frame, from_=0, to=1,
                                     number_of_steps=100, width=100,
                                     command=self.change_volume)
        self.volume_slider.set(0.5)
        # - labels -
        self.lbl_time.pack()
        self.lbl_status.pack()
        # - buttons -
        self.btn_speaker.pack()
        self.volume_slider.pack(pady=10)
        self.btn_start.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
        self.btn_pause.grid(row=1, column=0, padx=10, pady=10)
        self.btn_reset.grid(row=1, column=1, padx=10, pady=10)
    def load_music(self, index):
        path=os.path.join(self.music_folder, self.music_list[index])
        mixer.music.load(path)
    def toggle_music(self):
        self.music_on=not self.music_on
        if self.music_on:
            if self.paused_time==0:
                self.load_music(self.music_index)
                mixer.music.play(start=0)
            else:
                mixer.music.play(start=self.paused_time)
            self.btn_speaker.configure(image=self.icon_on)
        else:
            self.paused_time=mixer.music.get_pos()/1000
            mixer.music.pause()
            self.btn_speaker.configure(image=self.icon_off)
    def check_music_end(self):
        if self.music_on:
            if not mixer.music.get_busy():
                self.paused_time=0
                self.music_index=(self.music_index+1)%len(self.music_list)
                self.load_music(self.music_index)
                mixer.music.play()
        self.after(1000, self.check_music_end)
    def change_volume(self, value):
        mixer.music.set_volume(float(value))
    def format_time(self, seconds):
        minutes=seconds//60
        secs=seconds%60
        return f"{minutes:02}:{secs:02}"
    def start_timer(self, break_time: bool=False):
        if not self.run or break_time:
            self.run=True
            self.lbl_status.configure(text=self.work_text if not break_time else self.break_text)
            Thread(target=self.countdown).start()
    def pause_timer(self):
        if self.run:
            self.run=False
            self.lbl_status.configure(text=self.pause_text)
    def reset_timer(self):
        self.run=False
        self.is_break=False
        self.current_time=self.work_time
        self.lbl_time.configure(text="25:00")
        self.lbl_status.configure(text=self.ready_text)
    def countdown(self):
        while self.run and self.current_time>0:
            sleep(1)
            self.current_time-=1
            self.lbl_time.configure(text=self.format_time(self.current_time))
        if self.run:
            if self.is_break:
                self.current_time=self.work_time
                self.is_break=False
                self.pomodoro_count+=1
            else:
                self.current_time=self.break_time
                self.is_break=True
            self.start_timer(break_time=True)

            
if __name__=="__main__":
    root=Pomodoro()
    root.mainloop()