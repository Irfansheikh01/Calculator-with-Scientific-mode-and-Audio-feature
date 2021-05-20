from tkinter import *
from tkinter.messagebox import *
import math as m
from audio_helper import PlayAudio
import threading
# some useful variables
font=('verdana',20,'bold')
ob = PlayAudio()


#important function
def enable_voice():
    global sound,check
    if check:
        sound=1
        check=False
    else:
        sound = 0
        check = True






def click_btn_function(event):

    print('Button clicked')
    b=event.widget
    text=b['text']
    print(text)


    if sound==1:
        #print("HELLO")
        t = threading.Thread(target=ob.speak,args=(text))
        t.start()

    if text =='x':
        textField.insert(END,"*")
        return




    if text == '=':
        try:
            ex = textField.get()
            ans = eval(ex)
            textField.delete(0, END)
            textField.insert(0, ans)
            print(ans)

        except Exception as e:
            print("Error..", e)
            showerror("Error", e)

        return


    textField.insert(END,text)




def all_clear():
    textField.delete(0,END)


def clear():
    ex = textField.get()
    ex = ex[0:len(ex)-1]
    textField.delete(0,END)
    textField.insert(0,ex)



# creating a window
window = Tk()
window.title('Calculator by Irfan')
window.geometry('465x455')
bg_color="lightgreen"
# picture label
#pic = PhotoImage(file='img/cal1.pic')
#headingLabel = Label(window)
#headingLabel.pack(side=TOP, pady=10,padx=10)


# heading Label
heading = Label(window, text='My Calculator', font=font, underline=0)
heading.pack(side=TOP)

# textfield
textFieldFrame = Frame(window, border=5, relief=SUNKEN,bg=bg_color)
textFieldFrame.pack(pady=10)
textField = Entry(textFieldFrame,font=font, justify=CENTER, width=21)
textField.pack(side=TOP,pady=5, fill=X, padx=5)


# Buttons

buttonFrame = Frame(window,bg=bg_color)
buttonFrame.pack(side=TOP)

# adding button
sound = IntVar()
check = True
temp = 1
for i in range(0,3):
    for j in range(0,3):
        btn=Button(buttonFrame,text=str(temp), font=font, width=5, relief=RIDGE, activebackground='orange', activeforeground='white',bg=bg_color)
        btn.grid(row=i, column=j)
        temp= temp + 1
        btn.bind('<Button-1>',click_btn_function)

zeroBtn = Button(buttonFrame,text="0", font=font, width=5, relief=RIDGE,activebackground='orange',
                            activeforeground='white',bg=bg_color)
zeroBtn.grid(row=3, column=0)

dotBtn = Button(buttonFrame,text=".", font=font, width=5, relief=RIDGE,activebackground='orange',
                        activeforeground='white',bg=bg_color)
dotBtn.grid(row=3, column=1)

equalBtn = Button(buttonFrame,text="=", font=font, width=5, relief=RIDGE,
                        activebackground='orange', activeforeground='white',bg=bg_color)
equalBtn.grid(row=3, column=2)

plusBtn = Button(buttonFrame,text="+", font=font, width=5, relief=RIDGE,
                        activebackground='orange', activeforeground='white',bg=bg_color)
plusBtn.grid(row=0, column=3)

minusBtn = Button(buttonFrame,text="-", font=font, width=5, relief=RIDGE,
                        activebackground='orange', activeforeground='white',bg=bg_color)
minusBtn.grid(row=1, column=3)

multBtn = Button(buttonFrame,text="x", font=font, width=5, relief=RIDGE,
                        activebackground='orange', activeforeground='white',bg=bg_color)
multBtn.grid(row=2, column=3)

divBtn = Button(buttonFrame,text="/", font=font, width=5, relief=RIDGE,
                        activebackground='orange', activeforeground='white',bg=bg_color)
divBtn.grid(row=3, column=3)

clearBtn = Button(buttonFrame,text="<--", font=font, width=5, relief=RIDGE,
                        activebackground='orange', activeforeground='white',command=clear,bg=bg_color)
clearBtn.grid(row=4, column=0)

commaBtn = Button(buttonFrame,text=",", font=font, width=5, relief=RIDGE,
                        activebackground='orange', activeforeground='white',bg=bg_color)
commaBtn.grid(row=4, column=1)

allClearBtn = Button(buttonFrame,text="AC", font=font, width=11, relief=RIDGE,
                        activebackground='orange',bg=bg_color, activeforeground='white',command=all_clear)
allClearBtn.grid(row=4, column=2, columnspan=2)



# Bindinng all buttons

plusBtn.bind('<Button-1>',click_btn_function)
minusBtn.bind('<Button-1>',click_btn_function)
multBtn.bind('<Button-1>',click_btn_function)
divBtn.bind('<Button-1>',click_btn_function)
zeroBtn.bind('<Button-1>',click_btn_function)
equalBtn.bind('<Button-1>',click_btn_function)
dotBtn.bind('<Button-1>',click_btn_function)
commaBtn.bind('<Button-1>',click_btn_function)



def enterClick(event):
    print('hiii')
    e = Event()
    e.widget = equalBtn
    click_btn_function(e)

textField.bind('<Return>',enterClick)




#################################################

# functions of Scientific calci
scFrame = Frame(window,pady=20)

sqrtBtn = Button(scFrame,text="√", font=font, width=5, relief=RIDGE,
                        activebackground='orange', activeforeground='white',bg=bg_color)
sqrtBtn.grid(row=0, column=0)

powBtn = Button(scFrame,text="^", font=font, width=5, relief=RIDGE,
                        activebackground='orange', activeforeground='white',bg=bg_color)
powBtn.grid(row=0, column=1)

factBtn = Button(scFrame,text="x!", font=font, width=5, relief=RIDGE,
                        activebackground='orange', activeforeground='white',bg=bg_color)
factBtn.grid(row=0, column=2)

radBtn = Button(scFrame,text="toRad", font=font, width=5, relief=RIDGE,
                        activebackground='orange', activeforeground='white',bg=bg_color)
radBtn.grid(row=0, column=3)

degBtn = Button(scFrame,text="toDeg", font=font, width=5, relief=RIDGE,
                        activebackground='orange', activeforeground='white',bg=bg_color)
degBtn.grid(row=1, column=0)

sinBtn = Button(scFrame,text="sinθ", font=font, width=5, relief=RIDGE,
                        activebackground='orange', activeforeground='white',bg=bg_color)
sinBtn.grid(row=1, column=1)

cosBtn = Button(scFrame,text="cosθ", font=font, width=5, relief=RIDGE,
                        activebackground='orange', activeforeground='white',bg=bg_color)
cosBtn.grid(row=1, column=2)

tanBtn = Button(scFrame,text="tanθ", font=font, width=5, relief=RIDGE,
                        activebackground='orange', activeforeground='white',bg=bg_color)
tanBtn.grid(row=1, column=3)





normalcal = True


def calculate_sc(event):
    print('clicked')
    btn = event.widget
    text= btn['text']
    print(text)
    ans =''
    ex = textField.get()

    if text=='toDeg' :
        print("cal degree")
        ans = str(m.degrees(float(ex)))

    elif text=='toRad':
        print("cal radian")
        ans = str(m.radians(float(ex)))

    elif text=='x!':
        print("cal factorial")
        ans = str(m.factorial(int(ex)))

    elif text=='sinθ':
        print("cal sin")
        ans = str(m.sin(m.radians(int(ex))))

    elif text=='cosθ':
        print("cal cos")
        ans = str(m.cos(m.radians(int(ex))))

    elif text=='tanθ':
        print("cal tan")
        ans = str(m.tan(m.radians(int(ex))))

    elif text=='√':
        print("cal square root")
        ans = str(m.sqrt(float(ex)))

    elif text=='^':
        print("cal power")
        base,pow = ex.split(',')
        ans = str(m.pow(int(base),int(pow)))

    textField.delete(0,END)
    textField.insert(0, ans)

def sc_click():
    global normalcal
    print('clicked')
    if normalcal:
        #sc
        buttonFrame.pack_forget()
        # add scFrame
        scFrame.pack(side=TOP)
        buttonFrame.pack(side=TOP)
        window.geometry('465x620')
        print('show sc')
        normalcal= False
    else:
        print('show normal')
        scFrame.pack_forget()
        window.geometry('465x455')
        normalcal = True

# end functions

# Binding sc buttons
sqrtBtn.bind("<Button-1>", calculate_sc)
powBtn.bind("<Button-1>", calculate_sc)
factBtn.bind("<Button-1>", calculate_sc)
radBtn.bind("<Button-1>", calculate_sc)
degBtn.bind("<Button-1>", calculate_sc)
sinBtn.bind("<Button-1>", calculate_sc)
cosBtn.bind("<Button-1>", calculate_sc)
tanBtn.bind("<Button-1>", calculate_sc)



menuFont = ('',15)
menubar = Menu(window)




mode = Menu(menubar,font=menuFont, tearoff=0)
mode.add_checkbutton(label="Scientific Calculator",command=sc_click)
mode.add_checkbutton(label="Enable voice",command=enable_voice)
#mode.add_checkbutton(label="Disable voice",command=disable_voice)
menubar.add_cascade(label="Modes", menu=mode)

window.config(menu=menubar)

window.mainloop()
