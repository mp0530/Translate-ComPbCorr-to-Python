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

class UserForm3:
    def __init__(self,master):
        self.UserForm3 = master #create the windows
        self.UserForm3.config(bg = "yellow")
        self.UserForm3.geometry("500x800")

        self.font1 = Font(size = 9, weight = "bold")
        self.font2 = Font(size = 9, weight = "bold",slant = "italic")
        self.font3 = Font(size = 9)
        self.font4 = Font(size = 11, weight = "bold")

        self.ok = tk.Button(self.UserForm3,text = "OK",font = self.font4,bg = "green",fg = "yellow",width = 8,height = 1,command = self.ok)
        self.cancel = tk.Button(self.UserForm3,text = "Cancel",font = self.font4,bg = "green",fg = "yellow",width=8,height=1,command = self.UserForm3.quit)

        self.label1 = tk.Label(self.UserForm3,text = "Instrumental discrimination of U and Th",font = self.font1,fg = "green",bg = "yellow")
        self.label2 = tk.Label(self.UserForm3,text = "Factor",font = self.font1,fg = "green",bg = "yellow")
        self.label3 = tk.Label(self.UserForm3,text = "±",font = self.font1,fg = "green",bg = "yellow")
        self.label4 = tk.Label(self.UserForm3,text = "(1 σ)",font = self.font1,fg = "green",bg = "yellow")
        self.label5 = tk.Label(self.UserForm3,text = "Plague vs. Cholera - please make your choice !",font = self.font2,fg = "green",bg = "yellow")
        self.label6 = tk.Label(self.UserForm3,text = "U-Pb errors are highly correlated, but GLITTER in\n\
        principle treats them as uncorrelated. This causes\n\
        problems for calculation of corrected 207Pb/206Pb\n\
        ratios and ages, and becomes very prominet when\n\
        trying to plot TW concordias from TW style output.\n\
        These routines do not solve the problem, but have\n\
        been designed to create consistent output.",font = self.font3,fg = "green",bg = "yellow",justify = "left")
        self.label7 = tk.Label(self.UserForm3,text = "\n\
        GLITTER commonly reports apparent (spurious) error.\n\
        Choosing this option will allow you to specify a constant\n\
        error correlation coefficient. Error propogation of\n\
        corrected data will be done accordingly, and errors on\n\
        corrected ratios are internally consistent. But the error on\n\
        corrected 207Pb/206Pb ratios will appear smaller than on\n\
        the raw ratios!",font = self.font3,fg = "green",bg = "yellow",justify = "left")
        self.var_chk1 = tk.IntVar()
        self.var_chk2 = tk.IntVar()
        self.checkbox1 = tk.Radiobutton(self.UserForm3,text = "No correction",bg = "yellow",
                                        activebackground = "yellow",font = self.font1,fg = "green",
                                        variable = self.var_chk1, value = 0)
        self.checkbox2 = tk.Radiobutton(self.UserForm3,text = "Use empirical correction factor",bg = "yellow",
                                        activebackground = "yellow",font = self.font1,fg = "green",
                                        variable = self.var_chk1, value = 1)
        self.checkbox3 = tk.Radiobutton(self.UserForm3,text = "Use apparent error correlations from GLITTER",
                                        bg = "yellow",activebackground = "yellow",font = self.font3,fg = "green",
                                        variable = self.var_chk2, value = 1)
        self.checkbox4 = tk.Radiobutton(self.UserForm3,text = "Ignore apparent error correlations from GLITTER",
                                        bg = "yellow",activebackground = "yellow",font = self.font3,fg = "green",
                                        justify = "left",
                                        variable = self.var_chk2, value = 0)

        self.text1 = tk.Entry(self.UserForm3, width = 5, font=("Helvetica", 18))
        self.text2 = tk.Entry(self.UserForm3, width = 5, font=("Helvetica", 18))

        self.separator1 = ttk.Separator(self.UserForm3,orient = "horizontal")
        self.separator2 = ttk.Separator(self.UserForm3,orient = "horizontal")

        self.label1.place(relx = 0.05, rely = 0.02, anchor = "nw")
        self.checkbox1.place(relx = 0.2, rely = 0.08, anchor = "nw")
        self.checkbox2.place(relx = 0.2, rely = 0.13, anchor = "nw")
        self.label2.place(relx = 0.1, rely = 0.22, anchor = "w")
        self.text1.place(relx = 0.35, rely = 0.22, anchor = "center")
        self.label3.place(relx = 0.5, rely = 0.22, anchor = "center")
        self.text2.place(relx = 0.65, rely = 0.22, anchor = "center")
        self.label4.place(relx = 0.8, rely = 0.22, anchor = "w")
        self.separator1.place(rely = 0.3, relwidth = 2, anchor = "center")
        self.separator1.lower()
        self.label5.place(relx = 0.5, rely = 0.3, anchor = "center")
        self.label6.place(relx = 0.5, rely = 0.335, anchor = "n")
        self.checkbox3.place(relx = 0.1, rely = 0.54, anchor = "nw")
        self.checkbox4.place(relx = 0.1, rely = 0.59, anchor = "nw")
        self.separator2.place(rely = 0.65, relwidth = 2)
        self.label7.place(relx = 0.5, rely = 0.65, anchor = "n")
        self.ok.place(relx = 0.35, rely = 0.93, anchor = "center")
        self.cancel.place(relx = 0.65, rely = 0.93, anchor = "center")
        # self.UserForm3.mainloop()
    def ok(self):
        self.UserForm3.destroy()
        root = tk.Tk()
        app = UserForm1(root)

class UserForm1:
    def __init__(self,master):
        self.UserForm1 = master
        self.UserForm1.config(bg = "yellow")
        self.font1 = Font(size = 12, slant = "italic", weight = "bold")
        self.font2 = Font(size = 8, weight = "bold")
        self.font3 = Font(size = 9, weight = "bold",slant = "italic")
        self.font4 = Font(size = 7)
        self.font5 = Font(size = 8, slant = "italic", weight = "bold")
        self.font6 = Font(size = 15)
        # Title
        self.UserForm1.title("UserForm1")
        # Size
        self.UserForm1.geometry("600x900")
        self.UserForm1.minsize(width=400,height=600)
        self.label1 = tk.Label(self.UserForm1,text = "Composition of common-lead:", font = self.font3, fg = "#008000", bg = "yellow")
        self.label2 = tk.Label(self.UserForm1,text = "Stacey - Kramers at",font = self.font2,fg = "green",bg = "yellow")
        self.label3 = tk.Label(self.UserForm1,text = "Ga",font = self.font2,fg = "green",bg = "yellow")
        self.label4 = tk.Label(self.UserForm1,text = "OR:",font = self.font2,fg = "green",bg = "yellow")
        self.label5 = tk.Label(self.UserForm1,text = "206/204",font = self.font2,fg = "green",bg = "yellow")
        self.label6 = tk.Label(self.UserForm1,text = "207/204",font = self.font2,fg = "green",bg = "yellow")
        self.label7 = tk.Label(self.UserForm1,text = "208/204",font = self.font2,fg = "green",bg = "yellow")
        self.label8 = tk.Label(self.UserForm1,text = "Age of lead-loss",font = self.font2,fg = "green",bg = "yellow")
        self.label9 = tk.Label(self.UserForm1,text = "Ga",font = self.font2,fg = "green",bg = "yellow")
        self.label10 = tk.Label(self.UserForm1,text = "Correlation of errors in 206Pb/238U and 207Pb/235U",font = self.font3,fg = "green",bg = "yellow")
        self.label11 = tk.Label(self.UserForm1,text = "Using apparent error correlations from GLITTER output!",font = self.font4 ,fg = "green",bg = "yellow")
        self.label12 = tk.Label(self.UserForm1,text = "Number of Monte-Carlo trials",font = self.font2,fg = "green",bg = "yellow")
        self.label13 = tk.Label(self.UserForm1,text = "Sigma-level for discordance test (0, 1, 2....)",font = self.font2,fg = "green",bg = "yellow")

        self.text1 = tk.Entry(self.UserForm1,width = 6)
        self.text2 = tk.Entry(self.UserForm1,width = 7,font=("Helvetica", 12))
        self.text3 = tk.Entry(self.UserForm1,width = 7,font=("Helvetica", 12))
        self.text4 = tk.Entry(self.UserForm1,width = 7,font=("Helvetica", 12))
        self.text5 = tk.Entry(self.UserForm1,width = 6)
        self.text6 = tk.Entry(self.UserForm1,width = 5,font=("Helvetica", 15))
        self.text7 = tk.Entry(self.UserForm1,width = 5,font=("Helvetica", 15))
        self.text8 = tk.Entry(self.UserForm1,width = 4,font=("Helvetica", 15))



        self.ok = tk.Button(self.UserForm1,text = "OK",font = self.font1,bg = "green",fg = "yellow",width = 8,height = 1,command = self.from_ok)
        self.cancel = tk.Button(self.UserForm1,text = "Cancel",font = self.font1,bg = "green",fg = "yellow",width=8,height=1,command = self.UserForm1.quit)
        self.change = tk.Button(self.UserForm1,text = "Change",font = self.font5,bg = "green",fg = "yellow",width=7,height=1,command = self.from_change)

        self.checkbox1 = tk.Checkbutton(self.UserForm1,bg = "yellow",activebackground = "yellow",text = "Specify lead composition:",font = self.font2,fg = "green")
        self.checkbox2 = tk.Checkbutton(self.UserForm1,bg = "yellow",activebackground = "yellow",text = "Constant error correlation\ncoefficient of:",justify = "left",font = self.font2,fg = "green")
        self.checkbox3 = tk.Checkbutton(self.UserForm1,bg = "yellow",activebackground = "yellow",text = "Use observed error correlations\nfrom worksheet, but use a constant\nvalue for blanks:",justify = "left",font = self.font2,fg = "green")
        self.checkbox4 = tk.Checkbutton(self.UserForm1,bg = "yellow",activebackground = "yellow",text = "Use Discordance correction even when\nresult is inversely discordant",justify = "left",font = self.font2,fg = "green")
        self.checkbox5 = tk.Checkbutton(self.UserForm1,bg = "yellow",activebackground = "yellow",text = "Enable 207Pb correction",justify = "left",font = self.font2,fg = "green")
        self.checkbox6 = tk.Checkbutton(self.UserForm1,bg = "yellow",activebackground = "yellow",text = "Enable 208Pb correction",justify = "left",font = self.font2,fg = "green")
        self.checkbox7 = tk.Checkbutton(self.UserForm1,bg = "yellow",activebackground = "yellow",text = "Show Tera-Wasserburg style output (columns BF-BJ)",justify = "left",font = self.font2,fg = "green")

        self.separator1 = ttk.Separator(self.UserForm1,orient = "horizontal")
        self.separator2 = ttk.Separator(self.UserForm1,orient = "horizontal")

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
        self.change.place(relx = 0.47, rely = 0.695)

        self.checkbox1.place(relx = 0.06, rely = 0.26)
        self.checkbox2.place(relx = 0.06, rely = 0.5)
        self.checkbox3.place(relx = 0.06, rely = 0.58)
        self.checkbox4.place(relx = 0.06, rely = 0.75)
        self.checkbox5.place(relx = 0.06, rely = 0.85)
        self.checkbox6.place(relx = 0.06, rely = 0.90)
        self.checkbox7.place(relx = 0.06, rely = 0.95)

    def from_change(self):
        root = tk.Tk()
        app = UserForm4(root,False,self.UserForm1)

    def from_ok(self):
        root = tk.Tk()
        app = UserForm4(root,True,self.UserForm1)
class UserForm4:
    # def __init__(self, master):
    def __init__(self,master,close,prevmaster):
        self.close = close
        self.prevmaster = prevmaster

        self.UserForm4 = master #create the windows
        self.UserForm4.title("Monte-Carlo error estimate")
        self.UserForm4.config(bg = "yellow")
        self.UserForm4.geometry("480x300")

        self.font1 = Font(size = 12, weight = "bold")

        self.ok = tk.Button(self.UserForm4,text = "OK",font = self.font1,bg = "green",fg = "yellow",width = 8,height = 1,command = self.monte)

        self.label1 = tk.Label(self.UserForm4,text = "Set number of trials to",font = self.font1,fg = "green",bg = "yellow")
        self.label2 = tk.Label(self.UserForm4,text = "n >(>) 100!",font = self.font1,fg = "green",bg = "yellow")

        self.text1 = tk.Text(self.UserForm4,width = 4,height = 1,font=("Helvetica", 18))

        self.label1.place(relx = 0.35, rely = 0.4, anchor = "center")
        self.text1.place(relx = 0.85, rely = 0.4, anchor = "e")
        self.label2.place(relx = 0.3, rely = 0.65, anchor = "center")
        self.ok.place(relx = 0.9, rely = 0.9, anchor = "se")
        # self.UserForm4.mainloop()

    def monte(self):
        self.UserForm4.destroy()
        if self.close:
            self.prevmaster.destroy()
            root = tk.Tk()
            app = UserForm2(root)
class UserForm2:
    def __init__(self,master):
        ga = 100
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
        self.label4 = tk.Label(self.UserForm2,text = ga, font = self.font2, fg = "black", bg = "yellow")
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
class Main:
    def __init__(self,sheet):
        self.execute(sheet)
    def execute(self,sheet):
        if sheet == "data":
            root = tk.Tk()
            app = UserForm1(root)
            root.mainloop()

        elif sheet == "input":
            root = tk.Tk()
            app = UserForm3(root)
            root.mainloop()

x = Main("input")
