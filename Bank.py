import mysql.connector
from tkinter import *
from tkinter import messagebox as msg

def with_draw():
    global check
    mydb = mysql.connector.connect(user='root', passwd='#####',host='localhost',database='bank')
    mycursur = mydb.cursor()
    update_balance = int(check[0])-int(amt.get())
    if update_balance>=0:
        bal = "UPDATE Bank_customer set Amt=%d "%(update_balance)+"where Acc_no = %d"%(n1)
        mycursur.execute(bal)
        check = mycursur.fetchone()
        mydb.commit()
        msg.showinfo('Information','Balance Updated ')
        mydb.close()
        
def deposit():
    global check
    mydb = mysql.connector.connect(user='root', passwd='#####',host='localhost',database='bank')
    mycursur = mydb.cursor()
    update_balance = int(check[0])+int(amt.get())
    if update_balance>=0:
        bal = "UPDATE Bank_customer set Amt=%d "%(update_balance)+"where Acc_no = %d"%(n1)
        mycursur.execute(bal)
        check = mycursur.fetchone()
        mydb.commit()
        msg.showinfo('Information','Balance Updated ')
        mydb.close()
        

        


def customer_query():
    global cus_query
    global amt 
    cus_query =Toplevel(login)
    cus_query.geometry("3000x2500")
    cus_query.title("query")

    n1 = acc_no.get()
    Label(cus_query,text="Select your option",bg="blue",fg="white", width="200", height="3",font=("Calibri", 20)).pack()
    Label(cus_query,text="").pack()
    Display_acc = Label(cus_query,text="Account no:"+n1,fg="blue", width="200", height="3",font=("Calibri", 20))
    Display_acc.pack(side=TOP,anchor="w")

    Display_balance = Label(cus_query,text="Balance: "+str(check[0])+"  ",fg="blue", width="200", height="3",font=("Calibri", 20))
    Display_balance.pack(side=TOP ,anchor="w")

    Label(cus_query,text="").pack()
    Label(cus_query,text="").pack()


    Amt=IntVar()

    amt = Entry(cus_query,textvariable=Amt)
    amt.pack()
    Label(cus_query,text="").pack()
    Label(cus_query,text="").pack()


    Withdraw=Button(cus_query,text="Withdraw",bg="blue",fg="white",width="50", height="2",font=("Calibri", 15),command= with_draw)
    Withdraw.pack()
    
    Label(cus_query,text="").pack()

    Deposit=Button(cus_query,text="Deposit",bg="blue",fg="white",width="50", height="2",font=("Calibri", 15),command = deposit)
    Deposit.pack()
    Label(cus_query,text="").pack()

    exit = Button(cus_query,text="Exit",height="2",width="50",fg='white',bg='blue' ,font=("Calibri", 15),command=cus_query.destroy)
    exit.pack()


def check_login():
    mydb = mysql.connector.connect(user='root', passwd='#####',host='localhost',database='bank')
    mycursur = mydb.cursor()
    global n1
    
    
    n1 = int(acc_no.get())
    n2 = int(pwd.get())
    global check
    
    
    bal = "Select Amt from Bank_customer where Acc_no = %d and Pwd = %d"%(n1,n2)
    mycursur.execute(bal)
    check = mycursur.fetchone()

    if check is not None:
        customer_query()
    else:
        msg.showerror('Warning ','Invalid details')
        

        

    

def Login():
    global login
    global acc_no
    global pwd
    login = Toplevel(root)
    login.geometry("3000x2500")
    login.title("Login")

    Acc_no = StringVar()
    Pwd = IntVar()
    Label(login,text="Customer Login",bg="blue",fg="white", width="200", height="2", font=("Calibri", 13)).pack()
    Label(login,text="").pack()

    Label(login,text="Account No.",bg="blue",fg="white",width="50", height="2",font=("Calibri", 13)).pack()
    acc_no = Entry(login,textvariable=Acc_no)
    acc_no.pack()

    Label(login,text="").pack()
    Label(login,text="Password",bg="blue",fg="white",width="50", height="2",font=("Calibri", 13)).pack()
    pwd = Entry(login,textvariable=Pwd)
    pwd.pack()

    Label(login,text="").pack()
    
    login_btn = Button(login,text="Login",bg="blue",fg="white",width="20", height="2",font=("Calibri", 13),command=check_login)
    login_btn.pack()
    Label(login,text="").pack()
    Label(login,text="").pack()

    exit = Button(login,text="Exit",height="2",width="20",fg='white',bg='blue' ,font=("Calibri", 13),command=login.destroy)
    exit.pack()



def Save():
    global First_name
    global Last_name
    global Acc_no
    global pwd
    global amt

    mydb = mysql.connector.connect(user='root', passwd='#####',host='localhost',database='bank')
    mycursur = mydb.cursor()

    n1=First_name.get()
    n2 = Last_name.get()
    n3 = int(Acc_no.get())
    n4 = int(pwd.get())
    n5 = int(amt.get())

    ans = "insert into Bank_customer (First_Name,Last_name,Acc_no,Pwd,Amt) values ('%s','%s',%d,%d,%d)"%(n1,n2,n3,n4,n5)
    mycursur.execute(ans)
    mydb.commit()
    msg.showinfo('Information','Record Inserted ')
    First_name.delete(0,END)
    Last_name.delete(0,END)
    Acc_no.delete(0,END)
    pwd.delete(0,END)
    amt.delete(0,END)  

    mydb.close()


def Register():
    global register
    global First_name
    global Last_name
    global Acc_no
    global pwd
    global amt
    register = Toplevel(root)
    register.title("second window")
    register.geometry("3000x2500")

    F_name = StringVar()
    L_name = StringVar()
    acc_no = IntVar()
    Pwd = IntVar()
    amt= IntVar()

    Label(register,text="Register your details ",fg="white",bg="blue", width="300", height="2", font=("Calibri", 20)).pack()
    Label(register,text="").pack()


    
    Label(register,text="First_name",fg="blue", width="10", height="2", font=("Calibri", 20)).pack()
    First_name = Entry(register,textvariable=F_name,width=25)
    First_name.pack()
    
    label=Label(root,text=" ").pack()


    
    Label(register,text="Last_name",fg="blue", width="10", height="2", font=("Calibri", 20)).pack()
    Last_name = Entry(register,textvariable=L_name,width=25)
    Last_name.pack()
    
    label=Label(root,text=" ").pack()

    
    Label(register,text="Account_no",fg="blue", width="10", height="2", font=("Calibri", 20)).pack()
    Acc_no = Entry(register,textvariable=acc_no,width=25)
    Acc_no.pack()
    
    label=Label(root,text=" ").pack()

    
    Label(register,text="Password",fg="blue", width="20", height="2", font=("Calibri", 20)).pack()
    pwd = Entry(register,textvariable=Pwd,width=25)
    pwd.pack()
    
    label=Label(root,text=" ").pack()

    
    Label(register,text="Amount",fg="blue", width="10", height="2", font=("Calibri", 20)).pack()
    amt= Entry(register,textvariable=amt,width=25)
    amt.pack()
    
    label=Label(register,text=" ").pack()

    

    save=Button(register,text="SAVE",height=1,width=15,fg="white",bg="blue",font=("Calibri", 15),command=Save)
    save.pack()
    label=Label(register,text=" ").pack()
    
    

    exit=Button(register,text="EXIT",height=1,width=15,fg="white",bg="blue",font=("Calibri", 15),command=register.destroy)
    exit.pack()




def main():
    global root
    
    root=Tk()
    root.title("main screen")
    root.geometry("3000x2500")


    Label(root,text="Welcome to bank",fg="white",bg="blue", width="300", height="2", font=("Calibri",20)).pack()
    Label(root,text="").pack()
   
    label=Label(root,text=" ").pack()
    register = Button(root,text="Register",height=3,width=20,fg='white',bg='blue' ,font=("Arial Bold",20),command= Register)
    register.pack()
    label=Label(root,text=" ").pack()

    login = Button(root,text="login",height=3,width=20,fg='white',bg='blue' ,font=("Arial Bold", 20),command=Login)
    login.pack()
    label=Label(root,text=" ").pack()

    exit = Button(root,text="Exit",height=3,width=20,fg='white',bg='blue' ,font=("Arial Bold", 20),command=root.destroy)
    exit.pack()
    root.mainloop()

if __name__ =='__main__':
   main()
