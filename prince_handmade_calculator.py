import customtkinter as ctk

def button_click(number):
    current = entry.get()
    entry.delete(0, ctk.END)
    entry.insert(0, str(current) + str(number))


def equal():
    current = entry.get()
    entry.delete(0, ctk.END)
    try:
        result = eval(current)
        entry.insert(0, str(result))
    except SyntaxError:
        entry.insert(0, "Syntax Error")
    except ZeroDivisionError:
        entry.insert(0, "Math Error")


def clear():
    entry.delete(0, ctk.END)


root = ctk.CTk()
root.title("Prince app")
root.geometry("500x500")

entry = ctk.CTkEntry(root,
                     font=("arial", 40, "bold"),
                     height=10,
                     width=1000)
entry.grid()

button1 = ctk.CTkButton(root,
                        text=1,
                        height=100,
                        width=100,
                        text_color="black",
                        fg_color="#18E26C",
                        hover_color="#4BDD88",
                        font=("arial", 40, "bold"),
                        command=lambda: button_click(1))
button1.grid(padx=5, pady=5, row=1, column=0)

button2 = ctk.CTkButton(root,
                        text=2,
                        height=100,
                        width=100,
                        text_color="black",
                        fg_color="#18E26C",
                        hover_color="#4BDD88",
                        font=("arial", 40, "bold"),
                        command=lambda: button_click(2))
button2.grid(padx=5, pady=5, row=1, column=1)

button3 = ctk.CTkButton(root,
                        text=3,
                        height=100,
                        width=100,
                        text_color="black",
                        fg_color="#18E26C",
                        hover_color="#4BDD88",
                        font=("arial", 40, "bold"),
                        command=lambda: button_click(3))
button3.grid(padx=5, pady=5, row=1, column=2)

button4 = ctk.CTkButton(root,
                        text=4,
                        height=100,
                        width=100,
                        text_color="black",
                        fg_color="#18E26C",
                        hover_color="#4BDD88",
                        font=("arial", 40, "bold"),
                        command=lambda: button_click(4))
button4.grid(padx=5, pady=5, row=2, column=0)

button5 = ctk.CTkButton(root,
                        text=5,
                        height=100,
                        width=100,
                        text_color="black",
                        fg_color="#18E26C",
                        hover_color="#4BDD88",
                        font=("arial", 40, "bold"),
                        command=lambda: button_click(5))
button5.grid(padx=5, pady=5, row=2, column=1)

button6 = ctk.CTkButton(root,
                        text=6,
                        height=100,
                        width=100,
                        text_color="black",
                        fg_color="#18E26C",
                        hover_color="#4BDD88",
                        font=("arial", 40, "bold"),
                        command=lambda: button_click(6))
button6.grid(padx=5, pady=5, row=2, column=2)

button7 = ctk.CTkButton(root,
                        text=7,
                        height=100,
                        width=100,
                        text_color="black",
                        fg_color="#18E26C",
                        hover_color="#4BDD88",
                        font=("arial", 40, "bold"),
                        command=lambda: button_click(7))
button7.grid(padx=5, pady=5, row=3, column=0)

button8 = ctk.CTkButton(root,
                        text=8,
                        height=100,
                        width=100,
                        text_color="black",
                        fg_color="#18E26C",
                        hover_color="#4BDD88",
                        font=("arial", 40, "bold"),
                        command=lambda: button_click(8))
button8.grid(padx=5, pady=5, row=3, column=1)

button9 = ctk.CTkButton(root,
                        text=9,
                        height=100,
                        width=100,
                        text_color="black",
                        fg_color="#18E26C",
                        hover_color="#4BDD88",
                        font=("arial", 40, "bold"),
                        command=lambda: button_click(9))
button9.grid(padx=5, pady=5, row=3, column=2)

button0 = ctk.CTkButton(root,
                        text=0,
                        height=100,
                        width=100,
                        text_color="black",
                        fg_color="#18E26C",
                        hover_color="#4BDD88",
                        font=("arial", 40, "bold"),
                        command=lambda: button_click(0))
button0.grid(padx=5, pady=5, row=4, column=1)

button_equal = ctk.CTkButton(root,
                             text="=",
                             height=100,
                             width=100,
                             text_color="black",
                             fg_color="#18E26C",
                             hover_color="#4BDD88",
                             font=("arial", 40, "bold"),
                             command=equal)
button_equal.grid(padx=5, pady=5, row=4, column=2)

button_clear = ctk.CTkButton(root,
                             text="C",
                             height=100,
                             width=100,
                             text_color="black",
                             fg_color="#18E26C",
                             hover_color="#4BDD88",
                             font=("arial", 40, "bold"),
                             command=clear)
button_clear.grid(padx=5, pady=5, row=4, column=0)

button_plus = ctk.CTkButton(root,
                            text="+",
                            height=100,
                            width=100,
                            text_color="black",
                            fg_color="#18E26C",
                            hover_color="#4BDD88",
                            font=("arial", 40, "bold"),
                            command=lambda: button_click("+"))
button_plus.grid(padx=5, pady=5, row=1, column=3)

button_minus = ctk.CTkButton(root,
                             text="-",
                             height=100,
                             width=100,
                             text_color="black",
                             fg_color="#18E26C",
                             hover_color="#4BDD88",
                             font=("arial", 40, "bold"),
                             command=lambda: button_click("-"))
button_minus.grid(padx=5, pady=5, row=2, column=3)

button_multiply = ctk.CTkButton(root,
                                text="*",
                                height=100,
                                width=100,
                                text_color="black",
                                fg_color="#18E26C",
                                hover_color="#4BDD88",
                                font=("arial", 40, "bold"),
                                command=lambda: button_click("*"))
button_multiply.grid(padx=5, pady=5, row=3, column=3)

button_division = ctk.CTkButton(root,
                                text="/",
                                height=100,
                                width=100,
                                text_color="black",
                                fg_color="#18E26C",
                                hover_color="#4BDD88",
                                font=("arial", 40, "bold"),
                                command=lambda: button_click("/"))
button_division.grid(padx=5, pady=5, row=4, column=3)



root.mainloop()