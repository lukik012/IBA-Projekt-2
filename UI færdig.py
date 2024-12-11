import tkinter as tk
import customtkinter as c
from tkinter import ttk, messagebox
import sqlite3
import numpy as np
from datetime import datetime
import time
#Start databases for login og print jobs
def initialize_database():
    con = sqlite3.connect('login.db')
    cursor = con.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS login(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL,
                   password TEXT NOT NULL
                   )''')
    con.commit()
    con.close()

def initialize_print_jobs():
    con = sqlite3.connect('print.db')
    cursor = con.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS print(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   process TEXT NOT NULL,
                   machine TEXT NOT NULL,
                   material TEXT NOT NULL,
                   cost FLOAT NOT NULL,
                   unit FLOAT NOT NULL,
                   density FLOAT NOT NULL,
                   timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                   )''')
    con.commit()
    con.close()

# Initialize both databases
initialize_database()
initialize_print_jobs()

# Funktion til at gemme login data
def save_to_database(name, password, retries=5, delay=0.1):
    for _ in range(retries):
        try:
            with sqlite3.connect("login.db") as con:
                cursor = con.cursor()
                cursor.execute("INSERT INTO login (name, password) VALUES (?, ?)", (name, password))
                con.commit()
            return True
        except sqlite3.OperationalError as e:
            if "database is locked" in str(e).lower():
                time.sleep(delay)
            else:
                raise
    return False  # Return False if the operation failed after retries

# Function to save print jobs with retry mechanism
def save_to_print_jobs(process, machine, material, cost, unit, density, retries=5, delay=0.1):
    for _ in range(retries):
        try:
            with sqlite3.connect("print.db") as con:
                cursor = con.cursor()
                timestamp = datetime.now().strftime('%d-%m-%Y %H %M %S')
                cursor.execute("INSERT INTO print (process, machine, material, cost, unit, density, timestamp) VALUES (?, ?, ?, ?, ?, ?, ?)",
                               (process, machine, material, cost, unit, density, timestamp))
                con.commit()
            return True
        except sqlite3.OperationalError as e:
            if "database is locked" in str(e).lower():
                time.sleep(delay)
            else:
                raise
    return False  # Return False if the operation failed after retries

# Material cost dictionary for 3D printing
material_cost = {
    'FDM': {
        'Ultimaker 3': {'material': 'abs', 'price_per_kg': 66.66, 'density': 1.1},
        'Fortus 360mc': {'material': 'ultem', 'price_per_unit': 343, 'density': 1.27}
    },
    'SLA': {
        'Form2_clear': {'material': 'clear resin', 'price_per_L': 149, 'density': 1.18},
        'Form2_dental': {'material': 'dental model resin', 'price_per_L': 149, 'density': 1.18},
        'ProX_950': {'material': 'accura xtreme', 'price_per_10kg': 2800, 'density': 1.18},
        'Form2_casting': {'material': 'casting resin', 'price_per_L': 299, 'density': 1.18}
    },
    'SLS': {
        'EOSINT_P800_PA2200': {'material': 'PA2200', 'price_per_kg': 67.5, 'density': 0.93},
        'EOSINT_P800_PA12': {'material': 'PA12', 'price_per_kg': 60, 'density': 1.01},
        'EOSINT_P800_ALU': {'material': 'alumide', 'price_per_kg': 50, 'density': 1.36},
    },
    'SLM': {
        'EOSm100_TI6Al4V': {'material': 'TI6Al4V', 'price_per_kg': 400, 'density': 4.43},
        'EOSm100_SSL316': {'material': 'SSL316', 'price_per_kg': 30, 'density': 8},
    },
    'DLP': {
        '3DSystems_figure4': {'material': 'Problack 10', 'price_per_kg': 250, 'density': 1.07},
    }
}

# Beregnings funktion for 3D printing omkostninger
def calculate_print_cost(printer_type, printer_model, material, amount, unit):
    type_data = material_cost.get(printer_type)
    if not type_data:
        return f"Printer type '{printer_type}' not found."

    model_data = type_data.get(printer_model)
    if not model_data:
        return f"Printer model '{printer_model}' not found for type '{printer_type}'."

    if model_data.get('material') != material.lower():
        return f"Material '{material}' not found for model '{printer_model}'."

    if unit == 'Kg' and 'price_per_kg' in model_data:
        cost = amount * model_data['price_per_kg']
    elif unit == 'L' and 'price_per_L' in model_data:
        cost = amount * model_data['price_per_L']
    elif unit == 'unit' and 'price_per_unit' in model_data:
        cost = amount * model_data['price_per_unit']
    elif unit == '10kg' and 'price_per_10kg' in model_data:
        cost = (amount / 10) * model_data['price_per_10kg']
    else:
        return "This unit is not supported."

    return f"Total price: ${cost:.2f}"

# Login user
def login_user():
    name = entry_name.get()
    password = entry_password.get()

    if name and password:
        if save_to_database(name, password):
            messagebox.showinfo("Login", f"Velkommen:\nName: {name}")
            show_menu()       
        else:
            messagebox.showerror("Error", "Name is already registered!")
    else:
        messagebox.showwarning("Error", "All fields must be filled!")

# Funktion der styrer log ud handlingen
def logout_user():
    entry_name.delete(0, tk.END)
    entry_password.delete(0, tk.END)
    # Skift til startskærmen
    # Skjul menuen og vis login-skærmen igen
    menu_frame.pack_forget()
    frame.pack(padx=10, fill="both", expand=True)  # Vis login-frame igen

def login_frame():
    menu_frame.pack_forget()
    frame_calculator.pack_forget()
    label_frame.pack(padx=10, fill="both", expand=True)
#vis 
def show_menu():
    frame.pack_forget()
    frame_calculator.pack_forget()
    menu_frame.pack(padx=10, fill="both", expand=True)

# vis 3d beregner skærm efter menu
def show_calculator_screen():
    menu_frame.pack_forget()  # Hide menu frame
    frame_calculator.pack(padx=10, pady=10, fill="both")  # beregn frame

# Back to Menu from Calculator
def back_to_menu_from_calculator():
    frame_calculator.pack_forget()  # gemmer frame
    menu_frame.pack(padx=10, fill="both", expand=True)  # viser menu

# Menu Buttons
def open_calculator():
    show_calculator_screen()

def open_history():
    show_saved_calculations()
    messagebox.showinfo("History", "Viser gemte beregninger")


#Funktion til at opdatere printer modeller alt efter hvilken printer type der er valgt
def update_models(event=None):
    printer_type = combobox_printer_type.get()
    if printer_type in material_cost:
        models = list(material_cost[printer_type].keys())
    else:
        models = []
    # Ryd printermodel-dropsdown og opdater det baseret på valgte printertype
    combobox_printer_model.config(values=models)
    combobox_printer_model.set('') #Nulstil valgt model

#Funktion til at opdatere materiale alt efter hvilken printer der er valgt
def update_materials(event=None):
    printer_type = combobox_printer_type.get()
    model = combobox_printer_model.get()
    
    # Tjek om printertypen og modellen findes i material_cost
    if printer_type in material_cost and model in material_cost[printer_type]:
        model_data = material_cost[printer_type][model]
        material = model_data['material']  # Henter materiale fra model_data
        
        # Opdater material combobox med relevante materialer
        combobox_material.config(values=[material])
        combobox_material.set('')  # Fjern tidligere valg i material
        
        # Kald update_unit, når materialer er sat
        update_unit()
    else:
        # Hvis ingen data findes for printertype og model, ryd material comboboxen
        combobox_material.config(values=[])
        combobox_material.set('')  # Ryd tidligere valg
        combobox_unit.config(values=[])  # Ryd også enheder, da der ikke er et gyldigt valg
        print("No materials found for the selected printer model")

#Funktion til at opdatere enheder alt efter hvilken printer der er valgt

def update_unit(event=None):
    selected_printer_type = combobox_printer_type.get() #Henter den valgte printertype
    selected_printer_model = combobox_printer_model.get() #Henter den valgte printermodel

    #tjekker om printertype og model findes i vores material_cost dictionary
    if selected_printer_type in material_cost and selected_printer_model in material_cost[selected_printer_type]:
        model_data = material_cost[selected_printer_type][selected_printer_model]

        unit.clear() # Tøm unit-listen før vi tilføjer flere enheder
        
        #Finder de enheder baseret på de informationer vi finder i model_data
        if 'price_per_kg' in model_data:
            unit.append('Kg')
        if 'price_per_L' in model_data:
            unit.append('L')
        if 'price_per_unit' in model_data:
            unit.append('Unit')
        if 'price_per_10kg' in model_data:
            unit.append('10Kg')

        # Opdater unit dropdown med de relevante enheder 
        combobox_unit.config(values=unit)
        combobox_unit.set('')  # Fjern tidligere valg af unit
    else:
        # Hvis der ikke er data for den valgte type eller model
        combobox_unit.config(values=[])
        combobox_unit.set('')  # Ryd tidligere valg

# Calculate and display cost in UI
def calculate_and_display_cost():
    printer_type = combobox_printer_type.get()
    printer_model = combobox_printer_model.get()
    material = combobox_material.get()
    unit = combobox_unit.get()  
    try: 
        amount = float(entry_amount.get())
        antal_emner = int(entry_antal_emner.get()) # Henter antal emner
    except ValueError:
        messagebox.showerror("Invalid input","Please enter a valid number ")
        return
    result = calculate_print_cost(printer_type, printer_model, material, amount, unit)
    print(f"Calculation result:{result}") #Debug
    #label_result.config(text=result)
    
    #Her caller vi save_calculation, for at være sikre på beregningen bliver gemt i vores db
    if "Total price" in result:
        single_cost = float(result.split("$")[1].strip())
        total_cost = single_cost * antal_emner
        label_result.config(text=f"Total cost for {antal_emner} items: ${total_cost:.2f}")

        cost_value = float(result.split("$")[1].strip())
        density = material_cost[printer_type][printer_model].get('density', 1) #Henter density fra vores dict
        save_calculation(printer_type, printer_model, material, cost_value, unit, density)
    else:
        label_result.config(text=result)
        # Gem beregnet data til senere brug
    global last_cost_data
    last_cost_data = (printer_type, printer_model, material, amount, unit, total_cost)
     #Her caller vi save_calculation, for at være sikre på beregningen bliver gemt i vores db


#Funktion til at gemme beregninger i print.db
def save_calculation(printer_type, printer_model, material, cost, unit, density):
    if save_to_print_jobs(printer_type, printer_model, material, cost, unit, density):
        messagebox.showinfo("Gemt", "Din beregning blev gemt")
    else:
        messagebox.showerror("Fejl", "Din beregning kunne ikke gemmes.")

def show_saved_calculations():
    calculations_window = tk.Toplevel(root)
    calculations_window.title("Gemte beregninger")
    calculations_window.geometry("1083x693")

# Styling af Treeview
    style = ttk.Style()
    style.configure("Treeview", font=("Tuffy", 12), rowheight=25, background="#444444", fieldbackground="#666666", foreground="#eaeaea")
    style.map("Treeview", background=[("selected", "green")])  
    style.configure("Treeview.Heading", font=("Tuffy", 14, "bold"), foreground="green", background="white")


# Her laver vi en treeview widget, så den kan fremvise beregningerne i table format

    tree = ttk.Treeview(show_saved_calculations, columns =("Process", "Machine", "Material", "Cost", "Unit", "Density", "Timestamp"), show="headings")
    tree.heading("Process", text="Process")
    tree.heading("Machine", text="Machine")
    tree.heading("Material", text="Material")
    tree.heading("Cost", text="Cost")
    tree.heading("Unit", text="Unit")
    tree.heading("Density", text="Density")
    tree.heading("Timestamp", text="Timestamp")

    tree.pack(fill="both", expand=True)


#Tilslutter os databasen og henter gemte beregninger
    con = sqlite3.connect("print.db")
    cursor = con.cursor()
    cursor.execute("SELECT process, machine, material, cost, unit, density, timestamp FROM print")
    records = cursor.fetchall()
    con.close()

#Her indsætter vi dataen i vores treeview widget
    for record in records:
        tree.insert("",tk.END, values=record)


root = c.CTk()
root.title("User Registration and 3D Printer Cost Calculator")
root.geometry("1083x693")
root.configure(fg_color='#757575')


# Styling
root.option_add("*Font", "Arial 12")
root.option_add("*Button.padding", [10, 5])

# Ydre container Frame
frame = c.CTkFrame(master=root, fg_color='#757575', corner_radius=10)  # Baggrundsfarve for frame
frame.pack(pady=20, padx=60, fill="both", expand=True)


# Indre Frame for at holde labels centreret
label_frame = c.CTkFrame(master=frame, fg_color='#757575')  # Baggrundsfarve for label_frame
label_frame.pack(pady=30)

# Labels for "NextPrint" og "Easy" side om side
login_label = c.CTkLabel(master=label_frame, text="NextPrint", fg_color='#757575', text_color="#FFFFFF", font=("Tuffy", 64))
login_label.pack(side="left", padx=10)

login_label2 = c.CTkLabel(master=label_frame, text="Easy", fg_color='#757575', text_color="#228B22", font=("Tuffy", 64))
login_label2.pack(side="left", padx=10)

# Placering af de øvrige elementer
username_label = c.CTkLabel(master=frame, text="Username", fg_color='#757575', text_color="#FFFFFF", font=("Tuffy", 24))
username_label.pack(pady=12, padx=10)

entry_name = c.CTkEntry(master=frame, placeholder_text="Username")
entry_name.pack(pady=12, padx=10)

password_label = c.CTkLabel(master=frame, text="Password", fg_color='#757575', text_color="#FFFFFF", font=("Tuffy", 24))
password_label.pack(pady=12, padx=10)

entry_password = c.CTkEntry(master=frame, placeholder_text="Password", show="*")
entry_password.pack(pady=12, padx=10)

frame_login = c.CTkButton(frame, text="Login", fg_color='#228B22', text_color="#FFFFFF", font=("Tuffy", 24), command=login_user)
frame_login.pack(pady=12, padx=10)

# Frame for menu (hidden initially)
menu_frame = c.CTkFrame(master=root, fg_color='#757575')

# Menu items in the new frame
menu_label = c.CTkLabel(master=menu_frame, text="Menu", fg_color='#757575', text_color="#FFFFFF", font=("Tuffy", 64))
menu_label.pack(pady=20, anchor="center") 


button_calculator = c.CTkButton(master=menu_frame, text="Calculator", fg_color='#228B22', text_color="#FFFFFF", font=("Tuffy", 24), command=open_calculator)
button_calculator.pack(pady=10, anchor="center")  

button_history = c.CTkButton(master=menu_frame, text="History", fg_color='#228B22', text_color="#FFFFFF", font=("Tuffy", 24), command=open_history)
button_history.pack(pady=10, anchor="center")  


# Opret en rød "Log ud"-knap
button_logout = c.CTkButton(master=menu_frame, text="Log out", fg_color='red', text_color="#FFFFFF", font=("Tuffy", 24), command=logout_user)
button_logout.pack(side="bottom", anchor="center", pady=10)

# Cost Calculator Frame (Er gemt)
frame_calculator = tk.LabelFrame(root, text="3D Printer Calculator", font=("Tuffy", 24, "bold"), foreground="white", background="#333333", padx=10, pady=10) 
frame_calculator.pack_forget()

# Dynamisk centrering ved resizing
def resize(event):
    if frame_calculator.winfo_ismapped():
        frame_calculator.place(relx=0.5, rely=0.5, sticky="ew")

def back_to_menu_from_calculator():
    frame_calculator.pack_forget()  # Skjul beregningsskærmen
    menu_frame.pack(padx=10, fill="both", expand=True)  # Vis menuen

root.bind("<Configure>", resize)


#Printer type dropdown menu
printer_type = ['FDM', 'SLA', 'SLS', 'SLM', 'DLP']
label_printer_type =c.CTkLabel(frame_calculator,text="Printer type", text_color="white")
label_printer_type.grid(row=0, column=0, sticky="w")

combobox_printer_type = ttk.Combobox(frame_calculator, values= printer_type, state= "readonly")
combobox_printer_type.grid(row=0, column=1)
combobox_printer_type.bind("<<ComboboxSelected>>", update_models) # Binder event her for at opdatere printer modeller baseret på valgt type


#Printer model dropdown menu
printer_model = ['Ultimaker 3', 'Fortus 360mc', 'Form2', 'ProX 950', 'EOSINT P800', 'EOSm100', '3D Systems Figure 4']
label_printer_model = c.CTkLabel(frame_calculator, text="Printer model", text_color="white")
label_printer_model.grid(row= 1, column=0, sticky="w")

combobox_printer_model = ttk.Combobox(frame_calculator, values= printer_model, state= "readonly")
combobox_printer_model.grid(row=1, column=1)
combobox_printer_model.unbind("<<ComboboxSelected>>")
combobox_printer_model.bind("<<ComboboxSelected>>", lambda event: update_materials())
#Material dropdown menu
material = ['ABS', 'Ultem', 'Clear Resin', 'Dental Model Resin', 'Accura Xtreme', 'Casting Resin', 'PA2200', 'PA12', 'Alumide', 'Ti6Al4V', 'SSL316']
label_material = c.CTkLabel(frame_calculator, text="Material", text_color="white")
label_material.grid(row=2, column= 0, sticky="w")
combobox_material = ttk.Combobox(frame_calculator, values= material, state="readonly")
combobox_material.grid(row=2, column=1, sticky="w")

#Unit dropdown menu
unit = ['Kg', 'L', 'unit', '10Kg']
label_unit = c.CTkLabel(frame_calculator, text="Unit", text_color="white")
label_unit.grid(row=3, column=0, sticky="w")

combobox_unit = ttk.Combobox(frame_calculator, values= unit, state="readonly")
combobox_unit.grid(row=3, column=1)
combobox_unit.config(values=unit)
combobox_unit.set('') # Tømmer dropdownen så man skal vælge en ny enhed

#Amount skal forblive et input felt
c.CTkLabel(frame_calculator, text="Amount", text_color="white").grid(row=4, column=0, sticky="w")
entry_amount = c.CTkEntry(frame_calculator)
#bruger sticky= "ew" for at sikre mig at input feltet strækker sig for at udfylde dens grid celle
entry_amount.grid(row=4, column=1,columnspan=2, sticky="ew")

#Input felt til antal emner
c.CTkLabel(frame_calculator, text= "N. of subjects", text_color="white").grid(row=5, column=0, sticky="w")
entry_antal_emner = c.CTkEntry(frame_calculator)
entry_antal_emner.grid(row=5, column=1, columnspan=2, sticky="ew")

#Beregnings knap
button_calculate = c.CTkButton(frame_calculator, text="Calculate", command=calculate_and_display_cost, fg_color="green", text_color="white")
button_calculate.grid(row=6, column=0, columnspan=2, pady=(20, 10))

#Fonten ændres, så man kan se det bedre
bold_font = c.CTkFont(size=12, weight="bold")
label_result = c.CTkLabel(frame_calculator, text="Calculation result", fg_color="#333333", text_color="white", font=bold_font)
label_result.grid(row=7, column=0, columnspan=2, pady=(20, 10))



# Knap til at fremvise gemte beregninger
#Knap til at fremvise beregninger skal blive vist i anden frame. 
show_calculations_button = c.CTkButton(
    frame_calculator,
    text="Show saved calculations",
    command=show_saved_calculations,
    fg_color="blue",  # Blå farve for at skelne fra andre knapper
    text_color="white"
)
show_calculations_button.grid(row=8, column=0, columnspan=2, pady=10)

# Tilføj knappen "Tilbage" til at gå tilbage til menuen
button_back_to_menu = c.CTkButton(
    frame_calculator, 
    text="Back", 
    command=lambda:back_to_menu_from_calculator(),
    fg_color="red",  # Rød farve
    text_color="white"  # Hvid tekstfarve
)
button_back_to_menu.grid(row=9, column=0, columnspan=2, pady=(20, 10))

# Run the Tkinter main loop
frame.pack()
root.mainloop()