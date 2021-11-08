########################################################################
# Voov Automation Software 
## Naem Azam  naemazam.github.io
## steve    https://github.com/KHOJIDDIN
######################################################################
import math
from datetime import datetime as dt
from selenium import webdriver
from time import sleep
import tkinter as tk
from tkinter import *

timer = None
window = tk.Tk()
window.title('VooV Automation')
window.geometry("600x500")
window.minsize(100, 50)
window.maxsize(270, 200)
window.config(padx=20, pady=20, bg="#9bdeac")


def stop():
    countdown_label.config(text="")
    window.after_cancel(timer)


def start():
    time_now = dt.now().strftime('%H:%M:%S')
    time_in = time_entry.get()
    t = time_now.split(':')
    hour = int(t[0])
    mins = int(t[1])
    sec = int(t[2])
    user = time_in.split(":")
    user_hour = int(user[0])
    user_mins = int(user[1])
    secs = ((((user_hour - hour) * 60) + (user_mins - mins)) * 60) - sec
    link_label.grid_forget()
    time_label.grid_forget()
    submit_button.grid_forget()
    link_entry.grid_forget()
    time_entry.grid_forget()
    countdown_label.config(font=('Courier', 70, 'bold'))
    schedule_meeting(secs)


def schedule_meeting(secs):
    global timer
    link = link_entry.get()

    minutes = math.floor((secs / 60))
    sec = secs % 60

    if secs == 0:
        stop()
        driver_selenium(link)

    if sec < 10:
        sec = f"0{sec}"
    countdown_label.config(text=f"{minutes}:{sec}")

    if secs > 0:
        timer = window.after(1000, schedule_meeting, secs-1)


link_label = Label(text="Enter the meeting link:", bg="#9bdeac", fg="white", font=("Courier", 11, 'bold'))
link_label.grid(column=0, row=1)
time_label = Label(text="Meeting Time 24H(22:22):", bg="#9bdeac", fg="white", font=("Courier", 11, 'bold'))
time_label.grid(column=0, row=3)
countdown_label = Label(bg="#9bdeac", fg="blue", font=("Courier", 11, 'bold'))
countdown_label.grid(column=0, row=5)


link_entry = Entry(window, font=("Arial", 14))
link_entry.grid(column=0, row=2)

time_entry = Entry(window, font=("Arial", 14))
time_entry.grid(column=0, row=4)

image = PhotoImage(file="assets/button.png")
submit_button = Button(image=image, command=start)
submit_button.grid(column=0, row=6)


def driver_selenium(data_link):
    options = webdriver.ChromeOptions()
    options.add_argument("user-data-dir=C:\\google_path_for_selenium\\Profile")
    driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options)

    driver.get(data_link)

    button = driver.find_element_by_xpath("/html/body/div/div/div/div[4]/div[2]/button[3]")
    button.click()
    sleep(20)
    driver.quit()


window.mainloop()


