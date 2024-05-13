from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import ctypes
import os
import mysql.connector 


class store:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+280+95")
        self.root.title("Store")



    # Front Page
    def window(self):
        #frame
        main_Frame = Frame(self.root, bg="#9FA8B2")
        main_Frame.place(x=0, y=0, width=1366, height=768)

        left_Frame = Frame(self.root, bd=5, bg="#03D3C0")
        left_Frame.place(x=0, y=50, width=180, height=768)

        # top_Frame = Frame(self.root, bd=5, bg="#03D3C0")
        # top_Frame.place(x=180, y=0, width=1186, height=150)


        lbl_title=Label(self.root, text="RJN STORE",relief=GROOVE, font = ("times new romen",45,"bold"),bg="white",fg="#BA00EC")
        lbl_title.place(x=0,y=0,width=1366,height=50)

        style = ttk.Style()
        style.configure("Custom.TButton", background="white", foreground="red", padding=8)

        self.btndata = ttk.Button(left_Frame, text="Data", command=self.data, style="Custom.TButton", width=130, cursor="hand2")
        self.btndata.place(x=20, y=200, width=130, height=44)
        self.data()


    def data(self):
        data_Frame = Frame(self.root, bd=5, bg="white")
        data_Frame.place(x=180, y=50, width=1186, height=718)



        # search
        Search_Frame = Frame(data_Frame, bd=2, bg="white")
        Search_Frame.place(x=290, y=96, width=645, height=47)

        self.lblproduct = Label(Search_Frame, text="Product", font=("arial", 13, "bold"), bg="#4f5c8b", fg="#FFFFFF")
        self.lblproduct.place(x=0,y=0,width=140,height=40)

        self.txt_Search = ttk.Entry(Search_Frame, font=('arial', 13, 'bold'), width=12)
        self.txt_Search.place(x=145,y=3,width=450,height=35)

        searchimg = Image.open("img/search.png")
        searchimg = searchimg.resize((45, 45))
        self.photosearchimg = ImageTk.PhotoImage(searchimg)

        btn_search = Button(Search_Frame, image=self.photosearchimg, bg="white", bd=0, cursor="hand2")
        btn_search.place(x=597, y=0, width=45, height=45)



        # ==========================Info Frame===========================
        info_Frame = Frame(data_Frame, bd=5, relief=GROOVE, bg="#9FA8B2")
        info_Frame.place(x=200, y=150, width=950, height=535)

        scroll_x = ttk.Scrollbar(info_Frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(info_Frame, orient=VERTICAL)
        self.info_table = ttk.Treeview(info_Frame, columns=("date", "product", "name", "status", "qty", "amount"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.info_table.heading("date", text="Date")
        self.info_table.heading("product", text="Product")
        self.info_table.heading("name", text="Name")
        self.info_table.heading("status", text="Status")
        self.info_table.heading("qty", text="QTY")
        self.info_table.heading("amount", text="Amount")

        self.info_table["show"] = "headings"

        self.info_table.pack(fill=BOTH, expand=1)

        self.info_table.column("date", width=30)
        self.info_table.column("product", width=30)
        self.info_table.column("name", width=30)
        self.info_table.column("status", width=30)
        self.info_table.column("qty", width=30)
        self.info_table.column("amount", width=30)

        self.info_table.pack(fill=BOTH, expand=1)
        self.info_table.bind("<ButtonRelease-1>")



    


        






if __name__ == "__main__":
    root = Tk()
    obj = store(root)
    obj.window()
    root.mainloop()

