from tkinter import*
import math

root=Tk()
root.title('Калькулятор')
root.resizable(0,0)

def number_button(num):
    text1.insert(END,str(num))

def clear1():
    text1.delete(0,END)

def clear2():
    n=text1.get()
    text1.delete(len(n)-1)

def sqrt():
    s=float(text1.get())
    f=math.sqrt(s)
    clear1()
    text1.insert(0,f)

def factorial():
    s=int(text1.get())
    f=1
    for i in range(1,s+1):
        f*=i
    clear1()
    text1.insert(0,f)

def iquel():
    s=text1.get()
    try:
        result=eval(s)
        clear1()
        text1.insert(0,result)
    except Exception:
        clear1()
        text1.insert(0,'Error!')

fr1=Frame(root)
fr1.pack(side=TOP,pady=5)

fr2=Frame(root)
fr2.pack(side=LEFT,anchor=N,pady=5)

text1=Entry(fr1,width=16, font='Arial 30', justify='right',bd=5,insertwidth=-1)
text1.pack(side=RIGHT,anchor=N)

#1
b_b = Button(fr2, text='n!', width=3, bd=0,  fg='red', font='Arial 30',command=factorial)
b_b.grid(row=1, column=1)

b_ce = Button(fr2, text='CE', width=3, bd=0, fg='red', font='Arial 30',command=clear1)
b_ce.grid(row=1, column=2)

b_c = Button(fr2, text='С', width=3, bd=0, fg='red', font='Arial 30',command=clear2)
b_c.grid(row=1, column=3)

b_sqrt = Button(fr2, text='√', width=3, bd=0, fg='red', font='Arial 30',command=sqrt)
b_sqrt.grid(row=1, column=4)

b_p_m = Button(fr2, text='^', width=3, bd=0, fg='red', font='Arial 30',command=lambda:number_button('**'))
b_p_m.grid(row=1, column=5)

#2
b_7 = Button(fr2, text='7', width=3, bd=0, fg='blue', font='Arial 30',command=lambda:number_button(7))
b_7.grid(row=2, column=1)

b_8 = Button(fr2, text='8', width=3, bd=0, fg='blue', font='Arial 30',command=lambda:number_button(8))
b_8.grid(row=2, column=2)

b_9 = Button(fr2, text='9', width=3, bd=0, fg='blue', font='Arial 30',command=lambda:number_button(9))
b_9.grid(row=2, column=3)

b_slash = Button(fr2, text='/', width=3, bd=0, fg='red', font='Arial 30',command=lambda:number_button('/'))
b_slash.grid(row=2, column=4)

b_skot = Button(fr2, text='(', width=3, bd=0, fg='red', font='Arial 30',command=lambda:number_button('('))
b_skot.grid(row=2, column=5)

#3
b_4 = Button(fr2, text='4', width=3, bd=0,  fg='blue', font='Arial 30',command=lambda:number_button(4))
b_4.grid(row=3, column=1)

b_5 = Button(fr2, text='5', width=3, bd=0,  fg='blue', font='Arial 30',command=lambda:number_button(5))
b_5.grid(row=3, column=2)

b_6 = Button(fr2, text='6', width=3, bd=0, fg='blue', font='Arial 30',command=lambda:number_button(6))
b_6.grid(row=3, column=3)

b_star = Button(fr2, text='*', width=3, bd=0, fg='red', font='Arial 30',command=lambda:number_button('*'))
b_star.grid(row=3, column=4)

b_skza = Button(fr2, text=')', width=3, bd=0, fg='red', font='Arial 30',command=lambda:number_button(')'))
b_skza.grid(row=3, column=5)

#4
b_1 = Button(fr2, text='1', width=3, bd=0, fg='blue', font='Arial 30',command=lambda:number_button(1))
b_1.grid(row=4, column=1)

b_2 = Button(fr2, text='2', width=3, bd=0, fg='blue', font='Arial 30',command=lambda:number_button(2))
b_2.grid(row=4, column=2)

b_3 = Button(fr2, text='3', width=3, bd=0, fg='blue', font='Arial 30',command=lambda:number_button(3))
b_3.grid(row=4, column=3)

b_minus = Button(fr2, text='-', width=3, bd=0, fg='red', font='Arial 30',command=lambda:number_button('-'))
b_minus.grid(row=4, column=4)

b_ravno = Button(fr2, text='=',height=3, width=3, bd=0, fg='red', font='Arial 30',command=iquel)
b_ravno.grid(row=4, rowspan=2, column=5)


#5
b_0 = Button(fr2, text='0', width=7, bd=0, fg='blue', font='Arial 30',command=lambda:number_button(0))
b_0.grid(row=5, column=1,columnspan=2)

b_t = Button(fr2, text='.', width=3, bd=0, fg='red', font='Arial 30',command=lambda:number_button('.'))
b_t.grid(row=5, column=3)

b_p = Button(fr2, text='+', width=3, bd=0, fg='red', font='Arial 30',command=lambda:number_button('+'))
b_p.grid(row=5, column=4)




root.mainloop()

