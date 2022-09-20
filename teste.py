import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        root.configure(background="grey")

        GButton_637=tk.Button(root)
        GButton_637["bg"] = "#5fb878"
        ft = tkFont.Font(family='Times',size=10)
        GButton_637["font"] = ft
        GButton_637["fg"] = "#ffffff"
        GButton_637["justify"] = "center"
        GButton_637["text"] = "BAIXAR"
        GButton_637.place(x=200,y=280,width=156,height=46)
        GButton_637["command"] = self.GButton_637_command

        GCheckBox_82=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_82["font"] = ft
        GCheckBox_82["fg"] = "#333333"
        GCheckBox_82["justify"] = "center"
        GCheckBox_82["text"] = "Música"
        GCheckBox_82.place(x=220,y=230,width=70,height=25)
        GCheckBox_82["offvalue"] = "0"
        GCheckBox_82["onvalue"] = "1"
        GCheckBox_82["command"] = self.GCheckBox_82_command

        GCheckBox_220=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_220["font"] = ft
        GCheckBox_220["fg"] = "#333333"
        GCheckBox_220["justify"] = "center"
        GCheckBox_220["text"] = "Vídeo"
        GCheckBox_220.place(x=290,y=230,width=70,height=25)
        GCheckBox_220["offvalue"] = "0"
        GCheckBox_220["onvalue"] = "1"
        GCheckBox_220["command"] = self.GCheckBox_220_command

        GLineEdit_753=tk.Entry(root)
        GLineEdit_753["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_753["font"] = ft
        GLineEdit_753["fg"] = "#333333"
        GLineEdit_753["justify"] = "center"
        GLineEdit_753["text"] = "url_youtube"
        GLineEdit_753["relief"] = "groove"
        GLineEdit_753.place(x=100,y=180,width=374,height=30)

    def GButton_637_command(self):
        print("command")


    def GCheckBox_82_command(self):
        print("command")


    def GCheckBox_220_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
