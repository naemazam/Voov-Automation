########################################################################
## Naem Azam
# YOUTUBE: (The Terminal Boy) https://www.youtube.com/naemazam
# WEBSITE: naemazam.github.io
########################################################################
import webbrowser
import schedule
from time import sleep
from threading import Thread

import tkinter as tk
from tkinter import *
from tkinter.ttk import Combobox


class voovBotGUI:
    def __init__(self, name):
        self.title = name
        self.window = tk.Tk()
        self.window.title(self.title)
        self.window.geometry("600x500")
        self.window.minsize(600, 500)
        self.window.maxsize(600, 500)

        self.main_bg = PhotoImage(file='assests/main bg.png')
        self.button = PhotoImage(file="assests/button.png")
        self.canvas = Canvas(self.window, width=600, height=500)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.main_bg, anchor="nw")

        self.scheduled_meetings_count = 0
        self.meetings = {}

        self.home_page()
    
    def show_error(self, text, pos):
        self.err_text = Label(self.window, text=text, font=("montserrat", 10), fg="green", bg="#E8E7E3")
        self.err_text.place(x=pos[0], y=pos[1])

    def schedule_meeting(self):
        time, link, day = self.meetings[self.scheduled_meetings_count - 1]
        if day == 'Everyday':
            schedule.every().day.at(time).do(webbrowser.open_new_tab, link)
        elif day == 'Monday':
            schedule.every().monday.at(time).do(webbrowser.open_new_tab, link)
        elif day == 'Tuesday':
            schedule.every().tuesday.at(time).do(webbrowser.open_new_tab, link)
        elif day == 'Wednesday':
            schedule.every().wednesday.at(time).do(webbrowser.open_new_tab, link)
        elif day == 'Thrusday':
            schedule.every().thursday.at(time).do(webbrowser.open_new_tab, link)
        elif day == 'Friday':
            schedule.every().friday.at(time).do(webbrowser.open_new_tab, link)
        elif day == 'Saturday':
            schedule.every().saturday.at(time).do(webbrowser.open_new_tab, link)
        elif day == 'Sunday':
            schedule.every().sunday.at(time).do(webbrowser.open_new_tab, link)

    def schedule(self):
        try:
            self.err_text.destroy()
        except AttributeError:
            pass

        link = self.link.get()
        hrs, mins = self.time.get().split(':')
        day = self.select_weekday.get()
        if 24 > int(hrs) > 0 and 60 > int(mins) > 0:
            if 'https://' in link:
                self.meetings[self.scheduled_meetings_count] = [f"{hrs}:{mins}", link, day]
                self.scheduled_meetings.insert(self.scheduled_meetings_count, f"Meeting at {day}, {hrs}:{mins}")
                self.scheduled_meetings_count += 1
                self.schedule_meeting()
                self.link.delete(0, END)
                self.time.delete(0, END)
            else:
                self.show_error("Invalid Meeting Link!", (26, 187))
        else:
            self.show_error("Invalid Time!", (26, 275))

    def home_page(self):
        self.link = Entry(self.window, font=("Arial", 14))
        self.link.place(x=26, y=162, width=196, height=25)

        self.time = Entry(self.window, font=("Arial", 14))
        self.time.place(x=26, y=250, width=196, height=25)
        
        self.select_weekday = Combobox(self.window, width=30, textvariable=tk.StringVar())
        self.select_weekday['values'] = ('Everyday', 'Monday', 'Tuesday', 'Wednesday', 'Thrusday', 'Friday', 'Saturday', 'Sunday')
        self.select_weekday.place(x=26, y=334, width=196, height=25)
        self.select_weekday.current()

        self.schedule_btn = Button(self.window, image=self.button, command=self.schedule, borderwidth=0, bg="#E8E7E3")
        self.schedule_btn.place(x=194, y=400)

        self.scheduled_meetings = Listbox(self.window, width=28, height=13, font=("Arial", 12))
        self.scheduled_meetings.place(x=310, y=120)

def scheduler():
    while True:
        schedule.run_pending()
        sleep(1)

if __name__ == "__main__":
    gui = voovBotGUI('Voov Automation')
    Thread(target=scheduler, daemon=True).start()
    gui.window.mainloop()
    