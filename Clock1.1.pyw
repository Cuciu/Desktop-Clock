from tkinter import *
from tkinter.ttk import *

# retrieve system's time
from time import strftime

# creating tkinter window
root = Tk()
root.attributes('-alpha', 0.5) #define transparency
root.overrideredirect(-1) #eliminate windows borders
#define possition
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry("195x62+%d+%d" % (screen_width-195, screen_height-102))

root.wm_attributes("-topmost", 1) #always on top for windows / root.lift() for linux


def time():
    string = strftime('%H:%M %p')
    lbl.config(text=string)
    lbl.after(1000, time)

# Styling the label widget so that clock
lbl = Label(root, font=('calibri', 36, 'bold'),
            background='mediumturquoise',
            foreground='white')

# Placing clock at the centre of the tkinter window
lbl.pack(anchor='center')
time()

mainloop()