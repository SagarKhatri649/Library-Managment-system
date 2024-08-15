
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import mysql.connector
from tkinter import messagebox
import datetime
import tkinter


class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1550x800+0+0")

        # Variables
        self.member_var= StringVar()
        self.prn_no_var = StringVar()
        self.id_var = StringVar()
        self.firstname_var = StringVar()
        self.lastname_var = StringVar()
        self.address_var = StringVar()
        self.postcode_var = StringVar()
        self.mobile_var = StringVar()
        self.bookid_var = StringVar()
        self.booktitle_var = StringVar()
        self.dateborrowed_var = StringVar()
        self.datedue_var = StringVar()
        self.daysonbook_var = StringVar()
        self.latereturnfine_var = StringVar()
        self.dateoverdue_var = StringVar()
        self.finalprice_var = StringVar() 

        # Title
        lbtitle = Label(self.root, text="LIBRARY MANAGEMENT SYSTEM", bg="slategrey", fg="black", bd=20, relief=RIDGE, # type: ignore
                        font=("times new roman", 50, "bold"), padx=2, pady=6)
        lbtitle.pack(side=TOP, fill=X)

        # Main frame
        frame = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="lightslategrey")
        frame.place(x=0, y=130, width=1550, height=400)  # Corrected width

        # Data Frame Left
        DataFrameLeft = LabelFrame(frame, text="Library Membership Information ", bg="lightslategrey", fg="green",
                                   bd=20, relief=RIDGE, font=("times new roman", 15, "bold"))
        DataFrameLeft.place(x=0, y=5, width=950, height=350)

        lbMemebr = Label(DataFrameLeft, bg="lightslategrey", text="Member Type", font=("times new roman", 20, "bold"),
                         padx=4, pady=2)
        lbMemebr.grid(row=0, column=0, sticky=W)

        comMember = ttk.Combobox(DataFrameLeft, font=("times new roman", 13, "bold"), width=27,
                                 textvariable=self.member_var, state="readonly")
        comMember["value"] = ("Admin Staff", "Student", "Lecture")
        comMember.grid(row=0, column=1)

        lbPRN_No = Label(DataFrameLeft, bg="lightslategrey", text="PRN No.", font=("times new roman", 20, "bold"),
                         padx=4, pady=2)
        lbPRN_No.grid(row=1, column=0, sticky=W)
        txtPRN_NO = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.prn_no_var, width=29)
        txtPRN_NO.grid(row=1, column=1)

        lbTitle = Label(DataFrameLeft, bg="lightslategrey", text="Title", font=("times new roman", 20, "bold"), padx=4,
                        pady=2)
        lbTitle.grid(row=2, column=0, sticky=W)
        txtTitle = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.id_var, width=29)
        txtTitle.grid(row=2, column=1)

        lbFirstName = Label(DataFrameLeft, bg="lightslategrey", text="First Name", font=("times new roman", 20, "bold"),
                            padx=4, pady=2)
        lbFirstName.grid(row=3, column=0, sticky=W)
        txtFirstName = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.firstname_var, width=29)
        txtFirstName.grid(row=3, column=1)

        lbLastName = Label(DataFrameLeft, bg="lightslategrey", text="Last Name", font=("times new roman", 20, "bold"),
                           padx=4, pady=2)
        lbLastName.grid(row=4, column=0, sticky=W)
        txtLastName = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.lastname_var, width=29)
        txtLastName.grid(row=4, column=1)

        lbAddress = Label(DataFrameLeft, bg="lightslategrey", text="Address", font=("times new roman", 20, "bold"),
                          padx=4, pady=2)
        lbAddress.grid(row=5, column=0, sticky=W)
        txtAddress = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.address_var, width=29)
        txtAddress.grid(row=5, column=1)

        lbPostCode = Label(DataFrameLeft, bg="lightslategrey", text="Post Code", font=("times new roman", 20, "bold"),
                           padx=4, pady=2)
        lbPostCode.grid(row=6, column=0, sticky=W)
        txtPostCode = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.postcode_var, width=29)
        txtPostCode.grid(row=6, column=1)

        lbMobile = Label(DataFrameLeft, bg="lightslategrey", text="Mobile", font=("times new roman", 20, "bold"), padx=4,
                         pady=2)
        lbMobile.grid(row=7, column=0, sticky=W)
        txtMobile = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.mobile_var, width=29)
        txtMobile.grid(row=7, column=1)

        lbBookId = Label(DataFrameLeft, bg="lightslategrey", text="Book ID", font=("times new roman", 20, "bold"),
                         padx=4, pady=2)
        lbBookId.grid(row=0, column=2, sticky=W)
        txtBookId = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.bookid_var, width=27)
        txtBookId.grid(row=0, column=3)

        lbBookTitle = Label(DataFrameLeft, bg="lightslategrey", text="Book Title", font=("times new roman", 20, "bold"),
                            padx=4, pady=2)
        lbBookTitle.grid(row=1, column=2, sticky=W)
        txtBookTitle = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.booktitle_var, width=27)
        txtBookTitle.grid(row=1, column=3)

        lbDateBorrowed = Label(DataFrameLeft, bg="lightslategrey", text="Date Borrowed",
                               font=("times new roman", 20, "bold"), padx=4, pady=2)
        lbDateBorrowed.grid(row=2, column=2, sticky=W)
        txtDateBorrowed = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.dateborrowed_var, width=27)
        txtDateBorrowed.grid(row=2, column=3)

        lbDateDue = Label(DataFrameLeft, bg="lightslategrey", text="Date Due", font=("times new roman", 20, "bold"),
                          padx=4, pady=2)
        lbDateDue.grid(row=3, column=2, sticky=W)
        txtDateDue = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.datedue_var, width=27)
        txtDateDue.grid(row=3, column=3)

        lbDaysOnBook = Label(DataFrameLeft, bg="lightslategrey", text="Days On Book", font=("times new roman", 20, "bold"),
                             padx=4, pady=2)
        lbDaysOnBook.grid(row=4, column=2, sticky=W)
        txtDaysOnBook = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.daysonbook_var, width=27)
        txtDaysOnBook.grid(row=4, column=3)

        lbLateReturnFine = Label(DataFrameLeft, bg="lightslategrey", text="Late Return Fine",
                                 font=("times new roman", 20, "bold"), padx=4, pady=2)
        lbLateReturnFine.grid(row=5, column=2, sticky=W)
        txtLateReturnFine = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.latereturnfine_var,
                                  width=27)
        txtLateReturnFine.grid(row=5, column=3)

        lbDateOverdue = Label(DataFrameLeft, bg="lightslategrey", text="Date Overdue", font=("times new roman", 20, "bold"),
                              padx=4, pady=2)
        lbDateOverdue.grid(row=6, column=2, sticky=W)
        txtDateOverdue = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.dateoverdue_var, width=27)
        txtDateOverdue.grid(row=6, column=3)

        lbFinalPrice = Label(DataFrameLeft, bg="lightslategrey", text="Actual Price", font=("times new roman", 20, "bold"),
                             padx=4, pady=2)
        lbFinalPrice.grid(row=7, column=2, sticky=W)
        txtFinalPrice = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.finalprice_var, width=27)
        txtFinalPrice.grid(row=7, column=3)

        # Data Frame Right
        DataFrameRight = LabelFrame(frame, text="Book Details", bg="lightslategrey", fg="green", bd=20, relief=RIDGE,
                                    font=("times new roman", 15, "bold"))
        DataFrameRight.place(x=960, y=5, width=540, height=350)

        self.txtBox = Text(DataFrameRight, font=("times new roman", 12, "bold"), width=32, height=16, padx=2, pady=6)
        self.txtBox.grid(row=0, column=2)

        listScrollbar = Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0, column=1, sticky="ns")

        listBooks = ['Clean Code', 'CLR via C#', 'Pragmatic Programmer', 'Design Patterns', 'Refactoring', 'JavaScript: The Good Parts',
                     'Code Complete', 'Head First Design Patterns']

        def SelectBook(evt):
            value = str(listBox.get(listBox.curselection()))
            x = value
            self.bookid_var.set("AB123")
            self.booktitle_var.set("paul beery")
            
            d1=datetime.datetime.today()
            d2=datetime.timedelta(days=15)
            d3=d1+d2
            self.dateborrowed_var(d1)
            
            self.datedue_var.set(d3)
            self.daysonbook_var(15)
            self.latereturnfine_var("Rs.50")
            self.dateoverdue_var.set("No")
            self.finalprice_var.set("Rs.788")
            

        listBox = Listbox(DataFrameRight, font=("times new roman", 12, "bold"), width=20, height=16)
        listBox.bind("<<ListboxSelect>>", SelectBook)
        listBox.grid(row=0, column=0, padx=8)
        listScrollbar.config(command=listBox.yview)

        for item in listBooks:
            listBox.insert(END, item)

        # Buttons Frame
        framebutton = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="lightslategrey")
        framebutton.place(x=0, y=530, width=1550, height=70)

        btnAddData = Button(framebutton, command=self.add_data, text="Add Data", font=("arial", 12, "bold"), width=23,
                            bg="green", fg="white")
        btnAddData.grid(row=0, column=0)

        btnShowData = Button(framebutton,command=self.showData, text="Show Data", font=("arial", 12, "bold"), width=23, bg="green", fg="white")
        btnShowData.grid(row=0, column=1)

        btnUpdate = Button(framebutton, text="Update", font=("arial", 12, "bold"), width=23, bg="green", fg="white")
        btnUpdate.grid(row=0, column=2)

        btnDelete = Button(framebutton, text="Delete", font=("arial", 12, "bold"), width=23, bg="green", fg="white")
        btnDelete.grid(row=0, column=3)

        btnReset = Button(framebutton,command=self.reset, text="Reset", font=("arial", 12, "bold"), width=23, bg="green", fg="white")
        btnReset.grid(row=0, column=4)

        btnExit = Button(framebutton,command=self.iExit ,text="Exit", font=("arial", 12, "bold"), width=23, bg="green", fg="white")
        btnExit.grid(row=0, column=5)

        # Information Frame
        frameDetails = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="lightslategrey")
        frameDetails.place(x=0, y=600, width=1550, height=195)

        table_frame = Frame(frameDetails, bd=6, relief=RIDGE, bg="lightslategrey")
        table_frame.place(x=0, y=2, width=1420, height=190)

        xscroll = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        yscroll = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.library_table = ttk.Treeview(table_frame, column=("member", "prnno", "title", "firstname", "lastname",
                                                               "address", "postcode", "mobile", "bookid", "booktitle",
                                                               "dateborrowed", "datedue", "daysonbook", "latereturnfine",
                                                               "dateoverdue", "finalprice"),
                                          xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)

        xscroll.pack(side=BOTTOM, fill=X)
        yscroll.pack(side=RIGHT, fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        self.library_table.heading("member", text="Member")
        self.library_table.heading("prnno", text="PRN No.")
        self.library_table.heading("title", text="Title")
        self.library_table.heading("firstname", text="First Name")
        self.library_table.heading("lastname", text="Last Name")
        self.library_table.heading("address", text="Address")
        self.library_table.heading("postcode", text="Post Code")
        self.library_table.heading("mobile", text="Mobile No.")
        self.library_table.heading("bookid", text="Book ID")
        self.library_table.heading("booktitle", text="Book Title")
        self.library_table.heading("dateborrowed", text="Date Borrowed")
        self.library_table.heading("datedue", text="Date Due")
        self.library_table.heading("daysonbook", text="Days On Book")
        self.library_table.heading("latereturnfine", text="Late Return Fine")
        self.library_table.heading("dateoverdue", text="Date Overdue")
        self.library_table.heading("finalprice", text="Final Price")

        self.library_table["show"] = "headings"
        self.library_table.column("member", width=100)
        self.library_table.column("prnno", width=100)
        self.library_table.column("title", width=100)
        self.library_table.column("firstname", width=100)
        self.library_table.column("lastname", width=100)
        self.library_table.column("address", width=100)
        self.library_table.column("postcode", width=100)
        self.library_table.column("mobile", width=100)
        self.library_table.column("bookid", width=100)
        self.library_table.column("booktitle", width=100)
        self.library_table.column("dateborrowed", width=100)
        self.library_table.column("datedue", width=100)
        self.library_table.column("daysonbook", width=100)
        self.library_table.column("latereturnfine", width=100)
        self.library_table.column("dateoverdue", width=100)
        self.library_table.column("finalprice", width=100)
        
        self.fatch_data
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)

        self.library_table.pack(fill=BOTH, expand=1)

    def add_data(self):
       conn=mysql.connector(host="localhost",username="root",passwords="database2024",database="lms1")
       my_cursor=conn.cursor()
       my_cursor.execute=("insert into libray values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                               self.member_var.get(),
                               self.prn_no_var.get(),
                               self.id_var.get(),
                               self.firstname_var.get(),
                               self.lastname_var.get(),
                               self.address_var.get(),                               
                               self.postcode_var.get(),                               
                               self.mobile_var.get(),
                               self.bookid_var.get(),
                               self.booktitle_var.get(),
                               self.dateborrowed_var.get(),
                               self.datedue_var.get(),
                               self.daysonbook_var.get(),
                               self.latereturnfine_var.get(),

                              self.dateoverdue_var.get(),
                              self.finalprice_var.get(),))
       conn.commit
       self.fatch_data
       conn.close
    
    messagebox.showinfo("Success","Memeber has been inserted successfully")
    pass
    
    def update(self):
          conn=mysql.connector(host="localhost",username="root",passwords="database2024",database="lms1")
          my_cursor=conn.cursor()
          my_cursor.excecute("update library set Member=%,  ")
  
    def fatch_data(self):
         conn=mysql.connector(host="localhost",username="root",passwords="database2024",database="lms1")
         my_cursor=conn.cursor()
         my_cursor.excecute("select *from library ")
         
         if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END,values=i)
                
            conn.commit()
            
            conn.close()
            
    def get_cursor(self,event=""):
          cursor_row=self.library_table.focus()
          content=self.library_table.item(cursor_row)
          row=content['values']
          
          self.member_var.set(row[0])
          self.prn_no_var.set(row[1])
          self.firstname_var.set(row[2])


          self.lastname_var.set(row[3])
          self.postcode_var.set(row[4])
          self.address_var.set(row[5])
          self.mobile_var.set(row[6])
          self.bookid_var.set(row[7])
          self.booktitle_var.set(row[8])
          self.dateborrowed_var.set(row[9])
          self.datedue_var.set(row[10])
          self.daysonbook_var.set(row[11])
          self.latereturnfine_var.set(row[12])
          self.dateoverdue_var.set(row[13])
          self.finalprice_var.set(row[14])
          
          
          
    def showData(self):
          self.txtBox.insert(END,"Member Type\t\t"+self.member_var.get()+"\n")
          self.txtBox.insert(END,"PRN NO.\t\t"+self.prn_no_var.get()+"\n")
          self.txtBox.insert(END,"IDNO. \t\t"+self.id_var.get()+"\n")
          self.txtBox.insert(END,"First Name\t\t"+self.firstname_var.get()+"\n")
          self.txtBox.insert(END,"Last Name\t\t"+self.lastname_var.get()+"\n")
          self.txtBox.insert(END,"address\t\t"+self.address_var.get()+"\n")
          self.txtBox.insert(END,"postcode\t\t"+self.postcode_var.get()+"\n")
          self.txtBox.insert(END,"mobile\t\t"+self.mobile_var.get()+"\n")
          self.txtBox.insert(END,"bookid\t\t"+self.bookid_var.get()+"\n")
          self.txtBox.insert(END,"booktitlee\t\t"+self.booktitle_var.get()+"\n")
          self.txtBox.insert(END,"dateborrowed\t\t"+self.dateborrowed_var.get()+"\n")
          self.txtBox.insert(END,"datedue\t\t"+self.datedue_var.get()+"\n")
          self.txtBox.insert(END,"daysonbook\t\t"+self.daysonbook_var.get()+"\n")
          self.txtBox.insert(END,"latereturnfin\t\t"+self.latereturnfine_var.get()+"\n")
          self.txtBox.insert(END,"dateoverdu\t\t"+self.dateoverdue_var.get()+"\n")
          self.txtBox.insert(END,"finalprice\t\t"+self.finalprice_var.get()+"\n")
          
    def reset(self):
          self.member_var.set(""),
          self.prn_no_var.set(""),
          self.id_var.set(""),
          self.firstname_var.set(""),
          self.lastname_var.set(""),
          self.address_var.set(""),
          self.postcode_var.set(""),
          self.mobile_var.set(""),
          self.bookid_var.set(""),
          self.booktitle_var.set(""),
          self.dateborrowed_var.set(""),
          self.datedue_var.set(""),
          self.daysonbook_var.set(""),
          self.finalprice_var.set(""),
          self.txtBox.set(""),
          
          
    def iExit(self):
          iExit=tkinter.messagebox.askyesno("library mangement system ","Do you want to exit")
          if iExit>0:
              self.root.destory()
              return
              
        
         
    def delete(self):
        if self.prn_no_var.get()=="" or self.id_var.get()=="":
            messagebox.showerror("Error","First select the member")   
            
        else : 
             conn=mysql.connector(host="localhost",username="root",passwords="database2024",database="lms1")
             my_cursor=conn.cursor()
             query="delete from library where PRN_No=%s"
             
             conn.commit()
             self.fatch_data()
             self.reset()
             conn.close()
             
             messagebox.showinfo("Sucess"",Member has been Deleted")

if __name__ == "__main__":
    root = Tk()
    obj = LibraryManagementSystem(root)
    root.mainloop()
