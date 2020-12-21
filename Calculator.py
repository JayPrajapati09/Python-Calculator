from tkinter import *
import tkinter.messagebox as tmsg


def show(event):
    text = event.widget.cget("text")
    global press, op, n1, n2, res
    if text == "=":
        if len(display.get()) == 0:
            display.set("ENTER NUMBER FIRST")
        else:
            op = ""
            res = 0
            str = display.get()

            if "+" in str: op = "+"
            if "-" in str: op = "-"
            if "*" in str: op = "*"
            if "/" in str: op = "/"
            if "%" in str: op = "%"
            if "^" in str: op = "^"

            str1 = str.split(f"{op}")
            n1 = float(str1[0])
            n2 = float(str1[1])
        if op == "/" and n2 == 0:
            display.set("INFINITY")
            entry.update()
        else:
            if op == "+": res = n1 + n2
            elif op == "-": res = n1 - n2
            elif op == "*": res = n1 * n2
            elif op == "/": res = n1 / n2
            elif op == "%": res = n1 % n2
            elif op == "^": res = int(n1) ** int(n2)

            if tset == 0:
                res = int(res)

            display.set(res)
            entry.update()

    elif text == "C":
        text1 = display.get()
        len1 = len(text1) - 1
        display.set(text1[0: len1])
        entry.update()

    elif text == "CE":
        press = 1
        display.set("")
        entry.update()
    elif text == "+" or text == "-" or text == "*" or text == "/" or text == "%":
        if len(display.get()) == 0:
            display.set("ENTER NUMBER FIRST")
        elif press == 2:
            display.set("INVALID EXPRESSION")
        else:
            display.set(display.get() + text)
            press += 1
        entry.update()
    else:
        display.set(display.get() + text)
        entry.update()


def extra(event):
    text = event.widget.cget("text")
    global press
    if text == "Create By":
        tmsg.showinfo("Created By", "Jay Prajapati")
    elif text == "Day" or text == "Night":
        if text == "Day":
            root.configure(bg="white")
        else:
            root.configure(bg="black")
        root.update()
    elif text == "Int" or text == "Float":
        global tset
        if text == "Int":
            tset = 0
        else:
            tset = 1
    if text == "Power" or text == "Factorial":
        if len(display.get()) == 0:
            display.set("ENTER NUMBER FIRST")
        elif press == 2:
            display.set("INVALID EXPRESSION")
        else:
            if text == "Power":
                display.set(display.get() + "^")
                entry.update()
            elif text == "Factorial":
                f = int(display.get())
                fact = 1
                if f == 0 or f == 1:
                    fact = 1
                else:
                    for i in range(1, f):
                        fact = fact + fact * i
                display.set(fact)
                entry.update()
            press += 1


root = Tk()
root.title("Calculator")
root.wm_iconbitmap("cal.ico")
root.height = 400
root.width = 450
root.geometry(f"{root.width}x{root.height}")
root.configure(background="white")
tset = 0
press = IntVar()
press = 1
op = StringVar()
n1 = IntVar()
n2 = IntVar()
res = DoubleVar()
# ENTRY
display = StringVar()
entry = Entry(root, textvariable=display, relief=SOLID, font="lucidaconsole 20 bold", borderwidth=3)
entry.place(x=5, y=10, width=440, height=80)

# BUTTONS

btn = ["0", "00", ".", "=", "1", "2", "3", "+", "4", "5", "6", "-", "7", "8", "9", "*", "CE", "C", "%", "/"]
counter = 0
bn = []
for y1 in range(340, 90, -60):
    for x1 in range(5, 340, 85):
        if counter in [3, 7, 11, 15, 19]:
            button = Button(root, text=str(btn[counter]), relief=SOLID, font="lucidaconsole 18 bold", borderwidth=2)
            button.place(x=x1 + 10, y=y1, width=80, height=55)
        else:
            button = Button(root, text=str(btn[counter]), relief=SOLID, font="lucidaconsole 12 bold", borderwidth=2)
            button.place(x=x1, y=y1, width=80, height=55)
        button.bind('<Button-1>', show)

        counter += 1

elist = ["Create By", "", "", "Power", "Factorial"]
t11 = ["1", "Day", "Int"]
t22 = ["2", "Night", "Float"]
ecounter = 0
ebutton = Button(root)
for y11 in range(100, 400, 60):

    if ecounter == 1 or ecounter == 2:
        ebutton = Button(root, text=str(t11[ecounter]), relief=SOLID, borderwidth=1)
        ebutton.place(x=355, y=y11, width=45, height=55)
        ebutton.bind('<Button-1>', extra)
        ebutton = Button(root, text=str(t22[ecounter]), relief=SOLID, borderwidth=1)
        ebutton.place(x=400, y=y11, width=45, height=55)
    else:
        ebutton = Button(root, text=str(elist[ecounter]), relief=SOLID, borderwidth=2)
        ebutton.place(x=355, y=y11, width=90, height=55)
    ebutton.bind('<Button-1>', extra)
    ecounter += 1

root.mainloop()
