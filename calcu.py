import tkinter as tk


import tkinter.ttk as ttk

window=tk.Tk()
window.geometry("500x300")
txt=ttk.Entry(width=35)
txt.grid(row=0,column=0,columnspan=3)

def one():
    chk()
    txt.insert(tk.END,'1')
def two():
    chk()
    txt.insert(tk.END,'2')
def three():
    chk()
    txt.insert(tk.END,'3')
def zero():
    chk()
    txt.insert(tk.END,'0')
    
  
def minus():
    op()
    txt.insert(tk.END,'-')
def plus():
    op()
    txt.insert(tk.END,'+')
def eq():
    a=txt.get()
    ans=eval(a)
    txt.delete(0,tk.END)
    txt.insert(tk.END,ans)

def op():
    a=txt.get()
    
    if a[-1] in '+-*/':
        print(',,,,,,,,,,,,,,,')
        txt.delete(len(a)-1)   
        
def chk():
    n=txt.get()
    if len(n)==1 and n[0]=='0':
        txt.delete(0,tk.END)          

btn1=ttk.Button(text="1",command=one)
btn1.grid(row=2,column=0)
btn2=ttk.Button(text="2",command=two)
btn2.grid(row=2,column=1)
btn3=ttk.Button(text="3",command=three)
btn3.grid(row=2,column=2)
btn0=ttk.Button(text="0",command=zero)
btn0.grid(row=4,column=1)
btnm=ttk.Button(text="-",command=minus)
btnm.grid(row=4,column=2)
btnp=ttk.Button(text="+",command=plus)
btnp.grid(row=3,column=0)
btne=ttk.Button(text="=",command=eq)
btne.grid(row=3,column=1)



window.mainloop()