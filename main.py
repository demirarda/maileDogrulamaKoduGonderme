from queue import Empty
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import smtplib
import random
from email.mime.text import MIMEText

root = tk.Tk()
root.title("Giriş Ekranı")
root.geometry("480x360")

# define labels
mailLabel = Label(root, width=20, height=3, text="mail: ", font="Times 15")
mailLabel.place(x=-35, y=26)
passwordLabel = Label(root, width=20, height=3, text="password: ", font="Times 15")
passwordLabel.place(x=-20, y=76)

# define entries
mailEntry = Entry(root, width=15, font="bold")
mailEntry.place(x=140, y=45)
passwordEntry = Entry(root, width=15, font="bold")
passwordEntry.place(x=140, y=95)


# def send mail
def sendMail():
    code = str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(
        random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))
    sender = 'ar_d_mr@hotmail.com'
    receivers = ['ar_d_mr@hotmail.com']
    port = 587
    msg = MIMEText(code)
    msg['Subject'] = 'Doğrulama Kodu'
    msg['From'] = 'ar_d_mr@hotmail.com'
    msg['To'] = 'ar_d_mr@hotmail.com'
    with smtplib.SMTP('smtp.office365.com', port) as server:
        server.starttls()
        server.login('ar_d_mr@hotmail.com', '010203eray')
        server.sendmail(sender, receivers, msg.as_string())
        print("Successfully sent email")
    return code


# def code entry
def codeScreen():
    code = sendMail()
    root2 = tk.Tk()
    root2.title("code")
    root2.geometry("480x360")
    codeLabel = Label(root2, width=20, height=3, text="code: ", font="Times 15")
    codeLabel.place(x=-35, y=26)
    codeEntry = Entry(root2, width=15, font="bold")
    codeEntry.place(x=140, y=45)
    Button2 = Button(root2, text="TAMAM", width=20, font="bold", command=lambda: codeControl(code, codeEntry.get()))
    Button2.place(x=50, y=150)
    root2.mainloop()


# define userControl function
def userControl():
    if mailEntry.get() == str("ar_d_mr@hotmail.com") and passwordEntry.get() == str("010203eray"):
        codeScreen()
    else:
        messagebox.showinfo("Uyarı", "Mail ve Şifrenizi Kontrol Ediniz.")


def codeControl(code, auth):
    if code == auth and code != Empty:
        messagebox.showinfo("Başarılı", "Doğrulama başarılı")
    else:
        messagebox.showinfo("Uyarı", "Doğrulama BAŞARISIZ!")


# define button
loginButton = Button(root, text="GİRİŞ", width=20, font="bold", command=userControl)
loginButton.place(x=50, y=150)

root.mainloop()