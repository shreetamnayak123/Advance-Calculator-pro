
import tkinter as tk
from tkinter import ttk
import math

root = tk.Tk()
root.title("Advanced Calculator")
root.geometry("700x800")

expression = ""
history = []
dark = False
equation = tk.StringVar()

def press(v):
    global expression
    expression += str(v)
    equation.set(expression)

def clear():
    global expression
    expression = ""
    equation.set("")

def backspace():
    global expression
    expression = expression[:-1]
    equation.set(expression)

def equalpress():
    global expression
    try:
        result = str(eval(expression))
        history.append(f"{expression} = {result}")
        history_box.insert(tk.END, history[-1])
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""

def scientific(op):
    try:
        value = float(equation.get())
        funcs = {
            "sin": math.sin(math.radians(value)),
            "cos": math.cos(math.radians(value)),
            "tan": math.tan(math.radians(value)),
            "sqrt": math.sqrt(value),
            "log": math.log10(value),
            "square": value**2,
            "cube": value**3
        }
        equation.set(str(funcs[op]))
    except:
        equation.set("Error")

def convert_length():
    try:
        v = float(length_entry.get())
        unit = length_unit.get()
        factors = {"mm":0.001,"cm":0.01,"m":1,"km":1000}
        length_result.config(text=f"{v*factors[unit]} m")
    except:
        length_result.config(text="Invalid")

def convert_weight():
    try:
        v = float(weight_entry.get())
        unit = weight_unit.get()
        factors = {"mg":0.001,"g":1,"kg":1000}
        weight_result.config(text=f"{v*factors[unit]} g")
    except:
        weight_result.config(text="Invalid")

def bmi():
    try:
        w = float(weight_bmi.get())
        h = float(height_bmi.get())/100
        b = w/(h*h)
        bmi_result.config(text=f"BMI: {b:.2f}")
    except:
        bmi_result.config(text="Invalid")

def currency():
    try:
        amt = float(currency_entry.get())
        cur = currency_var.get()
        rates = {"INR":1,"USD":83,"EUR":90,"GBP":105}
        currency_result.config(text=f"{amt*rates[cur]:.2f} INR")
    except:
        currency_result.config(text="Invalid")

def toggle_dark():
    global dark
    dark = not dark
    bg = "black" if dark else "white"
    fg = "white" if dark else "black"
    root.configure(bg=bg)
    for w in root.winfo_children():
        try:
            w.configure(bg=bg, fg=fg)
        except:
            pass

entry = tk.Entry(root,textvariable=equation,font=("Arial",20),justify="right")
entry.pack(fill="x",padx=5,pady=5)

frame = tk.Frame(root)
frame.pack()

buttons = [
['7','8','9','/'],
['4','5','6','*'],
['1','2','3','-'],
['0','.','=','+']
]

for r,row in enumerate(buttons):
    for c,t in enumerate(row):
        cmd = equalpress if t=="=" else lambda x=t: press(x)
        tk.Button(frame,text=t,width=5,height=2,command=cmd).grid(row=r,column=c)

tk.Button(frame,text="C",command=clear).grid(row=4,column=0)
tk.Button(frame,text="⌫",command=backspace).grid(row=4,column=1)
tk.Button(frame,text="Dark",command=toggle_dark).grid(row=4,column=2,columnspan=2)

sci = tk.LabelFrame(root,text="Scientific")
sci.pack(fill="x",padx=5,pady=5)

for i,op in enumerate(["sin","cos","tan","sqrt","log","square","cube"]):
    tk.Button(sci,text=op,command=lambda o=op: scientific(o)).grid(row=0,column=i)

tk.Label(root,text="History").pack()
history_box = tk.Listbox(root,height=6)
history_box.pack(fill="x")

lf = tk.LabelFrame(root,text="Length Converter")
lf.pack(fill="x")
length_entry = tk.Entry(lf); length_entry.pack(side="left")
length_unit = tk.StringVar(value="cm")
ttk.Combobox(lf,textvariable=length_unit,values=["mm","cm","m","km"],width=5).pack(side="left")
tk.Button(lf,text="Convert",command=convert_length).pack(side="left")
length_result = tk.Label(lf,text="0 m"); length_result.pack(side="left")

wf = tk.LabelFrame(root,text="Weight Converter")
wf.pack(fill="x")
weight_entry = tk.Entry(wf); weight_entry.pack(side="left")
weight_unit = tk.StringVar(value="g")
ttk.Combobox(wf,textvariable=weight_unit,values=["mg","g","kg"],width=5).pack(side="left")
tk.Button(wf,text="Convert",command=convert_weight).pack(side="left")
weight_result = tk.Label(wf,text="0 g"); weight_result.pack(side="left")

bf = tk.LabelFrame(root,text="BMI Calculator")
bf.pack(fill="x")
weight_bmi = tk.Entry(bf,width=8)
weight_bmi.pack(side="left")
height_bmi = tk.Entry(bf,width=8)
height_bmi.pack(side="left")
tk.Button(bf,text="BMI",command=bmi).pack(side="left")
bmi_result = tk.Label(bf,text="")
bmi_result.pack(side="left")

cf = tk.LabelFrame(root,text="Offline Currency Converter")
cf.pack(fill="x")
currency_entry = tk.Entry(cf)
currency_entry.pack(side="left")
currency_var = tk.StringVar(value="USD")
ttk.Combobox(cf,textvariable=currency_var,values=["USD","EUR","GBP"],width=5).pack(side="left")
tk.Button(cf,text="Convert",command=currency).pack(side="left")
currency_result = tk.Label(cf,text="")
currency_result.pack(side="left")

root.mainloop()
