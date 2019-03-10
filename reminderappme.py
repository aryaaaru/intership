import sys
import datetime
import calendar
import tkinter as tk
from tkinter import *
from tkinter import messagebox as mbox
#from tkinter import calendar as cal
from datetime import datetime
from reminderappdb import Remdb

database=Remdb("reminderappme.db")

class Window(object):

    def __init__(self,window):

        self.window = window

        self.window.wm_title("Reminder")

        b1=Button(window,text="View", width=12,command=self.view_rem)
        b1.grid(row=0,column=0)
        
              
        b3=Button(window,text="Add new", width=12,command=self.add_rem)
        b3.grid(row=0,column=1)

        b4=Button(window,text="Update", width=12,command=self.update_rem)
        b4.grid(row=0,column=2)

        b5=Button(window,text="Delete", width=12,command=self.delete_rem)
        b5.grid(row=0,column=3)

        b6=Button(window,text="Close", width=12,command=window.destroy)
        b6.grid(row=0,column=4)

        l1=Label(window,text="Event")
        l1.grid(row=2,column=0)
        l1.visible = True

        l2=Label(window,text="Description")
        l2.grid(row=2,column=2)
        l2.visible = True

        l3=Label(window,text="Date")
        l3.grid(row=3,column=0)
        l3.visible = True

        l5=Label(window,text="Time")
        l5.grid(row=4,column=0)
        l5.visible = True

        l4=Label(window,text="Status")
        l4.grid(row=3,column=2)
        l4.visible = True

        self.title_text=StringVar()
        self.e1=Entry(window,textvariable=self.title_text)
        self.e1.grid(row=2,column=1)
        

        self.description_text=StringVar()
        self.e2=Entry(window,textvariable=self.description_text)
        self.e2.grid(row=2,column=3)
       

        self.date_text=StringVar()
        self.e3=Entry(window,textvariable=self.date_text)
        self.e3.grid(row=3,column=1)
        

        self.time_text=StringVar()
        self.e4=Entry(window,textvariable=self.time_text)
        self.e4.grid(row=4,column=1)
        

        self.status_text=StringVar()
        self.e5=Entry(window,textvariable=self.status_text)
        self.e5.grid(row=3,column=3)
        

        self.list1=Listbox(window, height=6,width=35)
        self.list1.grid(row=5,column=0,rowspan=6,columnspan=2)

        self.list1.bind('<<ListboxSelect>>',self.get_selected_row)

     
    def get_selected_row(self,event):
        if len(self.list1.curselection())>0:
            index=self.list1.curselection()[0]
            self.selected_tuple=self.list1.get(index)
            self.e1.delete(0,END)
            self.e1.insert(END,self.selected_tuple[1])
            self.e2.delete(0,END)
            self.e2.insert(END,self.selected_tuple[2])
            self.e3.delete(0,tk.END)
            self.e3.insert(END,time.acstime(),self.selected_tuple[3])
            self.e4.delete(0,END)
            self.e4.insert(END,self.selected_tuple[4])
            self.e5.delete(0,END)
            self.e5.insert(END,self.selected_tuple[5])

    def view_rem(self):
        self.list1.delete(0,END)
        for row in database.view():
            self.list1.insert(END,row)

    def add_rem(self):
        database.insert(self.title_text.get(),self.description_text.get(),self.date_text.get(),self.time_text.get(),self.status_text.get())
        self.list1.delete(0,END)
        self.list1.insert(END,(self.title_text.get(),self.description_text.get(),self.date_text.get(),self.time_text.get(),self.status_text.get()))
        mbox.showinfo("Message", "SUCCESSFULLY ADDED")
        self.list1.delete(0,END)
        for row in database.view():
            self.list1.insert(END,row)
        self.e1.delete(0,END)
        self.e2.delete(0,END)
        self.e3.delete(0,END)
        self.e4.delete(0,END)
        self.e5.delete(0,END)


    def delete_rem(self):
        database.delete(self.selected_tuple[0])
        mbox.showinfo("Message", "SUCCESSFULLY DELETED")
        self.list1.delete(0,END)
        for row in database.view():
            self.list1.insert(END,row)
        self.e1.delete(0,END)
        self.e2.delete(0,END)
        self.e3.delete(0,END)
        self.e4.delete(0,END)
        self.e5.delete(0,END)

    def update_rem(self):
        database.update(self.selected_tuple[0],self.title_text.get(),self.description_text.get(),self.date_text.get(),self.time_text.get(),self.status_text.get())
        mbox.showinfo("Message", "SUCCESSFULLY UPDATED")
        self.list1.delete(0,END)
        for row in database.view():
            self.list1.insert(END,row)
        self.e1.delete(0,END)
        self.e2.delete(0,END)
        self.e3.delete(0,END)
        self.e4.delete(0,END)
        self.e5.delete(0,END)
   # def dt_ins():
    #    e.delete(0, tk.END)
     #   e.insert(0, time.asctime())
#root = tk.Tk()
#root.title("time test")
#root.geometry('240x60+200+200')
#e = tk.Entry(root)
#b = tk.Button(root, text="Test!", command=dt_ins)
#e.pack(fill= tk.BOTH, expand = tk.YES)
#b.pack()

window=Tk()
Window(window)
window.mainloop()

