from tkinter import *
import pickle, os

def screen():
    global main_screen
    global found

    found = 0
    main_screen = Tk() 
    main_screen.geometry("300x250")
    main_screen.title("Account") 

    Label(text="Please login or sign up", bg="grey", width="300", height="2", font=("Calibri", 13)).pack() 
    Label(text="").pack() 

    Button(text="Sign up", height="2", width="30", command = sign_up).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command = login).pack() 
 
    main_screen.mainloop()
    
    
def sign_up():
    global username
    global password
    global passwordc
    global username_entry
    global password_entry
    global passwordc_entry
    global sign_up_screen
    
    sign_up_screen = Toplevel(main_screen) 
    sign_up_screen.title("Register")
    sign_up_screen.geometry("300x250")

    username = StringVar()
    password = StringVar()
    passwordc = StringVar()
    
    Label(sign_up_screen, text="Please enter details below", bg="grey").pack()
    Label(sign_up_screen, text="").pack()
    
    username_lable = Label(sign_up_screen, text="Username * ")
    username_lable.pack()
    
    username_entry = Entry(sign_up_screen, textvariable=username)
    username_entry.pack()
    
    password_lable = Label(sign_up_screen, text="Password * ")
    password_lable.pack()
    
    password_entry = Entry(sign_up_screen, textvariable=password, show='*')
    password_entry.pack()

    passwordc_lable = Label(sign_up_screen, text="Confirm Password * ")
    passwordc_lable.pack()
    
    passwordc_entry = Entry(sign_up_screen, textvariable=passwordc, show='*')
    passwordc_entry.pack()
    
    Label(sign_up_screen, text="").pack()
    
    Button(sign_up_screen, text="sign up", width=10, height=1, bg="grey", command = user_info).pack()

def user_info():

    global sign_up_screen
    global logged_in
    global found
    global username_info
    global password_info
    found = 0
    c = 0
    username_info = username.get()
    password_info = password.get()
    passwordc_info = passwordc.get()        
    f = open('user_details.bin', 'rb+')

    while True:
        try:

            d = pickle.load(f)
            
            if d['username']==username_info:
                c = 1
                break
            else:
                pass
        except EOFError:
            break
    
    if passwordc_info == password_info and c==0 :
                    
        rec = {'username' : username_info, 'password' : password_info, 'level1' : 0, 'level2' : 0, 'level3' : 0, 'level4' : 0, 'level5' : 0, 'level6' : 0, 'level7' : 0, 'level8' : 0, 'level9' : 0, 'level10' : 0, 'level11' : 0, 'level12' : 0}
        pickle.dump(rec, f)
        f.close()
        found = 1 
        sign_up_screen.destroy()
        f.close()
    else:
        
        Label(sign_up_screen, text="The details have not been entered correctly", fg="red", font=("calibri", 11)).pack()
        Label(sign_up_screen, text="or", fg="red", font=("calibri", 11)).pack()
        Label(sign_up_screen, text="The username already exists", fg="red", font=("calibri", 11)).pack()
        username_entry.delete(0, END)
        password_entry.delete(0, END)
        passwordc_entry.delete(0, END)
        f.close()
    

    
def login():
    global username
    global password
    global username_entry
    global password_entry
    global login_screen
    
    login_screen = Toplevel(main_screen) 
    login_screen.title("Login")
    login_screen.geometry("300x250")

    username = StringVar()
    password = StringVar()
    
    
    Label(login_screen, text="Please enter details below", bg="grey").pack()
    Label(login_screen, text="").pack()
    
    username_lable = Label(login_screen, text="Username * ")
    username_lable.pack()
    
    username_entry = Entry(login_screen, textvariable=username)
    username_entry.pack()
    
    password_lable = Label(login_screen, text="Password * ")
    password_lable.pack()
    
    password_entry = Entry(login_screen, textvariable=password, show='*')
    password_entry.pack()
    
    Label(login_screen, text="").pack()

    Button(login_screen, text="login", width=10, height=1, bg="grey", command = logging_in).pack()
    
def logging_in():
    global logged_in
    global found
    global username_info
    global password_info
    
    username_info = username.get()
    password_info = password.get()
    try:
        f = open('user_details.bin', 'rb')
        found = 0
        while True:
            try:
                rec = pickle.load(f)
                if rec['username'] == username_info and rec['password'] == password_info:
                    found = 1
            except EOFError:
                break
        f.close()
        username_entry.delete(0, END)
        password_entry.delete(0, END)
        
        if found == 1:
            f = open('login_details.txt','w')
            rec = [username_info, password_info]
            d = str(rec)
            f.write(d)
            f.close()
            login_screen.destroy()
            main_screen.destroy()
            start_screen()
            
            
        else:
            Label(login_screen, text="Invalid username or password", fg="red", font=("calibri", 11)).pack()
            Label(login_screen, text="please try again", fg="red", font=("calibri", 11)).pack()
    except:
        username_entry.delete(0, END)
        password_entry.delete(0, END)
        Label(login_screen, text="Invalid username or password", fg="red", font=("calibri", 11)).pack()
        Label(login_screen, text="please try again", fg="red", font=("calibri", 11)).pack()



def start_screen():
    global startup_screen

    startup_screen = Tk() 
    startup_screen.geometry("300x450")
    startup_screen.title("play") 

    Label(text="Choose an option", bg="grey", width="300", height="2", font=("Calibri", 13)).pack() 
    Label(text="").pack() 

    Button(text="Play", height="2", width="30", command = play).pack()
    Label(text="").pack()
    Button(text="Profile", height="2", width="30", command = data).pack() 
    Label(text="").pack()
    Button(text="Highscores", height="2", width="30", command = highscore).pack()
    Label(text="").pack()
    Button(text="Credits", height="2", width="30", command = credit).pack() 
    Label(text="").pack()
    Button(text="Exit", height="2", width="30", command = Exit).pack()
    startup_screen.mainloop()

def Exit():
    global startup_screen
    startup_screen.destroy()
    os.remove('login_details.txt')
def play():
    import final_game
    
def data():
    
    global profile_screen
    profile_screen = Toplevel(startup_screen) 
    profile_screen.title("")
    profile_screen.geometry("500x450")
    Button( profile_screen, text="User Details", height="2", width="30", command = data1).pack()
    Label(profile_screen, text="").pack()
    Button( profile_screen, text="Delete Account", height="2", width="30", command = del_account).pack()
    
    Label(profile_screen, text="Note: Deleting account will erase all your data and will exit the game", bg="red", width="300", height="2", font=("Calibri", 13)).pack()
    Label(profile_screen, text="").pack()
    Button(profile_screen, text="Close", height="2", width="30", command = close1).pack()

    
def data1():
    global profile_screen
    global username_info
    global password_info
    global profile_screen1
    profile_screen1 = Toplevel(profile_screen) 
    profile_screen1.title("")
    profile_screen1.geometry("400x450")
    f = open('user_details.bin', 'rb')
    while True:
        try:
            d = pickle.load(f)
            if d['username']==username_info and d['password'] == password_info:
                for i in d.keys():
                    if i == 'username' or i =='password':
                        t = ''
                        t=t+i+' - '+str(d[i])
                        Label(profile_screen1, text=t, bg="grey").pack()
                    else:
                        t = ''
                        t=t+i+' best score'+' - '+str(d[i])
                        Label(profile_screen1, text=t, bg="grey").pack()
                    
        except EOFError:
            break
    f.close()
    Label(profile1_screen, text='').pack()
    Button(profile_screen1, text="Close", height="2", width="30", command = close3).pack()
def close3():
    global profile_screen1
    profile_screen1.destroy()

def del_account():
    global username_info
    global password_info
    global profile_screen
    global startup_screen
    
    f = open("user_details.bin",'rb')
    t = open("temp.bin", 'wb')
    while True:
        try:
            d = pickle.load(f)
            if d['username'] != username_info and d['password'] != password_info:
                pickle.dump(d, t)
            else:
                pass
        except EOFError:
            break
    f.close()
    t.close()
    os.remove("user_details.bin")
    os.rename("temp.bin", "user_details.bin")
    profile_screen.destroy()
    startup_screen.destroy()
    os.remove('login_details.txt')
    
def close1():
    global profile_screen
    profile_screen.destroy()
    
def credit():
    global credit_screen
    credit_screen = Toplevel(startup_screen) 
    credit_screen.title("Credits")
    credit_screen.geometry("300x250")
    Label(credit_screen, text='Aaryan Shetty', bg="grey").pack()
    Label(credit_screen, text='').pack()
    Label(credit_screen, text='Siddharth Warrier', bg="grey").pack()
    Label(credit_screen, text='').pack()
    Button(credit_screen, text="Close", height="2", width="30", command = close2).pack()

def close2():
    global credit_screen
    credit_screen.destroy()
    
def highscore():
    global username_info
    global password_info
    highscore_screen = Toplevel(startup_screen)
    highscore_screen.title("Highscores")
    highscore_screen.geometry("300x450")
    f = open('user_details.bin','rb')
    hlist = []
    hlist1 = []
    ulist = []
    ulist1 = []
    while True:
        try:
            nlist = []
            
            rec = pickle.load(f)
            ulist.append(rec['username'])
            for i in range(1,13):
                nlist.append(rec['level{}'.format(i)])
                
            hlist.append(nlist)
        except EOFError:
            f.close()
            break
    for i in range(0,12):
        nlist1 = []
        ulist2 = []
        for u in range(len(hlist)):
            nlist1.append(hlist[u][i])
            ulist2.append(ulist[u])
            
        hlist1.append(nlist1)
        ulist1.append(ulist2)
    for i in range(len(hlist1)):
        hlist2 = []
        for z in hlist1[i]:
            if z!=0:
                hlist2.append(z)
        if hlist2!=[]:
            
            h = min(hlist2)
            ind = hlist1[i].index(h)
            det = 'level{}'.format(i+1)+' - '+str(h)+' by '+ulist1[i][ind]
            Label(highscore_screen, text=det, bg="grey").pack()
            Label(highscore_screen, text='').pack()
            
    

    
        

screen()
