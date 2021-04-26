from tkinter import *
from time import strftime

def time():
    string = strftime('%H:%M %p')
    lbl.config(text=string)
    lbl.after(1000, time)

def Close():
    root.destroy()

class App:
    def __init__(self, master):
        fm = Frame(master)
        exit_button = Button(root, text="Exit", command=Close)
        exit_button.pack(pady=10, side=RIGHT)
        fm.pack(fill=BOTH, expand=YES)


root = Tk()
root.attributes('-alpha', 0.5) #define transparency
root.overrideredirect(-1) #eliminate windows borders
root.option_add('*font', ('verdana', 12, 'bold'))
root.title("Alex Clock")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry("250x62+%d+%d" % (screen_width-250, screen_height-102))
root.wm_attributes("-topmost", 1) #always on top for windows / root.lift() for linux
display = App(root)

lbl = Label(root, font=('calibri', 36, 'bold'),
            background='mediumturquoise',
            foreground='white')
# Placing clock at the centre of the tkinter window
lbl.pack(anchor='center')
time()

root.mainloop()
