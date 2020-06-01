try:
    # for Python2
    import Tkinter as tk
except ImportError:
    # for Python3
    import tkinter as tk
from tkinter.font import Font
from tkinter import ttk
# ---------- To solve resolution issue in Windows -----------
import ctypes
import sys
import math
from globalval import globalval
from UserForm4 import UserForm4
from UserForm2 import UserForm2
if __name__ == "__main__":
    if 'win' in sys.platform:
        ctypes.windll.shcore.SetProcessDpiAwareness(1)

class UserForm1:
    def __init__(self,master1):
        self.master1 = master1
        master1.config(bg = "yellow")
        master1.title("UserForm1")
        master1.geometry("600x900")
        master1.minsize(width=400,height=600)

        self.font1 = Font(size = 12, slant = "italic", weight = "bold")
        self.font2 = Font(size = 8, weight = "bold")
        self.font3 = Font(size = 9, weight = "bold",slant = "italic")
        self.font4 = Font(size = 7)
        self.font5 = Font(size = 8, slant = "italic", weight = "bold")
        self.font6 = Font(size = 15)

        self.label1 = tk.Label(master1,text = "Composition of common-lead:", font = self.font3, fg = "#008000", bg = "yellow")
        self.label2 = tk.Label(master1,text = "Stacey - Kramers at",font = self.font2,fg = "green",bg = "yellow")
        self.label3 = tk.Label(master1,text = "Ga",font = self.font2,fg = "green",bg = "yellow")
        self.label4 = tk.Label(master1,text = "OR:",font = self.font2,fg = "green",bg = "yellow")
        self.label5 = tk.Label(master1,text = "206/204",font = self.font2,fg = "green",bg = "yellow")
        self.label6 = tk.Label(master1,text = "207/204",font = self.font2,fg = "green",bg = "yellow")
        self.label7 = tk.Label(master1,text = "208/204",font = self.font2,fg = "green",bg = "yellow")
        self.label8 = tk.Label(master1,text = "Age of lead-loss",font = self.font2,fg = "green",bg = "yellow")
        self.label9 = tk.Label(master1,text = "Ga",font = self.font2,fg = "green",bg = "yellow")
        self.label10 = tk.Label(master1,text = "Correlation of errors in 206Pb/238U and 207Pb/235U",font = self.font3,fg = "green",bg = "yellow")
        self.label11 = tk.Label(master1,text = "Using apparent error correlations from GLITTER output!",font = self.font4 ,fg = "green",bg = "yellow")
        self.label12 = tk.Label(master1,text = "Number of Monte-Carlo trials",font = self.font2,fg = "green",bg = "yellow")
        self.label13 = tk.Label(master1,text = "Sigma-level for discordance test (0, 1, 2....)",font = self.font2,fg = "green",bg = "yellow")

        self.montetrials = tk.IntVar()
        self.montetrials.set(globalval.monte_trials)
        self.labelmonte = tk.Label(master1,textvariable = self.montetrials,font = self.font2,fg = "green",bg = "yellow")
        self.ga = tk.DoubleVar()
        self.pb64 = tk.DoubleVar()
        self.pb74 = tk.DoubleVar()
        self.pb84 = tk.DoubleVar()
        self.ga.set(globalval.ga)
        self.pb64.set(globalval.pb64)
        self.pb74.set(globalval.pb74)
        self.pb84.set(globalval.pb84)
        self.leadlossage = tk.DoubleVar()
        self.leadlossage.set(globalval.leadlossage)
        self.const_err_coef = tk.DoubleVar()
        self.const_err_coef.set(0)
        self.obsev_err_coef = tk.DoubleVar()
        self.obsev_err_coef.set(0.9)
        self.text1 = tk.Entry(master1,width = 6,font=("Helvetica", 12),justify = "center",
                              textvariable = self.ga,state = "normal")
        self.ga.trace("w", self.update)

        self.text2 = tk.Entry(master1,width = 7,font=("Helvetica", 12),justify = "center",
                              textvariable = self.pb64,state = "disabled")
        self.text3 = tk.Entry(master1,width = 7,font=("Helvetica", 12),justify = "center",
                              textvariable = self.pb74,state = "disabled")
        self.text4 = tk.Entry(master1,width = 7,font=("Helvetica", 12),justify = "center",
                              textvariable = self.pb84,state = "disabled")
        self.text5 = tk.Entry(master1,width = 6,font=("Helvetica", 12),justify = "center",
                              textvariable = self.leadlossage)
        self.text6 = tk.Entry(master1,width = 5,font=("Helvetica", 15),justify = "center",
                              textvariable = self.const_err_coef)
        self.text6.delete(0,"end")
        self.text6.config(state = "disabled")
        self.text7 = tk.Entry(master1,width = 5,font=("Helvetica", 15),justify = "center",
                              textvariable = self.obsev_err_coef)
        self.sigma_discordance = tk.IntVar()
        self.sigma_discordance.set(2)
        self.text8 = tk.Entry(master1,width = 4,font=("Helvetica", 15),justify = "center",
                              textvariable = self.sigma_discordance)



        self.ok = tk.Button(master1,text = "OK",font = self.font1,bg = "green",fg = "yellow",width = 8,height = 1,command = self.from_ok)
        self.cancel = tk.Button(master1,text = "Cancel",font = self.font1,bg = "green",fg = "yellow",width=8,height=1,command = self.master1.quit)
        self.change = tk.Button(master1,text = "Change",font = self.font5,bg = "green",fg = "yellow",width=7,height=1,command = self.from_change)
        self.ifchange = False

        self.checkvar1 = tk.IntVar()
        self.checkvar2 = tk.IntVar()
        self.checkbox1 = tk.Checkbutton(master1,bg = "yellow",activebackground = "yellow",
                                        text = "Specify lead composition:",font = self.font2,fg = "green",
                                        variable = self.checkvar1,command = self.deselect1)
        self.checkbox2 = tk.Radiobutton(master1,bg = "yellow",activebackground = "yellow",
                                        text = "Constant error correlation\ncoefficient of:",
                                        justify = "left",font = self.font2,fg = "green",
                                        variable = self.checkvar2,value = 1,command = self.deselect2)
        self.checkbox3 = tk.Radiobutton(master1,bg = "yellow",activebackground = "yellow",
                                        text = "Use observed error correlations\nfrom worksheet, but use a constant\nvalue for blanks:",
                                        justify = "left",font = self.font2,fg = "green",
                                        variable = self.checkvar2, value = 0,command = self.deselect2)
        self.checkvar4 = tk.IntVar()
        self.checkvar5 = tk.IntVar()
        self.checkvar6 = tk.IntVar()

        self.checkbox4 = tk.Checkbutton(master1,bg = "yellow",activebackground = "yellow",
                                        text = "Use Discordance correction even when\nresult is inversely discordant",
                                        justify = "left",font = self.font2,fg = "green",
                                        variable = self.checkvar4,
                                        command = self.use_discordance)
        self.checkbox5 = tk.Checkbutton(master1,bg = "yellow",activebackground = "yellow",
                                        text = "Enable 207Pb correction",justify = "left",font = self.font2,fg = "green",
                                        variable = self.checkvar5,
                                        command = self.use_207_corr)
        self.checkbox6 = tk.Checkbutton(master1,bg = "yellow",activebackground = "yellow",
                                        text = "Enable 208Pb correction",justify = "left",font = self.font2,fg = "green",
                                        variable = self.checkvar6,
                                        command = self.use_208_corr)
        self.checkbox7 = tk.Checkbutton(master1,bg = "yellow",activebackground = "yellow",
                                        text = "Show Tera-Wasserburg style output (columns BF-BJ)",
                                        justify = "left",font = self.font2,fg = "green",)

        self.separator1 = ttk.Separator(master1,orient = "horizontal")
        self.separator2 = ttk.Separator(master1,orient = "horizontal")

        self.separator1.place(x = 0, rely = 0.47, relwidth = 2)
        self.separator1.lower()
        self.separator2.place(x = 0, rely = 0.67, relwidth = 2)

        self.label1.place(relx = 0.06, rely = 0.12)
        self.label2.place(relx = 0.06, rely = 0.17)
        self.label3.place(relx = 0.55, rely = 0.17)
        self.label4.place(relx = 0.1, rely = 0.23)
        self.label5.place(relx = 0.168, rely = 0.312)
        self.label6.place(relx = 0.368, rely = 0.312)
        self.label7.place(relx = 0.568, rely = 0.312)
        self.label8.place(relx = 0.1, rely = 0.4)
        self.label9.place(relx = 0.55, rely = 0.4)
        self.label10.place(relx = 0.5, rely = 0.455, anchor = "n")
        self.label11.place(relx = 0.1, rely = 0.555)
        self.label12.place(relx = 0.06, rely = 0.7)
        self.labelmonte.place(relx = 0.5, rely = 0.7)
        self.label13.place(relx = 0.06, rely = 0.815)

        self.text1.place(relx = 0.37, rely = 0.17)
        self.text2.place(relx = 0.15, rely = 0.345)
        self.text3.place(relx = 0.35, rely = 0.345)
        self.text4.place(relx = 0.55, rely = 0.345)
        self.text5.place(relx = 0.37, rely = 0.4)
        self.text6.place(relx = 0.7, rely = 0.5)
        self.text7.place(relx = 0.7, rely = 0.58)
        self.text8.place(relx = 0.64, rely = 0.81)

        self.ok.place(relx = 0.7, rely = 0.03)
        self.cancel.place(relx = 0.7, rely = 0.1)
        self.change.place(relx = 0.65, rely = 0.695)

        self.checkbox1.place(relx = 0.06, rely = 0.26)
        self.checkbox2.place(relx = 0.06, rely = 0.5)
        self.checkbox3.place(relx = 0.06, rely = 0.58)
        self.checkbox4.place(relx = 0.06, rely = 0.75)
        self.checkbox5.place(relx = 0.06, rely = 0.85)
        self.checkbox6.place(relx = 0.06, rely = 0.90)
        self.checkbox7.place(relx = 0.06, rely = 0.95)

    def from_change(self):
        self.ifchange = True
        top = tk.Toplevel()
        app = UserForm4(top,False,self.master1,self.montetrials)

    def from_ok(self):
        globalval.ga = self.ga.get()
        globalval.pb64 = self.pb64.get()
        globalval.pb74 = self.pb74.get()
        globalval.pb84 = self.pb84.get()
        globalval.leadlossage = self.leadlossage.get()
        if self.ifchange:
            self.master1.destroy()
            root = tk.Tk()
            app = UserForm2(root)
        else:
            top = tk.Toplevel()
            app = UserForm4(top,True,self.master1,self.montetrials)


    def update(self,*args):
        try:
            ga = self.ga.get()
        except:
            ga = 0
        self.pb64.set(18.7 - 9.74 * (math.exp(1.55125 * ga / 10) - 1))
        self.pb74.set(15.628 - 9.74 * (math.exp(9.8485 * ga / 10) - 1) / 137.88)
        self.pb84.set(38.63 - 36.84 * (math.exp(0.49475 * ga / 10) - 1))

    def deselect1(self):
        if self.checkvar1.get() == 1:
            self.text1.config(state = "disabled")
            self.text2.config(state = "normal")
            self.text3.config(state = "normal")
            self.text4.config(state = "normal")
        else:
            self.text1.config(state = "normal")
            self.text2.config(state = "disabled")
            self.text3.config(state = "disabled")
            self.text4.config(state = "disabled")

    def deselect2(self):
        if self.checkvar2.get() == 1:
            self.text6.config(state = "normal")
            self.const_err_coef.set(0.9)
            self.text7.delete(0,"end")
            self.text7.config(state = "disabled")
        else:
            self.text6.delete(0,"end")
            self.text6.config(state = "disabled")
            self.text7.config(state = "normal")
            self.obsev_err_coef.set(0.9)

    def use_discordance(self):
        if self.checkvar4.get() == 1:
            self.checkbox5.deselect()
            self.checkbox6.deselect()
            self.checkbox5.config(state = "disabled")
            self.checkbox6.config(state = "disabled")
        else:
            self.checkbox5.config(state = "normal")
            self.checkbox6.config(state = "normal")

    def use_207_corr(self):
        if self.checkvar5.get() == 1:
            self.checkbox4.config(state = "disabled")
            self.checkbox6.config(state = "disabled")
        else:
            self.checkbox4.config(state = "normal")
            self.checkbox6.config(state = "normal")

    def use_208_corr(self):
        if self.checkvar6.get() == 1:
            self.checkbox4.config(state = "disabled")
            self.checkbox5.config(state = "disabled")
        else:
            self.checkbox4.config(state = "normal")
            self.checkbox5.config(state = "normal")
