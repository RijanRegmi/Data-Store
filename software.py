from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import ctypes
import os
import mysql.connector 
from tkcalendar import DateEntry


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

        

        # btn_data = Button(left_Frame, text="Data", bg="white",  cursor="hand2")
        # btn_data.place(x=10, y=0, width=125, height=35)

        style = ttk.Style()
        style.map("C.TButton",
        foreground=[('pressed', 'red'), ('active', 'blue')],
        background=[('pressed', '!disabled', 'black'), ('active', 'white')]
        )

        # style = ttk.Style()
        # style.configure("BW.TLabel", background="white", foreground="red", padding=0)

        self.btndata = ttk.Button(left_Frame, text="Data", style="C.TButton",  command=self.data, cursor="hand2")
        self.btndata.place(x=20, y=200, width=130, height=44)

        dataimg = Image.open("img/data.png")
        dataimg = dataimg.resize((40, 35))
        self.photodataimg = ImageTk.PhotoImage(dataimg)

        dataimg = Label(self.btndata, image=self.photodataimg, bg="white")
        dataimg.place(x=5, y=5, width=40, height=35)
        self.data()



    def data(self):
        data_Frame = Frame(self.root, bd=5, bg="white")
        data_Frame.place(x=180, y=50, width=1186, height=718)

        # Data Entry Label Frame
        data_entry_Frame=LabelFrame(data_Frame,text="Data Entry",font = ("times new romen",12,"bold"),bg="white",fg="#BA00EC")
        data_entry_Frame.place(x=40,y=0,width=1100,height=90)


        #date
        self.lbldate = Label(data_entry_Frame, text="date", font=("arial", 12, "bold"), bg="white",fg="black", bd=4)
        self.lbldate.place(x=45, y=0)

        self.txtdate = DateEntry(data_entry_Frame, width=14, background='darkblue', foreground='white', borderwidth=2)
        self.txtdate.place(x=20, y=30)

        #symbol
        self.lblproduct = Label(data_entry_Frame, text="Product Name", font=("arial", 12, "bold"), bg="white",fg="black", bd=4)
        self.lblproduct.place(x=190, y=0)

        self.txtproduct = ttk.Entry(data_entry_Frame, font=("arial", 12, "bold"), width=20)
        self.txtproduct.place(x=160, y=30)

        #firstname
        self.lbls_name = Label(data_entry_Frame, text="Category", font=("arial", 12, "bold"), bg="white",fg="black", bd=4)
        self.lbls_name.place(x=450, y=0)

        self.txts_name = ttk.Entry(data_entry_Frame, font=("arial", 12, "bold"), width=24)
        self.txts_name.place(x=380, y=30)

        #status
        self.lblstatus = Label(data_entry_Frame, text="Status", font=("arial", 12, "bold"), bg="white",fg="black", bd=4)
        self.lblstatus.place(x=655, y=0)

        self.Combo_status=ttk.Combobox(data_entry_Frame, font = ("arial",12,"bold"),width=8,state="readonly")
        # self.Combo_status.current(0)
        self.Combo_status.place(x=640, y=30)

        #qty
        self.lblqty = Label(data_entry_Frame, text="QTY", font=("arial", 12, "bold"), bg="white",fg="black", bd=4)
        self.lblqty.place(x=795, y=0)

        self.txtqty = ttk.Entry(data_entry_Frame, font=("arial", 12, "bold"), width=10)
        self.txtqty.place(x=770, y=30)


        #amount
        self.lblamount = Label(data_entry_Frame, text="Amount", font=("arial", 12, "bold"), bg="white",fg="black", bd=4)
        self.lblamount.place(x=950, y=0)

        self.txtamount = ttk.Entry(data_entry_Frame, font=("arial", 12, "bold"), width=18)
        self.txtamount.place(x=900, y=30)



        # search
        Search_Frame = Frame(data_Frame, bd=2, bg="white")
        Search_Frame.place(x=290, y=96, width=645, height=47)

        self.lblproduct = Label(Search_Frame, text="Product", font=("arial", 13, "bold"), bg="#00C666", fg="#FFFFFF")
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
        self.info_table = ttk.Treeview(info_Frame, columns=("date", "product", "category", "status", "qty", "amount"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.info_table.heading("date", text="Date")
        self.info_table.heading("product", text="Product Name")
        self.info_table.heading("category", text="Category")
        self.info_table.heading("status", text="Status")
        self.info_table.heading("qty", text="QTY")
        self.info_table.heading("amount", text="Amount")

        self.info_table["show"] = "headings"

        self.info_table.pack(fill=BOTH, expand=1)

        self.info_table.column("date", width=30)
        self.info_table.column("product", width=30)
        self.info_table.column("category", width=30)
        self.info_table.column("status", width=30)
        self.info_table.column("qty", width=30)
        self.info_table.column("amount", width=30)

        self.info_table.pack(fill=BOTH, expand=1)
        self.info_table.bind("<ButtonRelease-1>")


        # Button Label Frame
        btn_Frame=LabelFrame(data_Frame,text="Data Manage",font = ("times new romen",12,"bold"),bg="white",fg="#BA00EC")
        btn_Frame.place(x=10,y=200,width=180,height=420)


        # button
        self.btnsavedata = Button(btn_Frame, text="Save", height=1, font=('arial', 15, 'bold'), bg="#00C666", fg="#FFFFFF",
                              width=10, cursor="hand2")
        self.btnsavedata.place(x=20, y=20)

        self.btncleardata = Button(btn_Frame, text="Clear", height=1, font=('arial', 15, 'bold'),
                               bg="#00C666", fg="#FFFFFF", width=10, cursor="hand2")
        self.btncleardata.place(x=20, y=120)

        self.btnupdate = Button(btn_Frame, text="Update", height=1, font=('arial', 15, 'bold'),
                               bg="#00C666", fg="#FFFFFF", width=10, cursor="hand2")
        self.btnupdate.place(x=20, y=220)

        self.btndelete = Button(btn_Frame, text="Delete", height=1, font=('arial', 15, 'bold'),
                               bg="#00C666", fg="#FFFFFF", width=10, cursor="hand2")
        self.btndelete.place(x=20, y=320)



    


        






if __name__ == "__main__":
    root = Tk()
    obj = store(root)
    obj.window()
    root.mainloop()

