# Required Modules
from tkinter import *
import Backend as Backend
from Requirments import *
from tkinter import ttk
import socket

# Checking for Operating system
pc_name = str(socket.gethostname())
pc_name = pc_name.split("-")
mac = False
if pc_name[0] == "MacBook" or pc_name[0] == "Macbook" or pc_name[0] == "Macbooks":
    # from tkmacosx import Button
    pc_name = pc_name[0]
    mac = True


# Class for Registration Window
class RegisterWin:
    def __init__(self, root, frame) -> None:
        if frame != None:
            frame.destroy
        # main screen for registration window
        full_width = int(root_width)
        full_height = int(root_height)
        self.frame = Frame(root, bg=bg_color, width=full_width, height=full_height)
        self.frame.pack()
        self.frame.place(x=0, y=0)
        title = Label(self.frame, text="Register Yourself", bg=bg_color, fg="white", font=big_font)
        title.pack()
        title.place(x=(full_width // 2 - 30), y=20)
        labels = ["Full Name", "Contact #", "Email Address", "Account Type", "ID (If Employe)", "Address", "Username",
                  "Password"]
        frame_text = ["Your Info", "Account Info"]
        types = ["Bill Officer", "Employee", "Owner"]
        y = 50
        h = [300, 200]
        frames = []
        for i in range(2):  # Creating two label frames
            label_Frame = LabelFrame(self.frame, bg=bg_color, text=frame_text[i], fg="white", font=font,
                                     width=full_width - 60, height=h[i])
            label_Frame.pack()
            label_Frame.place(x=30, y=y)
            y += (h[i] + 10)
            frames.append(label_Frame)
        y = 40
        self.Entries = []
        # creating labels and entries to create registration window
        for i in range(len(labels)):
            if i <= 5:
                FRAME = frames[0]
            else:
                if i == 6:
                    y = 40
                    FRAME = frames[1]
            label = Label(FRAME, text=labels[i], bg=bg_color, fg="white", font=font)
            label.pack()
            if i != 4:
                x = 30
                width = 60
            else:
                x = 350
                width = 20
            label.place(x=x, y=y)
            if i != 3:
                entry = Entry(FRAME, width=width, font=font)
                entry.pack()
                entry.place(x=x + 140, y=y)
                self.Entries.append(entry)
            else:
                type_combo = ttk.Combobox(FRAME, width=10, values=types)
                type_combo.pack()
                type_combo.place(x=200, y=y)
                type_combo.set("Owner")
                self.Entries.append(type_combo)
            if i != 3:
                y += 50
        self.Entries[0].focus_force()
        self.Entries[-1]['show'] = "*"
        btns = ["Submit", "Login"]
        y = full_height - 90
        j = 0
        # Creating buttons
        self.Buttons = []
        for i in btns:
            loginBtn = Button(self.frame, text=i, width=20, font=("Times 18"), bg="red", fg=fg_color)
            loginBtn.pack()
            loginBtn.place(x=(full_width // 2 - 100), y=y)
            y += 40
            j += 1
            self.Buttons.append(loginBtn)
