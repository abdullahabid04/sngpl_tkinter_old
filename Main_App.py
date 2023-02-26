# /usr/local/bin/python!
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from Login import LoginWin
from Register import RegisterWin
import Backend
from Requirments import *
# from Dashbaord import Dashbaord
# from modules.Billing import *
# from modules.Settings import Settings
# from modules.Home import home
# from modules.Projects import Tenders
# from modules.Stock import stock_entry


def ExitButton():
    exit()


def LogOut(root, user):
    result = messagebox.askquestion("Log Out Alert!", "Do you really Want to Log Out?")
    if result == "yes":
        root.destroy()
        Backend.Remember_me(user, "0", pc_name)
        main()


# def Dashboard_Func(data,root,load_img):
#
#    dashbaord = Dashbaord(data,mac,root,load_img)
#    btn_commands = [home,Billing,Tenders,stock_entry,Settings]
#    for i in range(len(dashbaord.DashBtn_list)):
#        if i != 5:
#           dashbaord.DashBtn_list[i]['command'] = lambda open=btn_commands[i],tab_no=i,imgs=load_img:dashbaord.Change_Tab(open=open,tab_no=tab_no,imgs=imgs)
#        else:
#            dashbaord.DashBtn_list[i]['command'] = lambda root=root,user=data[-2]:LogOut(root,user)
#
#
def Login_Confirmation(root, frame, entries, c, load_img):
    data = Backend.Login_Backend(entries, c, pc_name)
    if data != "wrong":
        frame.destroy()
        # Dashboard_Func(data,root,load_img)


def login_confirmation_event(event, root, frame, entries, c, imgs):
    Login_Confirmation(root, frame, entries, c, imgs)


def Submit_func(entries):
    Backend.Submit(entries=entries)


def Login_Func(root, this_frame, load_imgs):
    loginWin = LoginWin(root=root, Imgs=load_imgs, frame=this_frame)
    entries = loginWin.Entries
    checkBtn = loginWin.check
    commands = [lambda root=root, frame=loginWin.frame, c=checkBtn, entries=entries, imgs=load_imgs:
                Login_Confirmation(root, frame, entries, c, imgs),
                lambda root=root, frame=loginWin.frame, imgs=load_imgs:
                RegisterMember(root, frame, imgs)]
    for i in range(len(loginWin.buttons)):
        loginWin.buttons[i]["command"] = commands[i]
    entries[1].bind("<Return>", lambda event, root=root, frame=loginWin.frame, c=checkBtn, entries=entries,
                                       imgs=load_imgs: login_confirmation_event(event, root, frame, entries, c, imgs))


# Registration Form Window Code
def RegisterMember(root, myframe, imgs):
    register_win = RegisterWin(root, frame=myframe)
    entries = register_win.Entries
    commands = [lambda entries=entries: Submit_func(entries),
                lambda frame=myframe, root=root, img=imgs: Login_Func(root, frame, img)]
    for i in range(len(register_win.Buttons)):
        register_win.Buttons[i]["command"] = commands[i]


# Root Window and Program Starting Code
def main():
    root = Tk()
    root.title("AZEEM OFFICE APPLICATION")
    root.geometry(f'{root_width}x{root_height}')
    root.wm_resizable(0, 0)
    frame = Frame(root, relief=RIDGE, bg="white", )
    frame.pack(fill=BOTH, expand=1)
    load_imgs = []

    for i in range(len(Images)):
        try:
            load_imgs.append(PhotoImage(file=Images[i]))
        except:
            pass
            # path = filedialog.askopenfilename(filetypes=[("Image File", '.jpg', '.png')], title=Image_Titles[i])
            # load_imgs.append(PhotoImage(file=path))

    Logo = load_imgs[0]
    RegImage = load_imgs[1]
    LogoImage = Label(frame, image=Logo, relief=FLAT, border=0)
    LogoImage.pack(side=TOP)
    Register = Button(frame, image=RegImage, relief=FLAT, border=0,
                      command=lambda frame=frame, img=load_imgs, root=root: RegisterMember(root, frame, img))
    Register.pack()
    SignIn = Label(frame, text="Already a member?", font=("Times", 11), foreground="#00CCFF", background="#ffffff", )
    SignIn.pack()

    SignInLabel = Button(
        frame,
        text="Sign In",
        font=("Times", 11, "underline"),
        background="#FFFFFF",
        relief=FLAT,
        border=0,
        cursor="plus",
        command=lambda root=root, frame=frame, imgs=load_imgs: Login_Func(root, frame, imgs),
    )
    SignInLabel.pack()
    ExitImage = PhotoImage(file=Images[8])
    ExitLabel = Button(
        frame,
        image=ExitImage,
        relief=FLAT,
        border=0,
        width=70,
        height=70,
        command=ExitButton,
    )
    ExitLabel.pack()
    ExitLabel.place(x=70, y=560)
    LoginStatus, data = Backend.Login_Status(pc_name)
    if LoginStatus:
        pass
        # Dashboard_Func(data, root)

    mainloop()


main()
