import os
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector 



class Signup:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+280+95")
        self.root.title("Store")

    def insert(self):
        fullname = self.txts_fullname.get()
        contact = self.txts_contact.get()
        email = self.txts_email.get()
        username = self.txts_username.get()
        password = self.txts_password.get()
        confrim = self.txts_confrim.get()

        if password != confrim:
            messagebox.showinfo("Insert Status", "Confrim password dosenot match to Password")
        elif fullname == "" or contact == "" or email == "" or username == "" or password == "" or confrim == "":
            messagebox.showinfo("Insert Status", "All Fields are required")
        else:
            con = mysql.connector.connect(host="localhost", user="root", password="root", database="DataSoftware")
            cursor = con.cursor()
            cursor.execute("insert into userSignup values('" + fullname + "','" + contact + "','" + email + "','" + username + "','" + password + "')")
            cursor.execute("commit")

            messagebox.showinfo("Insert Status", "Account created")
            con.close()

    def open_login(self):
        self.root.destroy()
        os.system('python Login.py')

    def signup(self):
        #frame
        main_Frame = Frame(self.root, bg="#ffffff")
        main_Frame.place(x=0, y=0, width=1366, height=768)

        left_Frame = Frame(self.root, bd=5, bg="#03D3C0")
        left_Frame.place(x=200, y=100, width=980, height=618)

        inner_Frame = Frame(left_Frame, bd=5, bg="#ffffff")
        inner_Frame.place(x=500, y=5, width=465, height=597)


        logo_img = Image.open("img/logo.png")
        logo_img = logo_img.resize((450, 380), Image.LANCZOS)
        self.logo_img = ImageTk.PhotoImage(logo_img)
        label_logo_img = Label(left_Frame, bg="#03D3C0", image=self.logo_img)
        label_logo_img.place(x=30, y=100, width=450, height=380)


        lbl_title=Label(self.root, text="RJN STORE",relief=GROOVE, font = ("times new romen",45,"bold"),bg="white",fg="#BA00EC")
        lbl_title.place(x=0,y=0,width=1366,height=50)

        #Signup label
        self.lbls_signup = Label(inner_Frame, text="SIGNUP", font=("arial", 18, "bold"), bg="white",fg="#03D3C0", bd=4)
        self.lbls_signup.place(x=195, y=5)


        #Full Name
        self.lbls_fullname = Label(inner_Frame, text="Full Name", font=("arial", 18, "bold"), bg="white",fg="#03D3C0", bd=4)
        self.lbls_fullname.place(x=10, y=80)

        self.txts_fullname = ttk.Entry(inner_Frame, font=("arial", 18), width=22) #foreground="#008D80"
        self.txts_fullname.place(x=150, y=80)

        #Contact
        self.lbls_contact = Label(inner_Frame, text="Contact", font=("arial", 18, "bold"), bg="white",fg="#03D3C0", bd=4)
        self.lbls_contact.place(x=10, y=140)

        self.txts_contact = ttk.Entry(inner_Frame, font=("arial", 18),  width=22)
        self.txts_contact.place(x=150, y=140)

        #Email
        self.lbls_email = Label(inner_Frame, text="Email", font=("arial", 18, "bold"), bg="white",fg="#03D3C0", bd=4)
        self.lbls_email.place(x=10, y=200)

        self.txts_email = ttk.Entry(inner_Frame, font=("arial", 18),  width=22)
        self.txts_email.place(x=150, y=200)

        #Username
        self.lbls_username = Label(inner_Frame, text="Username", font=("arial", 18, "bold"), bg="white",fg="#03D3C0", bd=4)
        self.lbls_username.place(x=10, y=260)

        self.txts_username = ttk.Entry(inner_Frame, font=("arial", 18),  width=22)
        self.txts_username.place(x=150, y=260)

        #Password
        self.lbls_password = Label(inner_Frame, text="Password", font=("arial", 18, "bold"), bg="white",fg="#03D3C0", bd=4)
        self.lbls_password.place(x=10, y=320)

        self.txts_password = ttk.Entry(inner_Frame, show="*", font=("arial", 18),  width=22)
        self.txts_password.place(x=150, y=320)

        #Confirm Password
        self.lbls_confrim = Label(inner_Frame, text="Confirm", font=("arial", 18, "bold"), bg="white",fg="#03D3C0", bd=4)
        self.lbls_confrim.place(x=10, y=380)

        self.txts_confrim = ttk.Entry(inner_Frame, show="*", font=("arial", 18),  width=22)
        self.txts_confrim.place(x=150, y=380)

        style = ttk.Style()
        style.configure("C.TButton", 
                background="#03D3C0",
                font=('Arial', 12),
                padding=10)

        #Signup Button
        self.btnsignup = ttk.Button(inner_Frame, text="Signup", style="C.TButton", command=self.insert, cursor="hand2", takefocus=False)
        self.btnsignup.place(x=180, y=450, width=130, height=44)


        #Login label
        self.lbls_account = Label(inner_Frame, text="Already have account?", font=("arial", 18, "bold"), bg="white",fg="#03D3C0", bd=4)
        self.lbls_account.place(x=30, y=535)

        #Login Button
        self.btnlogin = ttk.Button(inner_Frame, text="Login", command=self.open_login, style="C.TButton", cursor="hand2", takefocus=False)
        self.btnlogin.place(x=310, y=530, width=90, height=44)




if __name__ == "__main__":
    root = Tk()
    obj = Signup(root)
    obj.signup()
    root.mainloop()