from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import scrolledtext
from tkinter.ttk import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import cx_Oracle
import random
import smtplib

window=Tk()
window.title("AIRLINE RESERVATION PORTAL")
window.geometry('300x400')

menu=Menu(window)
login=Menu(menu,tearoff=0)

def adlog():
    
    def login():
        
        con=cx_Oracle.connect('SYSTEM/Qplfc95060@192.168.56.1/xe')
        cur=con.cursor()
        
        sql="select * from Admin"
        cur.execute(sql)
        
        f=0
        for row in cur:
            if row[0]=='%s' %(uname2.get()) and row[1]=='%s' %(pwd2.get()):
                
                messagebox.showinfo("LOGIN!",'Login successful..')
                window1.destroy()
                
                window5=Toplevel(window)
                window5.title("AIRLINE RESERVATION PORTAL")
                window5.geometry('300x400')
                
                menu=Menu(window5)
                
                flight=Menu(menu,tearoff=0)
                
                
                def addflight():
                    
                    def add():
                        
                        con=cx_Oracle.connect('SYSTEM/Qplfc95060@192.168.56.1/xe')
                        cur=con.cursor()
                        
                        c_sql="select * from Flight"
                        cur.execute(c_sql)
                        
                        f=0
                        for row in cur:
                            if row[0]==int('%s' %(no.get())):
                                window6.destroy()
                                messagebox.showerror('ERROR','Flight Number Already Exists')
                                f=1
                                break
                        
                        if f==0:
                            
                            sql="insert into Flight(fno,fname,depcity,arrcity,avdate) values('%s','%s','%s','%s',to_date('%s','dd/mm/yyyy'))" %(no.get(),name.get(),dep_city.get(),arr_city.get(),days.get())
                            cur.execute(sql)
                            messagebox.showinfo('SUCCESS!','New Flight ADDED Successfully..')
                        
                        con.commit()
                        con.close()
                        
                    no=StringVar()
                    name=StringVar()
                    dep_city=StringVar()
                    arr_city=StringVar()
                    days=StringVar()
                    
                    window6=Toplevel(window5)
                    window6.title('AIRLINE RESERVATION PORTAL')
                    window6.geometry('300x400')
                    
                    Label(window6,text='ADD FLIGHT').grid(row=0,columnspan=2,sticky='WE')
                    Label(window6,text='').grid(row=1)
                    Label(window6,text='Flight Number').grid(row=2)
                    Label(window6,text='Flight Name').grid(row=3)
                    Label(window6,text='Departure City').grid(row=4)
                    Label(window6,text='Arrival City').grid(row=5)
                    Label(window6,text='Running Date').grid(row=6)
                    Entry(window6,textvariable=no).grid(row=2,column=1)
                    Entry(window6,textvariable=name).grid(row=3,column=1)
                    Entry(window6,textvariable=dep_city).grid(row=4,column=1)
                    Entry(window6,textvariable=arr_city).grid(row=5,column=1)
                    Entry(window6,textvariable=days).grid(row=6,column=1)
                    Label(window6,text='').grid(row=7)
                    Button(window6,text='Add',command=add).grid(row=8,column=1,sticky='W')    
                    
                    
                    window6.mainloop()
                
                flight.add_command(label='Add Flight',command=addflight)
                flight.add_separator()
                
                def remflight():
                    
                    def rem():
                        
                        con=cx_Oracle.connect('SYSTEM/Qplfc95060@192.168.56.1/xe')
                        cur=con.cursor()
                        
                        c_sql="select * from Flight"
                        cur.execute(c_sql)
                        
                        f=0
                        for row in cur:
                             if (row[0])==int('%s' %(no.get())):
                                f=1
                                break
                        
                        if f==1:
                            sql="delete from Flight where fno='%s'" %(no.get())
                            cur.execute(sql)
                            messagebox.showinfo('SUCCESS!','Flight REMOVED Successfully..')
                            window7.destroy()
                        else:
                            messagebox.showerror('ERROR','Requested Flight Not Found!!')
                            window7.destroy()
                        
                        con.commit()
                        con.close()
                    
                    no=StringVar()
                    
                    window7=Toplevel(window5)
                    window7.title('AIRLINE RESERVATION PORTAL')
                    window7.geometry('300x400')
                    
                    Label(window7,text='REMOVE FLIGHT').grid(row=0,columnspan=2,sticky='WE')
                    Label(window7,text='').grid(row=1)
                    Label(window7,text='Flight Number').grid(row=2)
                    Entry(window7,textvariable=no).grid(row=2,column=1)
                    Label(window7,text='').grid(row=3)
                    Button(window7,text='Remove',command=rem).grid(row=4,column=1,sticky='W')
                    
                    
                    window7.mainloop()
                
                flight.add_command(label='Remove Flight',command=remflight)
                flight.add_separator()
                
                def modflight():
                    
                    def submit():
                        
                        def mod():
                            
                            con=cx_Oracle.connect('SYSTEM/Qplfc95060@192.168.56.1/xe')
                            cur=con.cursor()
                        
                            c_sql="select * from Flight"
                            cur.execute(c_sql)
                        
                            f=0
                            for row in cur:
                                if (row[0])==int('%s' %(no.get())):
                                    f=1
                                    break
                        
                            if f==1:
                                sql="update Flight set fname='%s',depcity='%s',arrcity='%s',avdate=to_date('%s','dd/mm/yyyy') where fno='%s'" %(name2.get(),dep_city2.get(),arr_city2.get(),days2.get(),no.get())
                                cur.execute(sql)
                                e1.configure(state='disabled')
                                messagebox.showinfo('SUCCESS!','Flight MODIFIED Successfully..')
                                
                            else:
                                messagebox.showerror('ERROR','Requested Flight Not Found!!')
                                window8.destroy()
                        
                            con.commit()
                            con.close()
                        
                        Label(window8,text='').grid(row=5)
                        Label(window8,text='New Flight Name').grid(row=6)
                        Label(window8,text='New Departure City').grid(row=7)
                        Label(window8,text='New Arrival City').grid(row=8)
                        Label(window8,text='New Running Date').grid(row=9)
                        
                        Entry(window8,textvariable=name2).grid(row=6,column=1)
                        Entry(window8,textvariable=dep_city2).grid(row=7,column=1)
                        Entry(window8,textvariable=arr_city2).grid(row=8,column=1)
                        Entry(window8,textvariable=days2).grid(row=9,column=1)
                        Label(window8,text='').grid(row=10)
                        Button(window8,text='Update',command=mod).grid(row=11,column=1,sticky='W')
                    
                    no=StringVar()
                    name2=StringVar()
                    dep_city2=StringVar()
                    arr_city2=StringVar()
                    days2=StringVar()
                    
                    window8=Toplevel(window5)
                    window8.title('AIRLINE RESERVATION PORTAL')
                    window8.geometry('300x400')
                    
                    Label(window8,text='MODIFY FLIGHT').grid(row=0,columnspan=2,sticky='WE')
                    Label(window8,text='').grid(row=1)
                    Label(window8,text='Current Flight Number').grid(row=2)
                    e1=Entry(window8,textvariable=no)
                    e1.grid(row=2,column=1)
                    Label(window8,text='').grid(row=3)
                    Button(window8,text='Submit',command=submit).grid(row=4,column=1,sticky='W')
                    
                    
                    window8.mainloop()
                    
                flight.add_command(label='Modify Flight',command=modflight)
                
                menu.add_cascade(label='FLIGHT',menu=flight)
                
                options=Menu(menu,tearoff=0)
                
                options.add_command(label='About')
                options.add_separator()
                
                options.add_command(label='Help')
                options.add_separator()
                
                def logout():
                    
                    #m1=messagebox.askyesno('****','Do you want to Log Out?')
                    #if (messagebox.askyesno('****','Do you want to Log Out?'))=='yes':
                        window5.destroy()
                        
                options.add_command(label='Log-Out',command=logout)
                
                menu.add_cascade(label='OPTIONS',menu=options)
                
                window5.config(menu=menu)
                window5.mainloop()
                
                f=1
                break
            
        if f==0:
            messagebox.showerror("LOGIN!",'Login Failed..Try Later..')
            window1.destroy()
                            
        cur.close()
        con.close()
    
    uname2=StringVar()
    pwd2=StringVar()
    
    window1=Toplevel(window)
    window1.title("AIRLINE RESERVATION PORTAL")
    window1.geometry('300x400')
    
    Label(window1,text='ADMIN LOGIN').grid(row=0,columnspan=2,sticky='E')
    Label(window1,text='').grid(row=1)
    Label(window1,text='Username ').grid(row=2)
    Label(window1,text='Password ').grid(row=3)
    Entry(window1,textvariable=uname2).grid(row=2,column=1)
    Entry(window1,textvariable=pwd2).grid(row=3,column=1)
    Label(window1,text='').grid(row=4)
    Button(window1,text='Login',command=login).grid(row=5,column=1)    
    
    window1.mainloop()

login.add_command(label='Admin',command=adlog)
login.add_separator()

def passlog():
    
    def login():
        
        con=cx_Oracle.connect('SYSTEM/Qplfc95060@192.168.56.1/xe')
        cur=con.cursor()
        
        sql="select uname,password from Passenger"
        cur.execute(sql)
        
        f=0
        for row in cur:
            if row[0]=='%s' %(uname2.get()) and row[1]=='%s' %(pwd2.get()):
                
                messagebox.showinfo("LOGIN!",'Login successful..')
                window2.destroy()
                
                window11=Toplevel(window)
                window11.title("AIRLINE RESERVATION PORTAL")
                window11.geometry('300x400')
                
                menu=Menu(window11)
                
                ticket=Menu(menu,tearoff=0)
                
                def dispticket():
                    
                    def display():
                         
                         Label(tab2,text='').grid(row=0)
                         Label(tab2,text='DISPLAY TICKET').grid(row=1,columnspan=2,sticky='WE')
                         Label(tab2,text='').grid(row=2)
                         
                         con=cx_Oracle.connect('SYSTEM/Qplfc95060@192.168.56.1/xe')
                         cur=con.cursor()
                         
                         sql="select * from TravelInfo2"
                         cur.execute(sql)
                        
                         f=0
                         for row in cur:
                             if row[0]==int('%s' %(t_no.get())):
                                 
                                 f=1
                                 messagebox.showinfo('SUCCESS','Match Found..')
                                 
                                 sql1="select * from TravelInfo where tno='%s'" %(t_no.get()) 
                                 cur.execute(sql1)
                                 
                                 for r in cur:
                                     
                                     if int(r[1])==1:
                                         sex='Male'
                                     else:
                                         sex='Female'
                                         
                                     def close():
                                         window14.destroy()
                                         
                                     Label(tab2,text='Name:').grid(row=3,padx=(10, 10))
                                     Label(tab2,text='Sex:').grid(row=4,padx=(10, 10))
                                     Label(tab2,text='Age:').grid(row=5,padx=(10, 10))
                                     Label(tab2,text='Date of Birth:').grid(row=6,padx=(10, 10))
                                     Label(tab2,text='Address:').grid(row=7,padx=(10, 10))
                                     Label(tab2,text='').grid(row=8,padx=(10, 10))
                                     Label(tab2,text='Flight Number:').grid(row=9,padx=(10, 10))
                                     Label(tab2,text='Departure City:').grid(row=10,padx=(10, 10))
                                     Label(tab2,text='Arrival City:').grid(row=11,padx=(10, 10))
                                     Label(tab2,text='Date of Travel:').grid(row=12,padx=(10, 10))
                                         
                                     Label(tab2,text=r[0],font=('Helvetica',10,'bold')).grid(row=3,column=1,padx=(50, 10))
                                     Label(tab2,text=sex,font=('Helvetica',10,'bold')).grid(row=4,column=1,padx=(50, 10))
                                     Label(tab2,text=r[2],font=('Helvetica',10,'bold')).grid(row=5,column=1,padx=(50, 10))
                                     Label(tab2,text=r[3],font=('Helvetica',10,'bold')).grid(row=6,column=1,padx=(50, 10))
                                     Label(tab2,text=r[4],font=('Helvetica',10,'bold')).grid(row=7,column=1,padx=(50, 10))
                                     Label(tab2,text=r[9],font=('Helvetica',10,'bold')).grid(row=9,column=1,padx=(50, 10))
                                     Label(tab2,text=r[5],font=('Helvetica',10,'bold')).grid(row=10,column=1,padx=(50, 10))
                                     Label(tab2,text=r[6],font=('Helvetica',10,'bold')).grid(row=11,column=1,padx=(50, 10))
                                     Label(tab2,text=r[7],font=('Helvetica',10,'bold')).grid(row=12,column=1,padx=(50, 10))
                                     Label(tab2,text='',font=('Helvetica',10,'bold')).grid(row=13,column=1,padx=(50, 10))
                                     Button(tab2,text='CLOSE',command=close).grid(row=14,column=1)
                                     
                                 con.close()
                                 break
                             
                         if f==0:
                             messagebox.showerror('ERROR','Invalid TNo.. Try Again')
                             window14.destroy()
                                 
                    t_no=StringVar()
                    
                    window14=Toplevel(window11)
                    window14.title('AIRLINE RESERVATION PORTAL')
                    window14.geometry('430x380')
                    
                    tab_control=ttk.Notebook(window14)
                    
                    tab1=ttk.Frame(tab_control)
                    tab_control.add(tab1,text='CHECK')
                    
                    tab2=ttk.Frame(tab_control)
                    tab_control.add(tab2,text='DISPLAY')
                    
                    Label(tab1,text='').grid(row=0)
                    Label(tab1,text='DISPLAY TICKET').grid(row=1,columnspan=2,sticky='WE')
                    Label(tab1,text='').grid(row=2)
                    Label(tab1,text='Enter TNo').grid(row=3)
                    
                    Entry(tab1,textvariable=t_no).grid(row=3,column=1)
                    Label(tab1,text='').grid(row=4)
                    Button(tab1,text='SUBMIT',command=display).grid(row=5,column=1)
                    
                    tab_control.pack(expand=1,fill='both')
                    window14.mainloop()
                    
                    
                ticket.add_command(label='Display Ticket',command=dispticket)
                ticket.add_separator()
                
                def resticket():
                    
                    def submit():
                        
                        def reserve():
                            
                            con=cx_Oracle.connect('SYSTEM/Qplfc95060@192.168.56.1/xe')
                            cur=con.cursor()
                            
                            sql1="select * from Flight"
                            cur.execute(sql1)
                        
                            f=0
                            for row in cur:
                                if row[0]==int('%s' %(fno2.get())) and row[2]=='%s' %(d) and row[3]=='%s' %(a):
                                    
                                    f=1
                                    break
                            
                            if f==1:
                                
                                sql="insert into TravelInfo(name,sex,age,dob,address,depcity,arrcity,dateoftrip,fno,email) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" %(name.get(),sex.get(),age.get(),dob.get(),address.get(),dep_city.get(),arr_city.get(),date.get(),fno2.get(),email.get())
                                cur.execute(sql)
                                
                                messagebox.showinfo('RESERVE','The given flight has been reserved.. A unique ticket number TNo has been sent to your email account..')
                                
                                con.commit()
                                con.close()
                                
                                conn=cx_Oracle.connect('SYSTEM/Qplfc95060@192.168.56.1/xe')
                                cur=conn.cursor()
                                
                                t_no=random.randint(10000,99999)
                                
                                sql="insert into TravelInfo2 values(%d)" %(t_no)
                                cur.execute(sql)
                                
                                sql1="update TravelInfo set tno=%d where name='%s'" %(t_no,name2.get())
                                cur.execute(sql1)
                                
                                
                                msg=MIMEMultipart()
                                msg['From']="arpsys123@gmail.com"
                                password="Qplfc95060"
                                msg['To']="rahulgopinath17@gmail.com"
                                msg['Subject']="Ticket Reservation"
                                
                                body="Ticket NO: %d\nPlease use this given booking reference number for further activities such as csncellation or viewing of ticket.. "%t_no
                                msg.attach(MIMEText(body,'html'))
                                
                                server=smtplib.SMTP("smtp.gmail.com:587",timeout=120)
                                server.starttls()
                                server.login(msg['From'],password)
                                server.sendmail(msg['From'],msg['To'],msg.as_string())
                                server.quit()
                                
                                conn.commit()
                                conn.close()
                            
                            else:
                                messagebox.showerror("ERROR",'The given flight does not exist..')
                                #window12.destory()
                            
                        def close():
                            
                            window12.destroy()
                            
                        fno2=StringVar()
                        name2=StringVar()
                        
                        Label(tab3,text='').grid(row=0)
                        Label(tab3,text='SELECT TICKET').grid(row=1,columnspan=2,sticky='WE')
                        Label(tab3,text='').grid(row=2)
                        
                        txt = scrolledtext.ScrolledText(tab3,width=50,height=10)
                        txt.grid(row=3,columnspan=2)
                        Label(tab3,text='').grid(row=4)
                        Label(tab3,text='Flight Number').grid(row=5)
                        
                        con=cx_Oracle.connect('SYSTEM/Qplfc95060@192.168.56.1/xe')
                        cur=con.cursor()
                        
                        messagebox.showinfo("RESERVATION",'Here are a list of flights that fit your travel details')
                        
                        sql1="select * from Flight"
                        cur.execute(sql1)
                        
                        d=dep_city.get()
                        a=arr_city.get()
                        
                        for row in cur:
                            if row[2]=='%s' %(d) and row[3]=='%s' %(a):
                                
                                txt.insert(INSERT,row[0])
                                txt.insert(INSERT," ")
                                txt.insert(INSERT,row[1])
                                txt.insert(INSERT," ")
                                txt.insert(INSERT,row[2])
                                txt.insert(INSERT," ")
                                txt.insert(INSERT,row[3])
                                txt.insert(INSERT," ")
                                txt.insert(INSERT,row[4])
                                txt.insert(INSERT,"\n")
                        
                            
                        con.commit()
                        con.close()
        
                        
                        Entry(tab3,textvariable=fno2).grid(row=5,column=1)
                        Label(tab3,text='Enter Name (For CONFIRMATION) ').grid(row=6)
                        Entry(tab3,textvariable=name2).grid(row=6,column=1)
                        Label(tab3,text='').grid(row=7)
                        Button(tab3,text='RESERVE',command=reserve).grid(row=8,column=0,sticky='E')
                        Button(tab3,text='CLOSE',command=close).grid(row=9,column=0,sticky='E')
                        
                    def back():
                        
                        window12.destroy()
                        
                    dep_city=StringVar()
                    arr_city=StringVar()
                    date=StringVar()
                    name=StringVar()
                    sex=StringVar()
                    age=StringVar()
                    dob=StringVar()
                    email=StringVar()
                    address=StringVar()
                    
                    window12=Toplevel(window11)
                    window12.title('AIRLINE RESERVATION PORTAL')
                    window12.geometry('430x380')
                    
                    tab_control=ttk.Notebook(window12)
                    
                    tab1=ttk.Frame(tab_control)
                    tab_control.add(tab1,text='FLIGHT')
                    
                    tab2=ttk.Frame(tab_control)
                    tab_control.add(tab2,text='PERSONAL')
                    
                    tab3=ttk.Frame(tab_control)
                    tab_control.add(tab3,text='SELECTION')
                    
                    Label(tab1,text='').grid(row=0)
                    Label(tab1,text='RESERVE TICKET').grid(row=1,columnspan=2,sticky='WE')
                    Label(tab1,text='').grid(row=2)
                    Label(tab1,text='Departure City').grid(row=3)
                    Label(tab1,text='Arrival City').grid(row=4)
                    Label(tab1,text='Date of Travel').grid(row=5)
                    
                    
                    combo1=Combobox(tab1,textvariable=dep_city)
                    combo1['values']=('LasVegas','California','AbuDhabi','Singapore','Australia','London','NewYork')
                    combo1.grid(row=3,column=1)
                    combo1.current(0)
                    combo1=Combobox(tab1,textvariable=arr_city)
                    combo1['values']=('LasVegas','California','AbuDhabi','Singapore','Australia','London','NewYork')
                    combo1.grid(row=4,column=1)
                    combo1.current(1)
                    Entry(tab1,textvariable=date).grid(row=5,column=1)
                    Label(tab1,text='').grid(row=6)
                    
                    Label(tab2,text='').grid(row=0)
                    Label(tab2,text='PERSONAL DETAILS').grid(row=1,columnspan=2,sticky='WE')
                    Label(tab2,text='').grid(row=2)
                    Label(tab2,text='Full Name').grid(row=3)
                    Label(tab2,text='Sex').grid(row=4)
                    Label(tab2,text='Age').grid(row=5)
                    Label(tab2,text='Date of Birth').grid(row=6)
                    Label(tab2,text='E-Mail').grid(row=7)
                    Label(tab2,text='Address').grid(row=8)
                    
                    Entry(tab2,textvariable=name).grid(row=3,column=1,columnspan=2)
                    Radiobutton(tab2,text='Male',variable=sex,value=1).grid(column=1,row=4,sticky='W')
                    Radiobutton(tab2,text='Female',variable=sex,value=2).grid(column=2,row=4,sticky='W')
                    Spinbox(tab2,from_=1,to=120,textvariable=age).grid(column=1,row=5,columnspan=2)
                    Entry(tab2,textvariable=dob).grid(row=6,column=1,columnspan=2)
                    Entry(tab2,textvariable=email).grid(row=7,column=1,columnspan=2)
                    Entry(tab2,textvariable=address,width=50).grid(row=8,column=1,columnspan=3,sticky='E')
                    Label(tab2,text='').grid(row=9)
                    
                    Button(tab2,text='SUBMIT',command=submit).grid(row=10,column=1)
                    Button(tab2,text='BACK',command=back).grid(row=11,column=1)
                    

                    tab_control.pack(expand=1,fill='both')
                    
                    window12.mainloop()
                    
                
                ticket.add_command(label='Reserve Ticket',command=resticket)
                ticket.add_separator()
                
                def canticket():
                    
                    window13=Toplevel(window11)
                    window13.title('AIRLINE RESERVATION PORTAL')
                    window13.geometry('300x400')
                    
                    def cancel():
                        
                        con=cx_Oracle.connect('SYSTEM/Qplfc95060@192.168.56.1/xe')
                        cur=con.cursor()
                        
                        sql2="select * from TravelInfo2"
                        cur.execute(sql2)
                        
                        f=0
                        for row in cur:
                            if row[0]==int('%s' %(t_no.get())):
                                f=1
                                break
                        
                        if f==1:                        
                            
                            sql="delete from TravelInfo where tno='%s'" %(t_no.get())
                            cur.execute(sql)
                        
                            sql1="delete from TravelInfo2 where tno='%s'" %(t_no.get())
                            cur.execute(sql1)
                        
                            messagebox.showinfo('CANCEL','Ticket has been cancelled successfully')
                        
                        else:
                            messagebox.showerror('ERROR','Invalid Ticket Number..')
                            
                        con.commit()
                        con.close()
                        window13.destroy()
                        
                    t_no=StringVar()
                    name=StringVar()
                    
                    Label(window13,text='').grid(row=0)
                    Label(window13,text='CANCEL TICKET').grid(row=1,columnspan=2,sticky='WE')
                    Label(window13,text='').grid(row=2)
                    Label(window13,text='Ticket NO').grid(row=3)
                    Entry(window13,textvariable=t_no).grid(row=3,column=1)
                    Label(window13,text='').grid(row=4)
                    Button(window13,text='SUBMIT',command=cancel).grid(row=5,column=1)
                    
                    window13.mainloop()
                    
                ticket.add_command(label='Cancel Ticket',command=canticket)
                
                menu.add_cascade(label='TICKET',menu=ticket)
                
                flight=Menu(menu,tearoff=0)
                
                flight.add_command(label='Search for Flight')
                flight.add_separator()
                
                flight.add_command(label='Display all Flights')
                
                menu.add_cascade(label='FLIGHT',menu=flight)
                
                options=Menu(menu,tearoff=0)
                
                options.add_command(label='About')
                options.add_separator()
                
                options.add_command(label='Help')
                options.add_separator()
                
                def logout():
                    
                    #m1=messagebox.askyesno('****','Do you want to Log Out?')
                    #if (messagebox.askyesno('****','Do you want to Log Out?'))=='yes':
                        window11.destroy()
                        
                options.add_command(label='Log-Out',command=logout)
                
                menu.add_cascade(label='OPTIONS',menu=options)
                
                window11.config(menu=menu)
                window11.mainloop()
                
                f=1
                break
        if f==0:
            messagebox.showerror("LOGIN!",'Login Failed..Try Later..')
            window2.destroy()

        cur.close()
        con.close()
    
    uname2=StringVar()
    pwd2=StringVar()
    
    window2=Toplevel(window)
    window2.title("AIRLINE RESERVATION PORTAL")
    window2.geometry('300x400')
    
    Label(window2,text='PASSENGER LOGIN').grid(row=0,columnspan=2,sticky='E')
    Label(window2,text='').grid(row=1)
    Label(window2,text='Username ').grid(row=2)
    Label(window2,text='Password ').grid(row=3)
    Entry(window2,textvariable=uname2).grid(row=2,column=1)
    Entry(window2,textvariable=pwd2).grid(row=3,column=1)
    Label(window2,text='').grid(row=4)
    Button(window2,text='Login',command=login).grid(row=5,column=1)    
    
    window2.mainloop()

login.add_command(label='Passenger',command=passlog)

menu.add_cascade(label='LOGIN', menu=login)

register = Menu(menu,tearoff=0)

def adreg():
    
    def register():
        
        con=cx_Oracle.connect('SYSTEM/Qplfc95060@192.168.56.1/xe')
        cur=con.cursor()
        
        c_sql="select * from Admin"
        cur.execute(c_sql)
        
        f=0        
        for row in cur:
            if row[0]=='%s' %(uname.get()):
                messagebox.showerror('ERROR','Username already exists...')
                f=1
                break
        
        if f==0:
            sql="insert into Admin(uname,password) values('%s','%s')" %(uname.get(),pwd.get())
            cur.execute(sql)
            messagebox.showinfo('REGISTERED!','Admin Registration completed successfully...We have sent a confirmation mail into your account')
            
        window3.destroy()
        con.commit()
        con.close()
    
    uname=StringVar()
    pwd=StringVar()
    
    window3=Toplevel(window)
    window3.title("AIRLINE RESERVATION PORTAL")
    window3.geometry('300x400')
    
    Label(window3,text='ADMIN REGISTRATION').grid(row=0,columnspan=2,sticky='E')
    Label(window3,text='').grid(row=1)
    Label(window3,text='Username ').grid(row=2)
    Label(window3,text='Password ').grid(row=3)
    Entry(window3,textvariable=uname).grid(row=2,column=1)
    Entry(window3,textvariable=pwd).grid(row=3,column=1)
    Label(window3,text='').grid(row=4)
    Button(window3,text='Register',command=register).grid(row=5,column=1)    
    
    window3.mainloop()

register.add_command(label='Admin',command=adreg)
register.add_separator()

def passreg():
    
    def register():
        
        con=cx_Oracle.connect('SYSTEM/Qplfc95060@192.168.56.1/xe')
        cur=con.cursor()
         
        c_sql="select uname,password from Passenger"
        cur.execute(c_sql)
        
        f=0        
        for row in cur:
            if row[0]=='%s' %(uname.get()):
                messagebox.showerror('ERROR','Username already exists...')
                f=1
                break
        
        if f==0:
            sql="insert into Passenger(uname,password) values('%s','%s')" %(uname.get(),pwd.get())
            cur.execute(sql)
            messagebox.showinfo('REGISTERED!','Passenger Registration completed successfully...We have sent a confirmation mail into your account')
        
        window4.destroy()
        con.commit()
        con.close()
    
    uname=StringVar()
    pwd=StringVar()
    
    window4=Toplevel(window)
    window4.title("AIRLINE RESERVATION PORTAL")
    window4.geometry('300x400')
    
    Label(window4,text='PASSENGER REGISTRATION').grid(row=0,columnspan=2,sticky='E')
    Label(window4,text='').grid(row=1)
    Label(window4,text='Username ').grid(row=2)
    Label(window4,text='Password ').grid(row=3)
    Entry(window4,textvariable=uname).grid(row=2,column=1)
    Entry(window4,textvariable=pwd).grid(row=3,column=1)
    Label(window4,text='').grid(row=4)
    Button(window4,text='Register',command=register).grid(row=5,column=1)    
    
    window4.mainloop()

register.add_command(label='Passenger',command=passreg)

menu.add_cascade(label='REGISTER', menu=register)


window.config(menu=menu)

window.mainloop()