# importing modules
from tkinter import *
import Backend as Backend
from Requirments import *
import socket

# checking for operating system
pc_name = str(socket.gethostname())
pc_name = pc_name.split("-")
mac = False
if pc_name[0] == "MacBook" or pc_name[0] == "Macbook" or pc_name[0] == "Macbooks":
    # from tkmacosx import Button
    pc_name = pc_name[0]
    mac = True


# clear function to delete entry data
def clear(event, entry):
    entry.delete(0, "end")


# Login window class
class LoginWin:

    def __init__(self, root, Imgs, frame=None) -> None:

        if frame != None:
            frame.destroy()
        height = int(root_height)
        width = int(root_width)

        # Main Frame of Login Window
        self.frame = Frame(root, bg=light_fg)
        self.frame.pack(fill=BOTH, expand=1)

        # loginFrame = Frame(self.frame,bg="orange",width=width//2,height=height)
        # loginFrame.pack()
        # loginFrame.place(x=width//2,y=0)
        lbl = Label(self.frame, image=Imgs[13], bg="red")
        lbl.pack()
        lbl.place(x=-80, y=0)
        login_label = Label(self.frame, text="Login", bg="black", fg=light_fg, font=hug_bold_font)
        login_label.pack()
        login_label.place(x=60, y=130)

        loginImg = [Imgs[10], Imgs[11]]
        y = 200

        j = 0
        self.Entries = []
        for i in loginImg:
            lbl = Label(self.frame, image=i, bg="red")
            lbl.pack()

            lbl.place(x=50, y=y)
            entry = Entry(self.frame, width=entry_width, font=("Times 18"))
            entry.pack()
            entry.place(x=80, y=y)
            entry.bind("<Button-1>", lambda event, ent=entry: clear(event, ent))
            if i == 1:
                entry['show'] = "*"
            y += 50
            j += 1
            self.Entries.append(entry)
        self.Entries[0].focus_force()
        self.Entries[1]['show'] = "*"
        # creating checkbox 
        self.check = IntVar()
        logged_in = Checkbutton(self.frame, text="Remember me", fg=light_fg, bg="black", variable=self.check)
        logged_in.pack()
        logged_in.place(x=60, y=y)
        btns = ["Login", "Create Account"]

        j = 0
        # creating buttons
        self.buttons = []
        for i in btns:
            loginBtn = Button(self.frame, text=i, width=20, font=("Times 18"), bg="red", fg=fg_color)
            loginBtn.pack()
            loginBtn.place(x=60, y=y + 40)
            y += 40
            j += 1
            self.buttons.append(loginBtn)
