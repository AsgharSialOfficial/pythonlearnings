'''import tkinter as tk
from time import strftime
root = tk.Tk()
root.title('Digital Clock')
def time():
    string = strftime('%H:%M:%S %p \n %D')
    label.config(text=string)
    label.after(1000,time)


label = tk.Label(root, font=('calibari',50,'bold'), background='yellow',foreground='black')
label.pack(anchor='center')
time()
root.mainloop

'''
import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital Clock")

def update_time():
    string = strftime('%H:%M:%S %p \n %d/%m/%Y')
    label.config(text=string)
    label.after(1000, update_time)

label = tk.Label(
    root,
    font=('calibri', 50, 'bold'),
    background='yellow',
    foreground='black'
)
label.pack(anchor='center')

update_time()
root.mainloop()