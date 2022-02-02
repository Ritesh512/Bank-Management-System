# Bank-Management-System
Bank Management  System in python using Tkinter.
Import all the libraries in the code.
Download mysql installer in your system 
link for mysql: https://dev.mysql.com/downloads/installer/
After mysql setup do the follwing step:
step 1: open mysql workbench and create a database 
        command : create database bank;
                  use bank;
        
step 2: create a table as bank_customer you can change the name accordingly.
        command : create table bank_customer(
       First_name Varchar(20) NOT NULL,
       Last_name varchar(20) NOT NULL ,
       Acc_no int NOT NULL,
       PWD int NOT NULL ,
       Amt int,
       constraint PK_BANK PRIMARY KEY(Acc_no));
       
step 3: Go into the code chnage the user and password with your's.


Happy Journey!!
