import tkinter
import math

# Button layout
button_values = [
    ["AC", "+/-", "%", "÷"],
    ["7", "8", "9", "x"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]

right_symbols = ["+", "x", "-", "÷", "="]
top_symbols = ["AC", "+/-", "%"]

row_count = len(button_values)
column_count = len(button_values[0])

# Colors
color_light_gray = "#D4D4D2"
color_black = "#1C1C1C"
color_dark_gray = "#505050"
color_orange = "#FF9500"
color_white = "white"
color_red = "#FF3B30"

# State
A = "0"
operator = None

# Window setup
window = tkinter.Tk()
window.title("Calculator")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(
    frame,
    text="0",
    font=("Arial", 45),
    background=color_black,
    foreground=color_white,
    anchor="e",
    width=column_count
)
label.grid(row=0, column=0, columnspan=column_count, sticky="we")


def remove_zero_decimal(num):
    """Remove unnecessary decimal point for whole numbers."""
    if num % 1 == 0:
        return str(int(num))
    return str(round(num, 10))


def clear_all():
    """Reset calculator state."""
    global A, operator
    A = "0"
    operator = None


def show_error(message="Error"):
    """Display an error message on the label."""
    global A, operator
    label["text"] = message
    label.config(foreground=color_red)
    A = "0"
    operator = None


def reset_label_color():
    """Reset label color to white."""
    label.config(foreground=color_white)


def button_clicked(value):
    global A, operator

    reset_label_color()

    if value == "=":
        if A != "0" and operator is not None:
            B = label["text"]
            try:
                numA = float(A)
                numB = float(B)

                if operator == "+":
                    result = numA + numB
                elif operator == "-":
                    result = numA - numB
                elif operator == "x":
                    result = numA * numB
                elif operator == "÷":
                    if numB == 0:
                        show_error("Can't ÷ 0")
                        return
                    result = numA / numB

                label["text"] = remove_zero_decimal(result)
            except Exception:
                show_error()
            finally:
                clear_all()

    elif value in "+-x÷":
        if operator is None:
            A = label["text"]
            label["text"] = "0"
        operator = value

    elif value == "AC":
        clear_all()
        label["text"] = "0"

    elif value == "+/-":
        try:
            result = float(label["text"]) * -1
            label["text"] = remove_zero_decimal(result)
        except Exception:
            show_error()

    elif value == "%":
        try:
            result = float(label["text"]) / 100
            label["text"] = remove_zero_decimal(result)
        except Exception:
            show_error()

    elif value == "√":
        try:
            num = float(label["text"])
            if num < 0:
                show_error("Invalid")
                return
            result = math.sqrt(num)
            label["text"] = remove_zero_decimal(result)
        except Exception:
            show_error()

    elif value == ".":
        if "." not in label["text"]:
            label["text"] += "."

    elif value in "0123456789":
        if label["text"] == "0":
            label["text"] = value
        else:
            label["text"] += value


# Build buttons
for row in range(row_count):
    for column in range(column_count):
        value = button_values[row][column]
        button = tkinter.Button(
            frame,
            text=value,
            font=("Arial", 30),
            width=column_count - 1,
            height=1,
            command=lambda v=value: button_clicked(v)
        )
        if value in top_symbols:
            button.config(foreground=color_black, background=color_light_gray)
        elif value in right_symbols:
            button.config(foreground=color_white, background=color_orange)
        else:
            button.config(foreground=color_white, background=color_dark_gray)
        button.grid(row=row + 1, column=column)

frame.pack()

# Center the window
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width / 2) - (window_width / 2))
window_y = int((screen_height / 2) - (window_height / 2))
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.mainloop()