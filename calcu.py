from tkinter import *

def btnClick(numbers):
    global operator
    operator=operator + str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator=""
    text_Input.set("")

def btnEqualsInput():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operator=""

cal = Tk()
cal.title("Calculator")
operator=""
text_Input =StringVar()

textDisplay= Entry(cal,font=("",20),textvariable=text_Input,justify='right').grid(columnspan=4)
btn7=Button(cal,padx=16,pady=16,fg="black",font=("",20),text="7",command=lambda:btnClick(7)).grid(row=1,column=0)
btn8=Button(cal,padx=16,pady=16,fg="black",font=("",20),text="8",command=lambda:btnClick(8)).grid(row=1,column=1)
btn9=Button(cal,padx=16,pady=16,fg="black",font=("",20),text="9",command=lambda:btnClick(9)).grid(row=1,column=2)
Addition=Button(cal,padx=16,pady=16,fg="black",font=("",20),text="+",command=lambda:btnClick("+")).grid(row=1,column=3)

btn4=Button(cal,padx=16,pady=16,fg="black",font=("",20),text="4",command=lambda:btnClick(4)).grid(row=2,column=0)
btn5=Button(cal,padx=16,pady=16,fg="black",font=("",20),text="5",command=lambda:btnClick(5)).grid(row=2,column=1)
btn6=Button(cal,padx=16,pady=16,fg="black",font=("",20),text="6",command=lambda:btnClick(6)).grid(row=2,column=2)
Subtraction=Button(cal,padx=16,pady=16,fg="black",font=("",20),text="-",command=lambda:btnClick("-")).grid(row=2,column=3)

btn1=Button(cal,padx=16,pady=16,fg="black",font=("",20),text="1",command=lambda:btnClick(1)).grid(row=3,column=0)
btn2=Button(cal,padx=16,pady=16,fg="black",font=("",20),text="2",command=lambda:btnClick(2)).grid(row=3,column=1)
btn3=Button(cal,padx=16,pady=16,fg="black",font=("",20),text="3",command=lambda:btnClick(3)).grid(row=3,column=2)
multiply=Button(cal,padx=16,pady=16,fg="black",font=("",20),text="*",command=lambda:btnClick("*")).grid(row=3,column=3)

btn0=Button(cal,padx=16,pady=16,fg="black",font=("",20),text="0",command=lambda:btnClick(0)).grid(row=4,column=0)
btnClear=Button(cal,padx=16,pady=16,fg="black",font=("",20),text="C",command=btnClearDisplay).grid(row=4,column=1)
btnEquals=Button(cal,padx=16,pady=16,fg="black",font=("",20),text="=",command=btnEqualsInput).grid(row=4,column=2)
Division=Button(cal,padx=16,pady=16,fg="black",font=("",20),text="/",command=lambda:btnClick("/")).grid(row=4,column=3)

cal.mainloop()




