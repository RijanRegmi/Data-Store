from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import ctypes
import os
import mysql.connector 
from tkcalendar import DateEntry
from datetime import datetime



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
        left_Frame.place(x=0, y=50, width=180, height=718)

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


        style = ttk.Style()
        style.configure("C.TButton", 
                background="#03D3C0",
                font=('Arial', 12),
                padding=10)

        self.btndata = ttk.Button(left_Frame, text="Data", takefocus=False,  style="C.TButton", command=self.data, cursor="hand2")
        self.btndata.place(x=20, y=200, width=130, height=44)

        dataimg = Image.open("img/data.png")
        dataimg = dataimg.resize((40, 35))
        self.photodataimg = ImageTk.PhotoImage(dataimg)

        dataimg = Label(self.btndata, image=self.photodataimg, bg="white")
        dataimg.place(x=5, y=5, width=40, height=35)
        self.data()
        self.fetch_data()



    def data(self):
        self.date = StringVar()
        self.ProductID = StringVar()
        self.product = StringVar()
        self.category = StringVar()
        self.status_data=StringVar()
        self.qty = IntVar()
        self.rate = DoubleVar()
        self.amount = DoubleVar()
        self.status=["Buy","Sell"]

        data_Frame = Frame(self.root, bd=5, bg="white")
        data_Frame.place(x=180, y=50, width=1186, height=718)

        # Data Entry Label Frame
        data_entry_Frame=LabelFrame(data_Frame,text="Data Entry",font = ("times new romen",12,"bold"),bg="#03D3C0",fg="#BA00EC")
        data_entry_Frame.place(x=40,y=0,width=1100,height=90)


        #date
        self.lbldate = Label(data_entry_Frame, text="date", font=("arial", 14, "bold"), bg="#03D3C0",fg="black", bd=4)
        self.lbldate.place(x=35, y=0)

        self.txtdate = DateEntry(data_entry_Frame, selectmode="day", cursor="hand2", state="readonly", font=("Arial", 14, "bold"), textvariable=self.date, date_pattern="yyyy-mm-dd")
        self.txtdate.place(x=10, y=30, width=140)

        #ProductID
        self.lblProductID = Label(data_entry_Frame, text="Product ID", font=("arial", 14, "bold"), bg="#03D3C0",fg="black", bd=4)
        self.lblProductID.place(x=155, y=0)

        self.txtProductID = ttk.Entry(data_entry_Frame, textvariable=self.ProductID, font=("arial", 14, "bold"), width=9)
        self.txtProductID.place(x=155, y=30)

        #product
        self.lblproduct = Label(data_entry_Frame, text="Product Name", font=("arial", 12, "bold"), bg="#03D3C0",fg="black", bd=4)
        self.lblproduct.place(x=350, y=0)

        self.txtproduct = ttk.Entry(data_entry_Frame, textvariable=self.product, font=("arial", 14), width=22)
        self.txtproduct.place(x=275, y=30)

        #Category
        self.lblscategory = Label(data_entry_Frame, text="Category", font=("arial", 12, "bold"), bg="#03D3C0",fg="black", bd=4)
        self.lblscategory.place(x=630, y=0)

        self.txtcategory = ttk.Entry(data_entry_Frame, textvariable=self.category, font=("arial", 14), width=22)
        self.txtcategory.place(x=535, y=30)

        #status
        self.lblstatus = Label(data_entry_Frame, text="Status", font=("arial", 12, "bold"), bg="#03D3C0",fg="black", bd=4)
        self.lblstatus.place(x=795, y=0)

        #status
        self.Combo_status = ttk.Combobox(data_entry_Frame, textvariable=self.status_data, value=self.status, font=("arial", 14), width=4, state="readonly")
        self.Combo_status.current(0)
        self.Combo_status.place(x=795, y=30)

        #qty
        self.lblqty = Label(data_entry_Frame, text="QTY", font=("arial", 12, "bold"), bg="#03D3C0",fg="black", bd=4)
        self.lblqty.place(x=885, y=0)

        self.txtqty = ttk.Entry(data_entry_Frame, textvariable=self.qty, font=("arial", 14), width=6)
        self.txtqty.place(x=875, y=30)


        #Rate
        self.lblrate = Label(data_entry_Frame, text="Rate", font=("arial", 12, "bold"), bg="#03D3C0",fg="black", bd=4)
        self.lblrate.place(x=990, y=0)

        self.txtrate = ttk.Entry(data_entry_Frame, textvariable=self.rate, font=("arial", 14, "bold"), width=10)
        self.txtrate.place(x=960, y=30)

        #amount the field is hidden
        self.txtamount = ttk.Entry(data_entry_Frame, textvariable=self.amount, font=("arial", 12, "bold"), width=18)
        self.txtamount.place(x=1200, y=30)



        # search
        Search_Frame = Frame(data_Frame, bd=2, bg="white")
        Search_Frame.place(x=290, y=96, width=745, height=47)

        self.lblsearchby_label = Label(Search_Frame, text="Search By", font=("arial", 13, "bold"), bg="#00C666", fg="#FFFFFF")
        self.lblsearchby_label.place(x=0,y=0,width=140,height=40)

        self.txt_Search = ttk.Entry(Search_Frame, font=('arial', 13, 'bold'), width=12)
        self.txt_Search.place(x=345,y=3,width=350,height=35)

        searchimg = Image.open("img/search.png")
        searchimg = searchimg.resize((45, 45))
        self.photosearchimg = ImageTk.PhotoImage(searchimg)

        btn_search = Button(Search_Frame, image=self.photosearchimg, bg="white", bd=0, cursor="hand2")
        btn_search.place(x=697, y=0, width=45, height=45)

        opts = ["Select", "Product ID", "Product", "Category"]
        self.searchby_commbo_box_var = StringVar()
        self.searchby_commbo_box = ttk.Combobox(Search_Frame, font=("Arial", 13, "bold"), state="readonly", cursor="hand2", values=opts, textvariable=self.searchby_commbo_box_var) 
        self.searchby_commbo_box.current(0)
        self.searchby_commbo_box.place(x=150, y=3,width=180, height=35)
        self.searchby_commbo_box.bind("<<ComboboxSelected>>")
        self.searchby_commbo_box.bind("<<ComboboxSelected>>", lambda event: self.search_data())
        btn_search.config(command=self.search_data)

        
        # ==========================Info Frame===========================
        info_Frame = Frame(data_Frame, bd=5, relief=GROOVE, bg="#9FA8B2")
        info_Frame.place(x=200, y=150, width=950, height=535)

        scroll_x = ttk.Scrollbar(info_Frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(info_Frame, orient=VERTICAL)
        self.info_table = ttk.Treeview(info_Frame, columns=("date", "productID", "product", "category", "status", "qty", "rate", "amount"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.info_table.heading("date", text="Date")
        self.info_table.heading("productID", text="Product ID")
        self.info_table.heading("product", text="Product Name")
        self.info_table.heading("category", text="Category")
        self.info_table.heading("status", text="Status")
        self.info_table.heading("qty", text="QTY")
        self.info_table.heading("rate", text="Rate")
        self.info_table.heading("amount", text="Amount")

        self.info_table["show"] = "headings"

        self.info_table.pack(fill=BOTH, expand=1)

        self.info_table.column("date", width=15)
        self.info_table.column("productID", width=20)
        self.info_table.column("product", width=100)
        self.info_table.column("category", width=100)
        self.info_table.column("status", width=20)
        self.info_table.column("qty", width=10)
        self.info_table.column("rate", width=35)
        self.info_table.column("amount", width=35)

        self.info_table.pack(fill=BOTH, expand=1)
        self.info_table.bind("<ButtonRelease-1>", self.get_cursor )
        self.fetch_data()


        # Button Label Frame
        btn_Frame=LabelFrame(data_Frame,text="Data Manage",font = ("times new romen",12,"bold"),bg="#03D3C0",fg="#BA00EC")
        btn_Frame.place(x=10,y=200,width=180,height=420)


        # button
        self.btnsavedata = Button(btn_Frame, text="Save", command= self.additem, height=1, font=('arial', 15, 'bold'), bg="#00C666", fg="#FFFFFF",
                              width=10, cursor="hand2")
        self.btnsavedata.place(x=20, y=20)

        self.btncleardata = Button(btn_Frame, text="Clear", command=self.cleardata, height=1, font=('arial', 15, 'bold'),
                               bg="#00C666", fg="#FFFFFF", width=10, cursor="hand2")
        self.btncleardata.place(x=20, y=120)

        self.btnupdate = Button(btn_Frame, text="Update", command=self.update, height=1, font=('arial', 15, 'bold'),
                               bg="#00C666", fg="#FFFFFF", width=10, cursor="hand2")
        self.btnupdate.place(x=20, y=220)

        self.btndelete = Button(btn_Frame, text="Delete", command=self.delete, height=1, font=('arial', 15, 'bold'),
                               bg="#00C666", fg="#FFFFFF", width=10, cursor="hand2")
        self.btndelete.place(x=20, y=320)
        self.fetch_data()


    def get_cursor(self,event=""):
        cursor_row=self.info_table.focus()
        content=self.info_table.item(cursor_row)
        row=content["values"]
        self.date.set(row[0])
        self.ProductID.set(row[1])
        self.product.set(row[2])
        self.category.set(row[3])
        self.status_data.set(row[4])
        self.qty.set(row[5])
        self.rate.set(row[6])
        self.amount.set(row[7])


    def additem(self):
        date = self.txtdate.get()
        productID = self.txtProductID.get()
        product = self.txtproduct.get()
        category = self.txtcategory.get()
        status = self.Combo_status.get()
        qty = self.txtqty.get()
        rate = self.txtrate.get()

        try:
            qty = float(qty)
            rate = float(rate)
            amount = qty * rate
        except ValueError as e:
            messagebox.showerror("Input Error", f"Error: {e}")
            return

        if date == "" or productID == "" or product == "" or category == "" or status == "" or qty == "" or rate == "":
            messagebox.showinfo("Insert Status", "All Fields are required")
        else:
            con = mysql.connector.connect(host="localhost", user="root", password="root", database="DataSoftware")
            cursor = con.cursor()
            cursor.execute("insert into item (date, productID, product, category, status, qty, rate, amount) values (%s, %s, %s, %s, %s, %s, %s, %s)", 
                        (date, productID, product, category, status, qty, rate, amount))
            con.commit()

            messagebox.showinfo("Insert Status", "Data stored")
            con.close()
            self.fetch_data()



    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="root", database="DataSoftware")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM item")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            if self.info_table is not None:
                self.info_table.delete(*self.info_table.get_children())
                for i in rows:
                    self.info_table.insert("", END, value=i)
                conn.commit()
        conn.close()

    def delete(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="root", database="DataSoftware")
        my_cursor = conn.cursor()
        query="delete from item where productID=%s"
        value=(self.ProductID.get(),)
        my_cursor.execute(query,value)
        conn.commit()
        conn.close()
        self.fetch_data()
        messagebox.showinfo("Delete","Deleted successfully")  

    def cleardata(self):
        op=messagebox.askyesno("Clear Share","Do you want to Clear all?")
        if op>0:
            self.date.set("")
            self.ProductID.set("")
            self.product.set("")
            self.category.set("")
            self.status_data.set("")
            self.qty.set("")
            self.rate.set("")
            self.amount.set("")

    def update(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="root", database="DataSoftware")
        my_cursor = conn.cursor()
        my_cursor.execute(
                "UPDATE item SET date=%s, product=%s, category=%s, status=%s, qty=%s, rate=%s, amount=%s WHERE productID=%s",
                (self.date.get(), self.product.get(), self.category.get(), self.status_data.get(), self.qty.get(), self.rate.get(), self.amount.get(), self.ProductID.get())
            )
        conn.commit()
        messagebox.showinfo("Updated","Updated Succesfully!")
        my_cursor.close()
        conn.close()
        self.fetch_data()

    def search_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="root", database="DataSoftware")
        my_cursor = conn.cursor()
        
        search_by = self.searchby_commbo_box_var.get()
        search_value = self.txt_Search.get()

        # Modify the query based on the search filter
        if search_by == "Product ID":
            query = "SELECT * FROM item WHERE productID LIKE %s"
            value = ("%" + search_value + "%",)
        elif search_by == "Product":
            query = "SELECT * FROM item WHERE product LIKE %s"
            value = ("%" + search_value + "%",)
        elif search_by == "Category":
            query = "SELECT * FROM item WHERE category LIKE %s"
            value = ("%" + search_value + "%",)
        else:
            query = "SELECT * FROM item"
            value = ()

        my_cursor.execute(query, value)
        rows = my_cursor.fetchall()

        if len(rows) != 0:
            self.info_table.delete(*self.info_table.get_children())
            for row in rows:
                self.info_table.insert("", END, values=row)
            conn.commit()
        conn.close()



    



if __name__ == "__main__":
    root = Tk()
    obj = store(root)
    obj.window()
    root.mainloop()

