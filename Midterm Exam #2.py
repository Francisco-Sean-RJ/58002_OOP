import tkinter as tk

def show_full_name():
    first_name = entry_first_name.get()
    middle_name = entry_middle_name.get()
    last_name = entry_last_name.get()
    full_name = "%s, %s %s" % (last_name, middle_name, first_name)
    entry_full_name.delete(0, tk.END)
    entry_full_name.insert(0, full_name)

def clear_all():
    entry_first_name.delete(0, tk.END)
    entry_middle_name.delete(0, tk.END)
    entry_last_name.delete(0, tk.END)
    entry_full_name.delete(0, tk.END)

window = tk.Tk()
window.title("My Full Name")
window.configure(background="#FFFFFF")
label_first_name = tk.Label(window, text="Enter Given Name:", font=("Verdana", 12), foreground="red")
label_middle_name = tk.Label(window, text="Enter Middle Name:", font=("Verdana", 12), foreground="red")
label_last_name = tk.Label(window, text="Enter Last Name:", font=("Verdana", 12), foreground="red")
label_text = tk.StringVar(value="My Full Name")
entry_first_name = tk.Entry(window, font=("Verdana", 12))
entry_middle_name = tk.Entry(window, font=("Verdana", 12))
entry_last_name = tk.Entry(window, font=("Verdana", 12))
entry_full_name = tk.Entry(window, font=("Verdana", 12), foreground="red")

button_show = tk.Button(window, text="Show Full Name", font=("Verdana", 12), command=show_full_name, bd=0, bg="#FFFFFF", activebackground="#FFFFFF")
button_clear = tk.Button(window, text="Clear All", font=("Verdana", 12), command=clear_all, bd=0, bg="#FFFFFF", activebackground="#FFFFFF")

label_first_name.grid(row=1, column=0, padx=10, pady=10, sticky="W")
entry_first_name.grid(row=1, column=1, padx=10, pady=10)

label_middle_name.grid(row=2, column=0, padx=10, pady=10, sticky="W")
entry_middle_name.grid(row=2, column=1, padx=10, pady=10)

label_last_name.grid(row=3, column=0, padx=10, pady=10, sticky="W")
entry_last_name.grid(row=3, column=1, padx=10, pady=10)

entry_full_name.grid(row=4, column=1, padx=10, pady=10)

button_show.grid(row=6, column=0, columnspan=2, pady=10)
button_clear.grid(row=7, column=0, columnspan=2, pady=10)

label_title = tk.Label(window, text="My Full Name", font=("Verdana", 16, "bold"), foreground="red")
label_title.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

label_full_name = tk.Label(window, textvariable=label_text, font=("Verdana", 12, "bold"), foreground="red")
label_full_name.grid(row=4, column=0, padx=10, pady=10, sticky="W"+"E"+"N"+"S")

window.mainloop()
