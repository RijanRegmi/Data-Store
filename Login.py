import os
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector 



class Login:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+280+95")
        self.root.title("Store")

    def check_login(self):
        username = self.txts_username.get()
        password = self.txts_password.get()

        # Connect to MySQL database
        conn = mysql.connector.connect(host="localhost", user="root", password="root", database="DataSoftware")
        cursor = conn.cursor()

        # Execute SQL query to check if username and password match
        query = "SELECT * FROM userSignup WHERE username=%s AND password=%s"
        cursor.execute(query, (username, password))
        account = cursor.fetchone()

        if account:
            self.open_software()
            
        else:
            messagebox.showinfo("Login","Login Failed")
            self.login()


    def open_Signup(self):
        self.root.destroy()
        os.system('python Signup.py')

    def open_software(self):
        self.root.destroy()
        os.system('python software.py')

    def login(self):
        #frame
        main_Frame = Frame(self.root, bg="#ffffff")
        main_Frame.place(x=0, y=0, width=1366, height=768)

        left_Frame = Frame(self.root, bd=5, bg="#03D3C0")
        left_Frame.place(x=200, y=100, width=980, height=618)

        inner_Frame = Frame(left_Frame, bd=5, bg="#ffffff")
        inner_Frame.place(x=500, y=5, width=465, height=597)


        lbl_title=Label(self.root, text="RJN STORE",relief=GROOVE, font = ("times new romen",45,"bold"),bg="white",fg="#BA00EC")
        lbl_title.place(x=0,y=0,width=1366,height=50)

        #Login label
        self.lbls_login = Label(inner_Frame, text="LOGIN", font=("arial", 18, "bold"), bg="white",fg="#03D3C0", bd=4)
        self.lbls_login.place(x=195, y=5)


        #username
        self.lbls_username = Label(inner_Frame, text="Username", font=("arial", 18, "bold"), bg="white",fg="#03D3C0", bd=4)
        self.lbls_username.place(x=180, y=80)

        self.txts_username = ttk.Entry(inner_Frame, font=("arial", 18, "bold"), width=24)
        self.txts_username.place(x=80, y=120)

        #password
        self.lbls_password = Label(inner_Frame, text="Password", font=("arial", 18, "bold"), bg="white",fg="#03D3C0", bd=4)
        self.lbls_password.place(x=180, y=210)

        self.txts_password = ttk.Entry(inner_Frame, show="*", font=("arial", 18, "bold"), width=24)
        self.txts_password.place(x=80, y=250)

        style = ttk.Style()
        style.configure("C.TButton", 
                background="#03D3C0",
                font=('Arial', 12),
                padding=10)

        #Login Button
        self.btnlogin = ttk.Button(inner_Frame, text="Login", command=self.check_login, style="C.TButton", cursor="hand2", takefocus=False)
        self.btnlogin.place(x=180, y=350, width=130, height=44)


        #signin label
        self.lbls_login = Label(inner_Frame, text="Donot have account?", font=("arial", 18, "bold"), bg="white",fg="#03D3C0", bd=4)
        self.lbls_login.place(x=30, y=535)

        #Signup Button
        self.btnsignup = ttk.Button(inner_Frame, text="Signup", command=self.open_Signup, style="C.TButton", cursor="hand2", takefocus=False)
        self.btnsignup.place(x=290, y=530, width=90, height=44)




if __name__ == "__main__":
    root = Tk()
    obj = Login(root)
    obj.login()
    root.mainloop()