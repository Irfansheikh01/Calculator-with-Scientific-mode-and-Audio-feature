from tkinter import*
from tkinter import ttk


root=Tk()
root.title('checkbutton')
root.geometry('345x345')

combodict={'dettol':'20',
           'cynthol':'15',
            'Lux':'30',
           'dove':'40'

            }
comboval=IntVar()
def callfunct(event):
    b = event.widget
    text = combo.get()
    print(text)
    global comboval
    for i in combodict:
        #print(i)
        if i==text:

            comboval=2 * int(combodict.get(i))
            print(comboval)
combo=ttk.Combobox(root,
                    values=['dettol',
                            'cynthol',
                            'Lux'])
#for i in combodict:
#    combo.insert(combodict[i])
#print(dict(combo))
combo.pack()
combo.current()
#print(combo.current(0),combo.get())
combo.bind("<<ComboboxSelected>>",callfunct)
root.mainloop()
