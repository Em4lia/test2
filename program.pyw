# MODIFIED
# VERSION 2
# NEW BRANCH

from tkinter import *
import random
root = Tk()
w, h = root.winfo_screenwidth()//2-200, root.winfo_screenheight()//2-150
root.title("")
root.geometry(f"400x300+{w}+{h}")
root.resizable(height=False, width=False)

#root.overrideredirect(True)
#root.lift()
root.wm_attributes("-transparentcolor", "white")


root["bg"] = "white" #"sandy brown"
bg1 = "royalblue2"
bg2 = "firebrick1"
def color(event):
    global bg1, bg2
    bg1 == "DodgerBlue4"
    bg1 = "royalblue2"
    bg2 = "firebrick1"
    button["bg"] = bg2
c = 0
def click(event):
    global c
    if c==0:
        label.place(x="0", y="0")
        button["text"] = ""
        button["font"] = ("Arial", 8, "bold")
    if c%10 == 0 and c!=0:
        button["bg"] = bg1
    else:
        button["bg"] = bg2
    c+=1
    button["width"], button["height"] = str(random.randint(1, 9)), str(random.randint(1, 3))
    label["text"] = c-1
    button.place(x=str(random.randint(3, 320)), y=str(random.randint(5, 260)))
label = Button(text=c, font=("Arial", 13, "bold"), bg = "white", relief=GROOVE, border=0)
label.bind('<Button-1>', color)
button = Button(text="Start", width="5", height="1", bg="grey", foreground="Black", font=("Arial", 20, "bold"))
button.bind('<Button-1>', click)
button.place(x="150", y="113")
root.mainloop()