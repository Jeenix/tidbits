from tkinter import *
def main():


    def addnumbers():
        val1 = float(value1.get())
        val2 = float(value2.get())
        answer = val1 + val2
        solution = value1.get() + ' added to ' + value2.get()
        output_label.configure(text=str(solution) + ' is : {:.1f}'.format(answer))
        value1.delete(0, END)
        value2.delete(0, END)

    def subnumbers():
        val1 = float(value1.get())
        val2 = float(value2.get())
        answer = val1 - val2
        solution = value1.get() + ' subtracted from ' + value2.get()
        output_label.configure(text=str(solution) + ' is : {:.1f}'.format(answer))
        value1.delete(0, END)
        value2.delete(0, END)

    def multinumbers():
        val1 = float(value1.get())
        val2 = float(value2.get())
        answer = val1 * val2
        solution = value1.get() + ' multiplied by ' + value2.get()
        output_label.configure(text=str(solution) + ' is : {:.1f}'.format(answer))
        value1.delete(0, END)
        value2.delete(0, END)

    def divnumbers():
        val1 = float(value1.get())
        val2 = float(value2.get())
        answer = val1 / val2
        solution = value1.get() +' divided by ' + value2.get()
        output_label.configure(text= str(solution) + ' is : {:.1f}'.format(answer))
        value1.delete(0, END)
        value2.delete(0, END)

    root = Tk()
    root.title("Hello Python!")
    root.geometry("300x200")
    '''
    widgets are added here
    '''
    Label(text="Calculator").grid()
    Label(text="First Number").grid(column=0, row=1)

    value1 = Entry(text="First Number")
    value1.grid(column=1, row=1, columnspan=4)
    Label(text="Second Number").grid(column=0, row=2)

    value2 = Entry(text="Second Number")
    value2.grid(column=1, row=2, columnspan=4)

    Button(text="Add", command=addnumbers).grid(column=1, row=3)
    Button(text="Sub", command=subnumbers).grid(column=2, row=3)
    Button(text="Multi", command=multinumbers).grid(column=3, row=3)
    Button(text="Div", command=divnumbers).grid(column=4, row=3)

    Label(text="Result").grid(column=0, row=4)

    output_label = Label(font=('Verdana', 16))
    output_label.grid(column=0, row=5, columnspan=10)

    Button(text="Quit", command=root.destroy).grid(column=1, row=6)
    mainloop()


if __name__ == '__main__':
    main()
