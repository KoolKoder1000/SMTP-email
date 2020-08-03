"""A GUI for sending Emails"""
from smtplib import SMTP # For sending emails
from tkinter import Tk, Frame, Label, Entry, Text, Button, END # For the GUI
from tkinter.messagebox import showerror

server = SMTP(host="smtp.gmail.com", port=587) # Set the server to accept a gmail proxy

server.starttls() # Secure sending

server.login("<INSERT INSECURE GMAIL ADDRESS>", "<INSERT PASSWORD>") # Login to an (insecure) gmail account

def send(target, subject, message):
    """A function for sending the email, through the porxy, to the target email (any)"""
    try:
        completetext = 'Subject: {}\n\n{}'.format(subject, message) # 'Subject' formatted to be the subject of the email
        server.sendmail("<INSERT PROXY GMAIL ADDRESS>", target, completetext) # Send!
    except Exception: 
        showerror("Error", "Error! Check the email address\nand wifi connection.") # Check if entries have been filled correctly

window = Tk(screenName="Email") # Define the window and set its dimensions and background colour
window.geometry("300x320+500+100")
window.config(background="#141414")

frm_head = Frame(master=window, padx=10, pady=10, bg="#141414") # Create a Frame in which to put the heading
lbl_head = Label(master=frm_head, text="Email in python!", fg="White", bg="#141414", font=("Calibri", 30)) # Label for heading
frm_head.grid(row=0, column=0) # Position both widgets
lbl_head.grid(row=0, column=0)

frm_ent = Frame(master=window, padx=45, pady=10, bg="#141414") # Frame for entries
lbl_addr = Label(master=frm_ent, text="Address: ", fg="White", bg="#141414", font=("Calibri", 10)) # Instructional Labels
lbl_sub = Label(master=frm_ent, text="Subject: ", fg="White", bg="#141414", font=("Calibri", 10))
lbl_mess = Label(master=frm_ent, text="Message: ", fg="White", bg="#141414", font=("Calibri", 10))
ent_addr = Entry(master=frm_ent, fg="White", bg="#101010", font=("Calibri", 10)) # Entry boxes
ent_sub = Entry(master=frm_ent, fg="White", bg="#101010", font=("Calibri", 10))
ent_text = Text(master=frm_ent, fg="White", bg="#101010", width=20, height=5, font=("Calibri", 10))
frm_ent.grid(row=1, column=0, sticky="nsew") # Positioning widgets
lbl_addr.grid(row=0, column=0)
lbl_sub.grid(row=1, column=0)
lbl_mess.grid(row=2, column=0)
ent_addr.grid(row=0, column=1)
ent_sub.grid(row=1, column=1)
ent_text.grid(row=2, column=1)

btn_send = Button(master=window, text="SEND", width=15, fg="White", bg="#1F1F1F", font=("Calibri", 15), command=lambda: send(ent_addr.get(), ent_sub.get(), ent_text.get('1.0', END)))
btn_send.grid(row=2, column=0) # Button widget attached to the 'send' function

window.mainloop() # Rerun until 'x' is pressed

server.quit() # Close the server
