import tkinter as tk

window = tk.Tk()

lbl_screen = tk.Label(
    master=window,
    # width=50,
    height=4,
)


btn_seven = tk.Button(
    master=window,
    text='7',
    font = ('Sans','15','bold'),
    width=3,
    height=2,
    command=lambda: print('7')
)

btn_eight = tk.Button(
    master=window,
    text='8',
    font = ('Sans','15','bold'),
    width=3,
    height=2,
    command=lambda: print('8')
)

btn_nine = tk.Button(
    master=window,
    text='9',
    font = ('Sans','15','bold'),
    width=3,
    height=2,
    command=lambda: print('9')
)

btn_plus = tk.Button(
    master=window,
    text='+',
    font = ('Sans','15','bold'),
    width=3,
    height=2,
    command=lambda: print('+')
)

btn_four = tk.Button(
    master=window,
    text='4',
    font = ('Sans','15','bold'),
    width=3,
    height=2,
    command=lambda: print('4')
)

btn_five = tk.Button(
    master=window,
    text='5',
    font = ('Sans','15','bold'),
    width=3,
    height=2,
    command=lambda: print('5')
)

btn_six = tk.Button(
    master=window,
    text='6',
    font = ('Sans','15','bold'),
    width=3,
    height=2,
    command=lambda: print('6')
)

btn_minus = tk.Button(
    master=window,
    text='-',
    font = ('Sans','15','bold'),
    width=3,
    height=2,
    command=lambda: print('-')
)

btn_one = tk.Button(
    master=window,
    text='1',
    font = ('Sans','15','bold'),
    width=3,
    height=2,
    command=lambda: print('1')
)

btn_two = tk.Button(
    master=window,
    text='2',
    font = ('Sans','15','bold'),
    width=3,
    height=2,
    command=lambda: print('2')
)

btn_three = tk.Button(
    master=window,
    text='3',
    font = ('Sans','15','bold'),
    width=3,
    height=2,
    command=lambda: print('3')
)

btn_multiply = tk.Button(
    master=window,
    text='*',
    font = ('Sans','15','bold'),
    width=3,
    height=2,
    command=lambda: print('*')
)

btn_dot = tk.Button(
    master=window,
    text='.',
    font = ('Sans','15','bold'),
    width=3,
    height=2,
    command=lambda: print('.')
)

btn_zero = tk.Button(
    master=window,
    text='0',
    font = ('Sans','15','bold'),
    width=3,
    height=2,
    command=lambda: print('0')
)

btn_clear = tk.Button(
    master=window,
    text='C',
    font = ('Sans','15','bold'),
    width=3,
    height=2,
    command=lambda: print('C')
)

btn_equal = tk.Button(
    master=window,
    text='=',
    font = ('Sans','15','bold'),
    width=3,
    height=2,
    command=lambda: print('=')
)

lbl_screen.grid(row=0, column=0)
btn_seven.grid(row=1, column=0)
btn_eight.grid(row=1, column=1)
btn_nine.grid(row=1, column=2)
btn_plus.grid(row=1, column=3)
btn_four.grid(row=2, column=0)
btn_five.grid(row=2, column=1)
btn_six.grid(row=2, column=2)
btn_minus.grid(row=2, column=3)
btn_one.grid(row=3, column=0)
btn_two.grid(row=3, column=1)
btn_three.grid(row=3, column=2)
btn_multiply.grid(row=3, column=3)
btn_dot.grid(row=4, column=0)
btn_zero.grid(row=4, column=1)
btn_clear.grid(row=4, column=2)
btn_equal.grid(row=4, column=3)




window.mainloop()
