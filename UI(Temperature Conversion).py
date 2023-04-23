# Author:           @eddie304050
# Program name:     UI(Temperature Conversion)
# Date:             April 3th, 2022

# IMPORTS


# Imports all classes from the tkinter module.
from tkinter import *

# Imports all classes from the tkinter.tix module.
from tkinter.tix import *

# Imports the sys module for exiting the program.
import sys


# *****************************************************************************


# Function converts given temperature to celsius
result = 0.0


def to_celsius(_event=None):

    valid_temperature = 0.0
    valid_temperature = float(entry_temperature.get())
    result = 0.0

    result = (valid_temperature - 32) * (5/9)

    return (valid_temperature, "degrees Fahrenheit converts to", result, "degrees Celsius")


# Function converts given temperature to fahrenheit
def to_fahrenheit(_event=None):

    valid_temperature = 0.0
    valid_temperature = float(entry_temperature.get())
    result = 0.0

    result = (valid_temperature * (9/5) + 32)

    return (str(valid_temperature), "degrees Celsius converts to", str(result), "degrees Fahrenheit")


# Function closes the window
def close_window(_event=None):
    sys.exit()

# Function clears the value in all fields


def clear_fields(_event=None):
    entry_temperature.delete(0, END)
    entry_temperature.focus()
    label_result_output.configure(text="")
    radiobutton_celsius.select()


# Function selects which temperature type to convert to.
def selection():
    choice = var.get()
    if choice == 1:
        r = to_celsius()
    elif choice == 2:
        r = to_fahrenheit()

    return r

# Function converts and provides resulting temperature.


def convert_temp():
    try:
        r = selection()
        label_result_output.configure(text=(r))
    except:
        label_result_output.configure(
            text=("ERROR: Please enter a numeric temperature to convert."))


# *****************************************************************************
# TK INSTANCE
window = Tk()


# *****************************************************************************


# WINDOW PROPERTIES

# Window size
window.geometry("800x300")

# Window resize is set to False.
window.resizable(False, False)

# Window title is named "Temperature Conversion."
window.title("Temperature Conversion")

# Creates a Balloon object for tooltips.
tooltip = Balloon(window)


# *****************************************************************************


# ROW 0

# Row 0 Widgets
label_temperature_prompt = Label(text="Enter the Temperature:")
label_temperature_prompt.grid(row=0, column=0, padx=5, pady=5, sticky=E)
entry_temperature = Entry(width=25)
entry_temperature.grid(row=0, column=1, padx=5, pady=5, sticky=W)
entry_temperature.focus()
en = Entry(entry_temperature)
tooltip.bind_widget(entry_temperature, msg="Enter the temperature")


# *****************************************************************************


# ROW 1

# Row 1 Widgets
label_result_prompt = Label(text="Result:")
label_result_prompt.grid(row=1, column=0, padx=5, pady=5, sticky=E)
label_result_output = Label(width=70, bd=4, relief=SUNKEN)
label_result_output.grid(row=1, column=1, padx=5, pady=5, sticky=W)
tooltip.bind_widget(label_result_output, msg="Displays the Calculated Area")


# *****************************************************************************


# ROW 2

# Row 2 Widgets
var = IntVar()
radiobutton_celsius = Radiobutton(window, text="Celsius", variable=var, value=1,
                                  command=to_celsius, bg="yellow", indicator=0)
radiobutton_celsius.grid(row=2, column=0, padx=5, pady=5, sticky=E)
radiobutton_celsius.select()


radiobutton_fahrenheit = Radiobutton(window, text="Fahrenheit", variable=var, value=2,
                                     command=to_fahrenheit, bg="yellow", indicator=0)
radiobutton_fahrenheit.grid(row=2, column=1, padx=5, pady=5, sticky=W)


# ROW 3

# Row 3 Widgets
button_convert = Button(text="Convert", width=18, command=convert_temp)
button_convert.grid(row=3, column=0, padx=10, pady=10, sticky=E)

button_clear = Button(text="Clear", width=18, command=clear_fields)
button_clear.grid(row=3, column=1, padx=10, pady=10, sticky=W)

button_exit = Button(text="Exit", width=18, command=close_window)
button_exit.grid(row=3, column=2, padx=10, pady=10, sticky=W)

# Assigning balloon comments
tooltip.bind_widget(button_convert, msg="<Return> - To Convert Temperature")

tooltip.bind_widget(button_clear, msg="<Alt-c> - To Clear All Fields")

tooltip.bind_widget(button_exit, msg="<Alt-x> - To Exit")

tooltip.bind_widget(radiobutton_celsius, msg="Converts to Celsius")

tooltip.bind_widget(radiobutton_fahrenheit, msg="Converts to Fahrenheit")


# *****************************************************************************

# HOTKEYS


# ALT-c clears all the fields.
window.bind("<Alt-c>", clear_fields)

# ALT-x closes the window and ends the program.
window.bind("<Alt-x>", close_window)

# RETURN converts the given temperature.
window.bind("<Return>", convert_temp)


window.mainloop()
