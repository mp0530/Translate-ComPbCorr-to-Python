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
UserForm1 = tk.Tk() #create the windows
UserForm1.config(bg = "yellow")
font1 = Font(size = 12, slant = "italic", weight = "bold")
font2 = Font(size = 8, weight = "bold")
font3 = Font(size = 9, weight = "bold",slant = "italic")
font4 = Font(size = 7)
font5 = Font(size = 8, slant = "italic", weight = "bold")
font6 = Font(size = 15)
# Title
UserForm1.title("UserForm1")
# Size
UserForm1.geometry("600x900")
UserForm1.minsize(width=400,height=600)

label1 = tk.Label(UserForm1,text = "Composition of common-lead:", font = font3, fg = "#008000", bg = "yellow")
label2 = tk.Label(UserForm1,text = "Stacey - Kramers at",font = font2,fg = "green",bg = "yellow")
label3 = tk.Label(UserForm1,text = "Ga",font = font2,fg = "green",bg = "yellow")
label4 = tk.Label(UserForm1,text = "OR:",font = font2,fg = "green",bg = "yellow")
label5 = tk.Label(UserForm1,text = "206/204",font = font2,fg = "green",bg = "yellow")
label6 = tk.Label(UserForm1,text = "207/204",font = font2,fg = "green",bg = "yellow")
label7 = tk.Label(UserForm1,text = "208/204",font = font2,fg = "green",bg = "yellow")
label8 = tk.Label(UserForm1,text = "Age of lead-loss",font = font2,fg = "green",bg = "yellow")
label9 = tk.Label(UserForm1,text = "Ga",font = font2,fg = "green",bg = "yellow")
label10 = tk.Label(UserForm1,text = "Correlation of errors in 206Pb/238U and 207Pb/235U",font = font3,fg = "green",bg = "yellow")
label11 = tk.Label(UserForm1,text = "Using apparent error correlations from GLITTER output!",font = font4 ,fg = "green",bg = "yellow")
label12 = tk.Label(UserForm1,text = "Number of Monte-Carlo trials",font = font2,fg = "green",bg = "yellow")
label13 = tk.Label(UserForm1,text = "Sigma-level for discordance test (0, 1, 2....)",font = font2,fg = "green",bg = "yellow")

text1 = tk.Text(UserForm1,width = 6,height = 1.4)
text2 = tk.Text(UserForm1,width = 7,height = 1.4,font=("Helvetica", 12))
text3 = tk.Text(UserForm1,width = 7,height = 1.4,font=("Helvetica", 12))
text4 = tk.Text(UserForm1,width = 7,height = 1.4,font=("Helvetica", 12))
text5 = tk.Text(UserForm1,width = 6,height = 1.4)
text6 = tk.Text(UserForm1,width = 5,height = 1.4,font=("Helvetica", 15))
text7 = tk.Text(UserForm1,width = 5,height = 1.4,font=("Helvetica", 15))
text8 = tk.Text(UserForm1,width = 4,height = 1.4,font=("Helvetica", 15))


ok = tk.Button(UserForm1,text = "OK",font = font1,bg = "green",fg = "yellow",width = 8,height = 1)
cancel = tk.Button(UserForm1,text = "Cancel",font = font1,bg = "green",fg = "yellow",width=8,height=1,command = UserForm1.quit)
change = tk.Button(UserForm1,text = "Change",font = font5,bg = "green",fg = "yellow",width=7,height=1)

checkbox1 = tk.Checkbutton(UserForm1,bg = "yellow",activebackground = "yellow",text = "Specify lead composition:",font = font2,fg = "green")
checkbox2 = tk.Checkbutton(UserForm1,bg = "yellow",activebackground = "yellow",text = "Constant error correlation\ncoefficient of:",justify = "left",font = font2,fg = "green")
checkbox3 = tk.Checkbutton(UserForm1,bg = "yellow",activebackground = "yellow",text = "Use observed error correlations\nfrom worksheet, but use a constant\nvalue for blanks:",justify = "left",font = font2,fg = "green")
checkbox4 = tk.Checkbutton(UserForm1,bg = "yellow",activebackground = "yellow",text = "Use Discordance correction even when\nresult is inversely discordant",justify = "left",font = font2,fg = "green")
checkbox5 = tk.Checkbutton(UserForm1,bg = "yellow",activebackground = "yellow",text = "Enable 207Pb correction",justify = "left",font = font2,fg = "green")
checkbox6 = tk.Checkbutton(UserForm1,bg = "yellow",activebackground = "yellow",text = "Enable 208Pb correction",justify = "left",font = font2,fg = "green")
checkbox7 = tk.Checkbutton(UserForm1,bg = "yellow",activebackground = "yellow",text = "Show Tera-Wasserburg style output (columns BF-BJ)",justify = "left",font = font2,fg = "green")

separator1 = ttk.Separator(UserForm1,orient = "horizontal")
separator2 = ttk.Separator(UserForm1,orient = "horizontal")

separator1.place(x = 0, rely = 0.47, relwidth = 2)
separator1.lower()
separator2.place(x = 0, rely = 0.67, relwidth = 2)

label1.place(relx = 0.06, rely = 0.12)
label2.place(relx = 0.06, rely = 0.17)
label3.place(relx = 0.55, rely = 0.17)
label4.place(relx = 0.1, rely = 0.23)
label5.place(relx = 0.168, rely = 0.312)
label6.place(relx = 0.368, rely = 0.312)
label7.place(relx = 0.568, rely = 0.312)
label8.place(relx = 0.1, rely = 0.4)
label9.place(relx = 0.55, rely = 0.4)
label10.place(relx = 0.5, rely = 0.455, anchor = "n")
label11.place(relx = 0.1, rely = 0.555)
label12.place(relx = 0.06, rely = 0.7)
label13.place(relx = 0.06, rely = 0.815)

text1.place(relx = 0.37, rely = 0.17)
text2.place(relx = 0.15, rely = 0.345)
text3.place(relx = 0.35, rely = 0.345)
text4.place(relx = 0.55, rely = 0.345)
text5.place(relx = 0.37, rely = 0.4)
text6.place(relx = 0.7, rely = 0.5)
text7.place(relx = 0.7, rely = 0.58)
text8.place(relx = 0.64, rely = 0.81)

ok.place(relx = 0.7, rely = 0.03)
cancel.place(relx = 0.7, rely = 0.1)
change.place(relx = 0.47, rely = 0.695)

checkbox1.place(relx = 0.06, rely = 0.26)
checkbox2.place(relx = 0.06, rely = 0.5)
checkbox3.place(relx = 0.06, rely = 0.58)
checkbox4.place(relx = 0.06, rely = 0.75)
checkbox5.place(relx = 0.06, rely = 0.85)
checkbox6.place(relx = 0.06, rely = 0.90)
checkbox7.place(relx = 0.06, rely = 0.95)

UserForm1.mainloop()
