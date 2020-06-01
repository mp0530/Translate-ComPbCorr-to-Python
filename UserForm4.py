import tkinter as tk
from tkinter.font import Font
from tkinter import ttk
# ---------- To solve resolution issue in Windows -----------
import ctypes
import sys
from globalval import globalval
from UserForm2 import UserForm2
if __name__ == "__main__":
    if 'win' in sys.platform:
        ctypes.windll.shcore.SetProcessDpiAwareness(1)
# -----------------------------------------------------------

class UserForm4:
    def __init__(self,master4,close,prevmaster,prev_monte_trials):
        self.close = close
        self.prevmaster = prevmaster
        self.prev_monte_trials = prev_monte_trials
        self.UserForm4 = master4 #create the windows
        master4.title("Monte-Carlo error estimate")
        master4.config(bg = "yellow")
        master4.geometry("480x300")

        self.font1 = Font(size = 12, weight = "bold")

        self.ok = tk.Button(master4,text = "OK",font = self.font1,bg = "green",fg = "yellow",width = 8,height = 1,command = self.monte)

        self.label1 = tk.Label(master4,text = "Set number of trials to",font = self.font1,fg = "green",bg = "yellow")
        self.label2 = tk.Label(master4,text = "n >(>) 100!",font = self.font1,fg = "green",bg = "yellow")

        self.montetrial = tk.IntVar()
        self.montetrial.set(self.prev_monte_trials.get())
        # print(self.monte_trials.get())
        self.entry1 = tk.Entry(master4,width = 4,font=("Helvetica", 18),justify = "center",
                              textvariable = self.montetrial,state = "normal")
        self.montetrial.trace("w", self.checkval)
        self.label1.place(relx = 0.35, rely = 0.4, anchor = "center")
        self.entry1.place(relx = 0.85, rely = 0.4, anchor = "e")
        self.label2.place(relx = 0.3, rely = 0.65, anchor = "center")
        self.ok.place(relx = 0.9, rely = 0.9, anchor = "se")
        # self.UserForm4.mainloop()

    def monte(self):
        if self.montetrial.get() < 100:
            self.label2.config(fg = "red")
        else:
            globalval.monte_trials = self.entry1.get()
            self.UserForm4.destroy()
            if self.close:
                self.prevmaster.destroy()
                root = tk.Tk()
                app = UserForm2(root)
            else:
                self.prev_monte_trials.set(globalval.monte_trials)

    def checkval(self,*args):
        if self.montetrial.get() < 100:
            self.entry1.config(fg = "red")
        else:
            self.entry1.config(fg = "black")
