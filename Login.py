from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox


class login:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+280+95")
        self.root.title("Store")

    def window(self):
        #frame
        main_Frame = Frame(self.root, bg="#ffffff")
        main_Frame.place(x=0, y=0, width=1366, height=768)

        left_Frame = Frame(self.root, bd=5, bg="#03D3C0")
        left_Frame.place(x=200, y=100, width=980, height=618)

        inner_Frame = Frame(left_Frame, bd=5, bg="#ffffff")
        inner_Frame.place(x=500, y=5, width=465, height=597)


        lbl_title=Label(self.root, text="RJN STORE",relief=GROOVE, font = ("times new romen",45,"bold"),bg="white",fg="#BA00EC")
        lbl_title.place(x=0,y=0,width=1366,height=50)


        #username
        self.lbls_name = Label(inner_Frame, text="Username", font=("arial", 18, "bold"), bg="white",fg="#03D3C0", bd=4)
        self.lbls_name.place(x=180, y=80)

        self.txts_name = ttk.Entry(inner_Frame, font=("arial", 18, "bold"), width=24)
        self.txts_name.place(x=80, y=120)

        #username
        self.lbls_name = Label(inner_Frame, text="Password", font=("arial", 18, "bold"), bg="white",fg="#03D3C0", bd=4)
        self.lbls_name.place(x=180, y=210)

        self.txts_name = ttk.Entry(inner_Frame, font=("arial", 18, "bold"), width=24)
        self.txts_name.place(x=80, y=250)



if __name__ == "__main__":
    root = Tk()
    obj = login(root)
    obj.window()
    root.mainloop()