# Using tkinter
from tkinter import *
import os

def Restart():
    os.system("shutdown /r /t 1")

def Restart_Time():
    os.system("shutdown /r /t 20")

def LogOut():
    os.system("shutdown -l")

def Shutdown():
    os.system("shutdown /s /t 1")


st = Tk()                           # Making an Object variable for Shutdown. Tk Class
st.title("Shutdown App")
st.geometry("240x235")
st.config(bg = "Red")              # Configure Background colour

r_button = Button(st, text = "Restart", font = ("Time New Roman", 20, "bold"),
                  relief = RAISED, cursor = "plus", command=Restart)
r_button.place(x=15, y=15, height=40, width=210)

rt_button = Button(st, text = "Timed Restart", font = ("Time New Roman", 20, "bold"),
                   relief = RAISED, cursor = "plus", command=Restart_Time)
rt_button.place(x=15, y=70, height=40, width=210)

lg_button = Button(st, text = "Log Out", font = ("Time New Roman", 20, "bold"),
                   relief = RAISED, cursor = "plus", command=LogOut)
lg_button.place(x=15, y=125, height=40, width=210)

sd_button = Button(st, text = "Shutdown", font = ("Time New Roman", 20, "bold"),
                   relief = RAISED, cursor = "plus", command=Shutdown)
sd_button.place(x=15, y=180, height=40, width=210)



st.mainloop()                       # To see UI always. mainloop fn