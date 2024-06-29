from tkinter import *

def calculate():
    tens = int(entry.get()) * 30 if entry.get() else 0
    sixes = int(entry2.get()) * 30 if entry2.get() else 0
    fours = int(entry3.get()) * 20 if entry3.get() else 0
    quarterInch = int(entry4.get()) * 45 if entry4.get() else 0
    adjustments = int(entry5.get()) * 30 if entry5.get() else 0

    totalTime = (tens + sixes + fours + quarterInch + adjustments) / 60
    result_label.config(text=f"Total Time: {totalTime:.2f} Hour(s)")

def focus_next_event(event):
    if event.keysym == "Down":
        event.widget.tk_focusNext().focus()
    elif event.keysym == "Up":
        event.widget.tk_focusPrev().focus()
    return "break"

root= Tk()

root.title("Time-Calculator")
root.geometry("400x400")

root.grid_columnconfigure(1,weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_rowconfigure(0,minsize=40)

result_label = Label(root, text="Total Time: 0.00 Hour(s)",font=20)
result_label.grid(row=0,column=0,columnspan=2,padx=(80,0),pady=(40,20))

label = Label(root, text="10000 FT")
label.grid(row=1,column=0,padx=(40,5),pady=10,sticky="e")

entry = Entry(root)
entry.grid(row=1,column=1,padx=(5,40),pady=10,sticky="w")
entry.bind("<Down>", focus_next_event)
entry.bind("<Up>", focus_next_event)

label2 = Label(root, text="6000 FT")
label2.grid(row=2,column=0,padx=(40,5),pady=5,sticky="e")

entry2 = Entry(root)
entry2.grid(row=2,column=1,padx=(5,40),pady=10,sticky="w")
entry2.bind("<Down>", focus_next_event)
entry2.bind("<Up>", focus_next_event)

label3 = Label(root, text="4000 FT")
label3.grid(row=3,column=0,padx=(40,5),pady=5,sticky="e")

entry3 = Entry(root)
entry3.grid(row=3,column=1,padx=(5,40),pady=10,sticky="w")
entry3.bind("<Down>", focus_next_event)
entry3.bind("<Up>", focus_next_event)

label4 = Label(root, text="6.35mm")
label4.grid(row=4,column=0,padx=(40,5),pady=5,sticky="e")

entry4 = Entry(root)
entry4.grid(row=4,column=1,padx=(5,40),pady=10,sticky="w")
entry4.bind("<Down>", focus_next_event)
entry4.bind("<Up>", focus_next_event)

label5 = Label(root,text="Core Color Changes")
label5.grid(row=5,column=0,padx=(40,5),pady=5,sticky="e")

entry5 = Entry(root)
entry5.grid(row=5,column=1,padx=(5,40),pady=10,sticky="w")
entry5.bind("<Down>", focus_next_event)
entry5.bind("<Up>", focus_next_event)

button = Button(root,text="Calculate",width=10,command=calculate)
button.grid(row=6,column=0,columnspan=2,padx=(80,0),pady=20)

root.mainloop()