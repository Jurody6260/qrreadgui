import jwt
import qrcode as QR
import tkinter as tk
from tkinter import ttk
from models import *
maincolor = "#27263D"
secondcolor = "#27293A"
win = tk.Tk()
win.geometry('450x600+150+150')
win.title("QR")
win.configure(background=maincolor)
mainFR = tk.Frame(win, bg=secondcolor)
mainFR.place(relx=0.25, rely=0.015, relwidth=0.5, relheight=0.15)

lbl = tk.Label(mainFR, text="QR CODE", bg=secondcolor, fg="red")
lbl.place(relx=0.5, rely=0.05, anchor=tk.CENTER)


encoded_jwt = jwt.encode({"name": "Azamat"}, "secret", algorithm="HS256")
print(encoded_jwt)
code = QR.make(encoded_jwt)
code.show()
code.save("qr.png")

decoded_jwt = jwt.decode(encoded_jwt, "secret", algorithms="HS256")
print(decoded_jwt)

win.mainloop()
