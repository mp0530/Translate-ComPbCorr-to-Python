import tkinter as tk
from tkinter.font import Font
from tkinter import ttk
# ---------- To solve resolution issue in Windows -----------
import ctypes
import sys
from globalval import globalval
if __name__ == "__main__":
    if 'win' in sys.platform:
        ctypes.windll.shcore.SetProcessDpiAwareness(1)
# -----------------------------------------------------------
class UserForm2:
    def __init__(self,master):
        self.UserForm2 = master #create the windows
        self.UserForm2.config(bg = "yellow")
        self.UserForm2.geometry("1000x800")

        self.font1 = Font(size = 36, weight = "bold")
        self.font2 = Font(size = 12, weight = "bold")
        self.font3 = Font(size = 14, weight = "bold")
        self.font4 = Font(size = 16, weight = "bold", slant = "italic")

        self.accept = tk.Button(self.UserForm2,text = "Accept!",font = self.font4,bg = "green",fg = "yellow",width = 8,height = 1)
        self.cancel = tk.Button(self.UserForm2,text = "Cancel",font = self.font4,bg = "green",fg = "yellow",width = 8,height = 1,command = self.UserForm2.quit)

        self.label1 = tk.Label(self.UserForm2,text = "WARNING!", font = self.font1, fg = "red", bg = "yellow")
        self.label2 = tk.Label(self.UserForm2,text = "You have chosen your analyses to a lead-loss event at", font = self.font2, fg = "red", bg = "yellow")
        self.label3 = tk.Label(self.UserForm2,text = "Ga", font = self.font2, fg = "red", bg = "yellow")
        self.label4 = tk.Label(self.UserForm2,text = globalval.leadlossage, font = self.font2, fg = "black", bg = "yellow")
        self.label5 = tk.Label(self.UserForm2,text = "This correction routine assumes that the discordance\n\
        pattern is entirely due to lead-loss at a fixed time.\n\
        Therefore do not use corrected data to construct\n\
        lead-loss lines to any other lower intercept age!", font = self.font3, fg = "red", bg = "yellow")

        self.accept.place(relx = 0.35, rely = 0.75, anchor = "center")
        self.cancel.place(relx = 0.65, rely = 0.75, anchor = "center")

        self.label1.place(relx = 0.5, rely = 0.15, anchor = "center")
        self.label2.place(relx = 0.4, rely = 0.27, anchor = "center")
        self.label3.place(relx = 0.9, rely = 0.27, anchor = "center")
        self.label4.place(relx = 0.8, rely = 0.27, anchor = "center")
        self.label5.place(relx = 0.5, rely = 0.4, anchor = "center")

        # self.UserForm2.mainloop()


