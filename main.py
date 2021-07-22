from tkinter import *
import base64


r = Tk()
r.geometry('500x300')
r.resizable(0, 0)
r.title("Message Encode and Decode")

text = StringVar()
secure_key = StringVar()
mode = StringVar()
result = StringVar()


def Encode(key, clear):
    enc = []

    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) +
                     ord(key_c)) % 256)

        enc.append(enc_c)

    return base64.urlsafe_b64encode("".join(enc).encode()).decode()


def Decode(key, enc):
    dec = []

    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) -
                     ord(key_c)) % 256)

        dec.append(dec_c)
    return "".join(dec)


def Mode():
    clear = text.get()
    k = secure_key.get()

    if mode.get() == 'e':
        result.set(Encode(k, clear))

    elif mode.get() == 'd':
        result.set(Decode(k, clear))

    else:
        result.set('Invalid Mode')


def Reset():
    text.set("")
    secure_key.set("")
    mode.set("")
    result.set("")


def Exit():
    r.destory()


Label(r, text='ENCODE DECODE', font='arial 20 bold').pack()

l1 = Label(r, text='MESSAGE', font='arial 10 bold').place(x=0, y=50)
e1 = Entry(r, textvariable=text).place(x=355, y=60)

l2 = Label(r, text='KEY', font='arial 10 bold').place(x=0, y=100)
e2 = Entry(r, textvariable=secure_key).place(x=355, y=110)

l3 = Label(r, text='MODE(e-encode, d-decode)', font='arial 10 bold').place(x=0, y=150)
e3 = Entry(r, textvariable=mode).place(x=355, y=160)

button1 = Button(r, text='Result', width=10, command=Mode).place(x=0, y=200)
e4 = Entry(r, textvariable=result).place(x=355, y=210)

button2 = Button(r, text='RESET', width=10, bg='green', command=Reset).place(x=0, y=250)
button3 = Button(r, text='EXIT', width=10, bg='red', command=Exit).place(x=100, y=250)

r.mainloop()
