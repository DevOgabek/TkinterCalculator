import tkinter as tk


def btn_click(numbers):
    current_operator.set(current_operator.get() + str(numbers))


def btn_clear_display():
    current_operator.set("")


def btn_equals_input():
    try:
        result = str(eval(current_operator.get()))
        current_operator.set(result)
    except Exception as e:
        current_operator.set("Error")


def create_button(root, text, row, column, command=None):
    return tk.Button(
        root,
        padx=16,
        pady=16,
        bd=8,
        fg="black",
        font=("Time New Roman", 20, "bold"),
        text=text,
        command=command,
    )


def on_key_press(event):
    if hasattr(event, "char"):
        key = event.char
        if key.isdigit() or key in "+-*/":
            btn_click(key)
        elif key == "\r":
            btn_equals_input()
        elif key == "c":
            btn_clear_display()


cal = tk.Tk()
cal.title("Calculator")

current_operator = tk.StringVar()

txt_display = tk.Entry(
    cal,
    font=("Time New Roman", 20, "bold"),
    textvariable=current_operator,
    bd=30,
    insertwidth=4,
    bg="blue",
    justify="right",
)
txt_display.grid(row=0, column=0, columnspan=4)

buttons = [
    ("7", 1, 0),
    ("8", 1, 1),
    ("9", 1, 2),
    ("+", 1, 3),
    ("4", 2, 0),
    ("5", 2, 1),
    ("6", 2, 2),
    ("-", 2, 3),
    ("1", 3, 0),
    ("2", 3, 1),
    ("3", 3, 2),
    ("*", 3, 3),
    ("0", 4, 0),
    ("C", 4, 1),
    ("=", 4, 2),
    ("/", 4, 3),
]

for btn_text, row, column in buttons:
    if btn_text == "C":
        command = btn_clear_display
    elif btn_text == "=":
        command = btn_equals_input
    else:
        command = lambda num=btn_text: btn_click(num)
    button = create_button(cal, btn_text, row, column, command)
    button.grid(row=row, column=column)

cal.bind("<Key>", on_key_press)
cal.mainloop()