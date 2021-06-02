import jwt
import qrcode as QR
import tkinter as tk
from tkinter import ttk
from models import *
import cv2
import pyzbar.pyzbar as pyzbar
# cap = cv2.VideoCapture(0)
# font = cv2.FONT_HERSHEY_PLAIN
# while True:
#     _, frame = cap.read()
#     decodedObjects = pyzbar.decode(frame)
#     for obj in decodedObjects:
#         #print("Data", obj.data)
#         cv2.putText(frame, str(obj.data), (50, 50), font, 2,
#                     (255, 0, 0), 3)
#     cv2.imshow("Frame", frame)
# k = cv2.waitKey(0)
# if k == 27:
#     cv2.destroyAllWindows()
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


encoded_jwt = jwt.encode({"name": "Pudge is missing 14:45"}, "secret", algorithm="HS256")
print(encoded_jwt)
code = QR.make(encoded_jwt)
code.show()
code.save("qr.png")
decoded_jwt = jwt.decode(encoded_jwt, "secret", algorithms="HS256")
print(decoded_jwt)

win.mainloop()
