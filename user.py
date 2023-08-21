import tkinter as tk
import tkinter.ttk as ttk

win = tk.Tk()
win.title('Input介面')
win.geometry('800x600')
win.resizable(False, False)
name = tk.StringVar()
card = tk.IntVar()
month = tk.IntVar()
years = tk.IntVar()
secure = tk.IntVar()
brand = tk.StringVar()
product = tk.StringVar()

usernamelist = ['蕭合亭']
username = ttk.Combobox( win, state='readonly' )
username['values'] = usernamelist
username.pack(pady=10)




textname = tk.Label( win, text='姓名', font=('Arial', 8) ).place(x=0, y=0)
entryname = tk.Entry(win, textvariable=name, width=20).place(x=30, y=0)
textcard = tk.Label( win, text='卡號', font=('Arial', 8) ).place(x=0, y=30)
entrycard = tk.Entry(win, textvariable=card, width=20).place(x=30, y=30)
textmonth = tk.Label( win, text='月份', font=('Arial', 8) ).place(x=0, y=60)
entrymonth = tk.Entry(win, textvariable=month, width=20).place(x=30, y=60)
textyear = tk.Label( win, text='年分', font=('Arial', 8) ).place(x=0, y=90)
entryyear = tk.Entry(win, textvariable=years, width=20).place(x=30, y=90)
textbrand = tk.Label( win, text='品牌', font=('Arial', 8) ).place(x=0, y=120)
entrybrand = tk.Entry(win, textvariable=brand, width=20).place(x=30, y=120)
textproduct = tk.Label( win, text='品名', font=('Arial', 8) ).place(x=0, y=150)
entryproduct = tk.Entry(win, textvariable=product, width=20).place(x=30, y=150)

#def combobox_selected(event):
    

btn = tk.Button(win, text='顯示' ).place(x=400, y=300) 
win.mainloop()