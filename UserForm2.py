import tkinter as tk
from tkinter.font import Font
from tkinter import ttk
# ---------- To solve resolution issue in Windows -----------
import ctypes
import sys

if __name__ == "__main__":
    if 'win' in sys.platform:
        ctypes.windll.shcore.SetProcessDpiAwareness(1)
# -----------------------------------------------------------

ga = 100
UserForm2 = tk.Tk() #create the windows
UserForm2.config(bg = "yellow")
UserForm2.geometry("1000x800")

font1 = Font(size = 36, weight = "bold")
font2 = Font(size = 12, weight = "bold")
font3 = Font(size = 14, weight = "bold")
font4 = Font(size = 16, weight = "bold", slant = "italic")

accept = tk.Button(UserForm2,text = "Accept!",font = font4,bg = "green",fg = "yellow",width = 8,height = 1)
cancel = tk.Button(UserForm2,text = "Cancel",font = font4,bg = "green",fg = "yellow",width = 8,height = 1,command = UserForm2.quit)

label1 = tk.Label(UserForm2,text = "WARNING!", font = font1, fg = "red", bg = "yellow")
label2 = tk.Label(UserForm2,text = "You have chosen your analyses to a lead-loss event at", font = font2, fg = "red", bg = "yellow")
label3 = tk.Label(UserForm2,text = "Ga", font = font2, fg = "red", bg = "yellow")
label4 = tk.Label(UserForm2,text = ga, font = font2, fg = "black", bg = "yellow")
label5 = tk.Label(UserForm2,text = "This correction routine assumes that the discordance\n\
pattern is entirely due to lead-loss at a fixed time.\n\
Therefore do not use corrected data to construct\n\
lead-loss lines to any other lower intercept age!", font = font3, fg = "red", bg = "yellow")

accept.place(relx = 0.35, rely = 0.75, anchor = "center")
cancel.place(relx = 0.65, rely = 0.75, anchor = "center")

label1.place(relx = 0.5, rely = 0.15, anchor = "center")
label2.place(relx = 0.4, rely = 0.27, anchor = "center")
label3.place(relx = 0.9, rely = 0.27, anchor = "center")
label4.place(relx = 0.8, rely = 0.27, anchor = "center")
label5.place(relx = 0.5, rely = 0.4, anchor = "center")

UserForm2.mainloop()
