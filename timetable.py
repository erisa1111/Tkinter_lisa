import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter import simpledialog
import csv
from tkinter import filedialog



class Courses():

    def __init__(self, root):
        FilePathLbl = Label(root, width=15)
        FilePathLbl.config(text="Provide data path", bg="white")
        FilePathLbl.grid(row=0, column=0, padx=(5, 10), pady=(20, 0))

        self.PathEntry = Entry(root)
        self.PathEntry.grid(row=0, column=1, padx=(0, 0), pady=(20, 0), columnspan=2,
                            sticky=W + E)

        YrLbl = Label(root, width=15)
        YrLbl.config(text="Year", bg="white")
        YrLbl.grid(row=1, column=0, padx=(5, 10), pady=(20, 0), sticky=W + E)
        n = tk.StringVar()
        self.YrBox = ttk.Combobox(root, width=5, textvariable=n)
        self.YrBox['values'] = ('1', '2', '3', '4', '5')
        self.YrBox.grid(column=1, row=1, padx=(5, 10), pady=(20, 0), sticky=W + E)
        self.YrBox.current()

        DepLbl = Label(root)
        DepLbl.config(text="Department", bg="white")
        DepLbl.grid(row=1, column=3, padx=(5, 10), pady=(20, 0), sticky=W + E)

        self.DpEntry = Entry(root)
        self.DpEntry.grid(row=1, column=4, padx=(5, 10), pady=(20, 0), sticky=W)

        DspBtn = Button(root, command=self.enter_file_dir)
        DspBtn.config(text="Display", bg="white")
        DspBtn.grid(row=2, column=0, sticky=E, padx=(0, 10), pady=(50, 0))

        ClrBtn = Button(root, command=self.delete)
        ClrBtn.config(text="Clear", bg="white")
        ClrBtn.grid(row=2, column=1, sticky=W + E, padx=(0, 10), pady=(50, 0))

        SvBtn = Button(root, command=self.save_file)
        SvBtn.config(text="Save", bg="white" )
        SvBtn.grid(row=2, column=2, sticky=W + E, padx=(0, 10), pady=(50, 0))

        SelCrsLbl = Label(root)
        SelCrsLbl.config(text="Selected courses: ", bg="white")
        SelCrsLbl.grid(row=5, column=0, columnspan=5, padx=(10, 0), pady=(50, 0), ipadx=5, sticky=W)

        self.SelCrsLbx = Listbox(root, width=20)
        self.SelCrsLbx.grid(row=6, column=0, columnspan=5, padx=(10, 0), pady=(15, 0), sticky=W)
       



        CrsLbl = Label(root)
        CrsLbl.config(text="Courses", bg="white")
        CrsLbl.grid(row=5, column=2, columnspan=10, padx=(0, 0), pady=(50, 0), sticky=W + E)

        self.CrsLbx = Listbox(root, width=50)
        self.CrsLbx.grid(row=6, column=2, columnspan=10, padx=(0, 0), pady=(15, 0), sticky=W + E)
        self.CrsLbx.bind("<Double-1>", self.select_item)

        self.splitlist = []
        self.tosave = []


    def enter_file_dir(self):
        self.CrsLbx.delete(0,END)
        filepath = self.PathEntry.get()
        try: 
            file_ = open(str(filepath), 'r', encoding="utf8", errors="ignore")
            #file_ = open(str("C:\\Users\\DION\\Desktop\\sampledata (1).csv"), 'r', encoding="utf8", errors="ignore")
        except FileNotFoundError as f:
            messagebox.showerror(title=None, message='File Path not selected')
        else:
            fileread = file_.read()
            reader = csv.reader(file_)
            data = list(reader)

        

       
            for i in fileread.splitlines():
                if self.DpEntry.get():
                    if i.startswith(str(self.DpEntry.get())):
                        isplit = i.split(' ')
                        yearstr = str(self.YrBox.current()+1)
                        
                        if isplit[1][0] == yearstr:
                            self.CrsLbx.insert(END, i)
                            self.tosave.append(i)
                            print(self.tosave)
                        elif yearstr == '0':
                            self.CrsLbx.insert(END, i)
                else:
                    messagebox.showerror(title=None, message='Please select a departament')
                    break
                        

        

            for i in self.CrsLbx.curselection():
                print(self.CrsLbx.get(i))





    def delete(self):
        self.CrsLbx.delete(0,END)
        self.DpEntry.delete(0,END)
        self.PathEntry.delete(0,END)
        self.YrBox.delete(0,END)
        self.SelCrsLbx.delete(0,END)
        self.splitlist= []

    def select_item(self, event):
        selection = self.CrsLbx.curselection()
        

        for i in selection:
            self.f_selected = event.widget.get(i)
            splitf = self.f_selected.split(',')
            
            if (splitf[0]) not in self.splitlist: 
                
                if len(self.splitlist) < 6:
                    
                    self.SelCrsLbx.insert(END, (f"Added {splitf[0]}"))
                    self.splitlist.append(splitf[0])
                    self.tosave.append(self.f_selected)
                else:
                    messagebox.showerror(title=None, message='Only 6 courses allowed')
            else:
                messagebox.showerror(title=None, message='Cannot add twice')




    def save_file(self):
        saver = filedialog.asksaveasfile(defaultextension='.txt',filetypes=[    
                                            ('Text file', '.txt'),
                                            ('Html file', '.html'),
                                            ('All files', '.*')
        
        ])    
        
        for i in self.tosave:
            saver.write(i+'\n')

    
    
 

    
# C:\Users\DION\Desktop\sampledata (1).csv
# C:\Users\BIT Admin\Downloads\sampledata (1).csv

root = Tk()
root.resizable(0, 0)  
root.geometry("520x500+400+200") 
root.wm_title(" " * 50 + "Timetable") 
root.configure(background='#856ff8')  
Courses(root)




root.mainloop()



