from tkinter import *
import os


def logout():
    return os.system("shutdown -l")

def shutdown():
    return os.system("shutdown /s /t 1")

def restart():
    return os.system("shutdown /r /t 1")

sd = Tk()
sd.title("ShutDown")
sd.config(bg="red")
sd.geometry("300x300")

button = Button(sd, text="Logout", font="bold",command=logout)
button.place(x=100, y=40, height=40, width=90)

button1 = Button(sd, text="Shutdown", font="bold",command=shutdown)
button1.place(x=100, y=120, height=40, width=90)

button2 = Button(sd, text="Restart", font="bold", command=restart)
button2.place(x=100, y=200, height=40, width=90)


sd.mainloop()