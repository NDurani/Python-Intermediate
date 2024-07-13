import tkinter


window = tkinter.Tk()

window.title('mile to kilo Con    ')

window.minsize(width=400, height=100)

# f_label = tkinter.Label(window, text='Welcome to My', font=('Arial', 10, 'bold'))
# f_label.grid(column=0, row=0)
# def change_text():
#     new_text = input.get()
#     window.title(new_text)
#
#
# button = tkinter.Button(text="change text", command= change_text)
# button.grid(column=1, row=1)
#
# button2 = tkinter.Button(text= "habibi")
# button2.grid(column=2, row=0)
#
# input =tkinter.Entry(width= 10)
#
# input.grid(column=3, row=2)

result = ""
def calc_km_to_mile():
    num = input_num.get()
    print(num)
    result = int(num) * 1.689
    f_result.config(text=result)


input_num = tkinter.Entry(text="Enter your Number!", width=5)
input_num.grid(column=1, row=0)
in_mile = tkinter.Label(text="Miles")
in_mile.grid(column=2, row=0)

is_equal = tkinter.Label(text="Is equal to")
is_equal.grid(column=0, row=1)

f_result = tkinter.Label(text= result)
f_result.grid(column=1, row=1)


to_km = tkinter.Label(text="Km")
to_km.grid(column=2, row=1)

calc_button = tkinter.Button(text="Calculate", command=calc_km_to_mile)
calc_button.grid(column=1, row=2)




window.mainloop()