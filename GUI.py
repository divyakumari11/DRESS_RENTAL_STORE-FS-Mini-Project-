from tkinter import *
import tkinter.font
import datetime
import tkinter.messagebox
from datetime import timedelta
import os
import hashlib
import binascii
from tkinter import*
from PIL import ImageTk,Image

def login_in():
	global id_input_login
	global password_input_login
	global login_menu

	login_menu=Tk()
	login_menu.wm_title("Login")
	login_menu.minsize(860,700)
	login_menu.maxsize(1960,900)
	login_menu.resizable(0,0)
	login_menu.geometry("1199x600+100+50")

# ===BG Image===================
	login_menu.bg= PhotoImage(file="images/costumeShop1.png")
	login_menu.bg_image=Label(login_menu,image=login_menu.bg).place(x=0,y=0,relwidth=1,relheight=1)
	k_font = tkinter.font.Font(family='Times new roman', size=15, weight=tkinter.font.BOLD)
	

	#id
	id_label=Label(login_menu,relief=GROOVE,text="Your ID:",font=('arial',18,'bold'),bg="purple")
	id_label.place(x=250,y=45)
	id_input_login=Entry(login_menu,width=10,font=("times new roman",18,"bold"),bd=5,relief=SUNKEN)
	id_input_login.place(x=370,y=45)

	
	
	# #password
	password_label=Label(login_menu,relief=GROOVE,text="Password:",font=('arial',20,'bold'),bg="purple")
	password_label.place(x=700,y=45)
	password_input_login=Entry(login_menu, show="*",width=10,font=("times new roman",18,"bold"),bd=5,relief=SUNKEN)
	password_input_login.place(x=865,y=45)
	
	#login button
	loginbutton1=Button(login_menu,command=login_check,text=" Login ",bg='red',height=2,width=14,font=k_font)
	loginbutton1.place(x=255,y=600)
	
	# #register button
	registerbutton=Button(login_menu,command=register_in,text=" Register ",bg='orange',height=2,width=14,font=k_font)
	registerbutton.place(x=455,y=600)
	# #feedback button
	feedbackbutton=Button(login_menu,command=feedback_read,text=" Feedback ",bg='purple',height=2,width=14,font=k_font)
	feedbackbutton.place(x=655,y=600)
	# #admin button
	adminbutton=Button(login_menu,command=admin_in,text=" Admin Login ",bg='brown',height=2,width=14,font=k_font)
	adminbutton.place(x=855,y=600)


	login_menu.mainloop()

def login_check():
	global id
	id=id_input_login.get()
	password=password_input_login.get()

	#use absolute path instead of relative - if using relative make sure to be in same directory
	pos = binary_search('index.txt', id)
	if pos == -1:
		tkinter.messagebox.showinfo("Login"," Username is incorrect.Please reenter")
		return(login_in)
	else:
		f2 = open ('Userprofile.txt', 'r')
		f2.seek(int(pos))
		l = f2.readline()
		l = l.rstrip()
		word = l.split('|')
		if(verify_password(word[1], password)):
			tkinter.messagebox.showinfo("Login","Login Successful!")
			login_menu.destroy()
			Main_Menu()
		else:
			tkinter.messagebox.showinfo("Login"," Password that you have entered is incorrect.Please reenter")
			return(login_in)
		f2.close()


def register_in():
	global id_input
	global name_input
	global email_input
	global password_input
	global register_menu

	register_menu=Tk()
	register_menu.wm_title("Register")
	register_menu.geometry("1199x600+100+50")
	#bg image#################################
	# register_menu.bg= PhotoImage(file="images/registerPic.png")
	# register_menu.bg_image1=Label(register_menu,image=register_menu.bg).place(x=0,y=0,relwidth=1,relheight=1)
	k_font = tkinter.font.Font(family='Times new roman', size=10, weight=tkinter.font.BOLD)
	

	#title2_label=Label(register_menu,relief=GROOVE,text="DRESS RENTAL SYSTEM REGISTRATION PORTAL",font=('Times new roman',20,'bold'))
	#title2_label.place(x=250,y=45)
	id_label=Label(register_menu,text="Your ID",bd=5,relief=SUNKEN,font=('arial',20,'bold'))
	# id_label.place(x=370,y=45)
	id_label.grid(row=0,column=1,padx=200,pady=10,sticky="w")


	name_label=Label(register_menu,text="Full Name",bd=5,relief=SUNKEN,font=('arial',20,'bold'))
	name_label.grid(row=1,column=1,padx=200,pady=10,sticky="w")

	email_label=Label(register_menu,text="Email",bd=5,relief=SUNKEN,font=('arial',20,'bold'))
	email_label.grid(row=2,column=1,padx=200,pady=10,sticky="w")

	password_label=Label(register_menu,text="Password",bd=5,relief=SUNKEN,font=('arial',20,'bold'))
	password_label.grid(row=3,column=1,padx=200,pady=10,sticky="w")

	id_input=Entry(register_menu,bd=10,relief=SUNKEN)
	id_input.grid(row=0,column=2,padx=200,pady=10,sticky="w")

	name_input=Entry(register_menu,bd=10,relief=SUNKEN)
	name_input.grid(row=1,column=2,padx=200,pady=10,sticky="w")

	email_input=Entry(register_menu,bd=10,relief=SUNKEN)
	email_input.grid(row=2,column=2,padx=200,pady=10,sticky="w")

	password_input=Entry(register_menu,bd=10,relief=SUNKEN)
	password_input.grid(row=3,column=2,padx=200,pady=10,sticky="w")

	# loginbutton1=Button(register_menu,command=login_in,text=" Login ",bg='light blue',height=2,width=14,font=k_font)
	# loginbutton1.grid(row=13,column=2,pady=20,padx=10,sticky="w")
	registerbutton=Button(register_menu,command=register_check,text=" Register ",bg='dark blue',height=2,width=14,font=k_font)
	registerbutton.grid(row=14,column=2,pady=20,padx=10,sticky="w")
	password_input.config(show="*")

	# id_label.grid(row=3,column=15)
	# id_input.grid(row=3,column=20)
	# name_label.grid(row=5,column=15)
	# name_input.grid(row=5,column=20)
	# email_label.grid(row=6,column=15)
	# email_input.grid(row=6,column=20)
	# password_label.grid(row=7,column=15)
	# password_input.grid(row=7,column=20)
	# registerbutton.grid(columnspan=2)
	# loginbutton1.grid(columnspan=2)

	register_menu.mainloop()

def register_check():
	global id

	id=id_input.get()
	name=name_input.get()
	email=email_input.get()
	password=password_input.get()

	if len(id)==0 or len(name) == 0 or len(email) == 0 or len(password) == 0:
		tkinter.messagebox.showinfo("Register","You left one or more fields blank O_O")
		register_menu.lift()
		return(register_in)

	pos = binary_search('index.txt', id)
	if pos != -1:
		tkinter.messagebox.showinfo("Register","Already registered. Choose a different ID")
		register_menu.destroy()

	f2 = open ('Userprofile.txt', 'a')
	pos = f2.tell()
	f3 = open ('index.txt', 'a')
	buf = id + '|' + hash_password(password) + '|' + name + '|' + email + '|' + '#'
	f2.write(buf)
	f2.write('\n')
	buf = id + '|' + str(pos) + '|' + '#'
	f3.write(buf)
	f3.write('\n')
	f3.close()
	f2.close()
	key_sort('index.txt')
	tkinter.messagebox.showinfo("Register","Registration Successful!")
	register_menu.destroy()


def hash_password(password):
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),
                                salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')

def verify_password(stored_password, provided_password):
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512',
                                  provided_password.encode('utf-8'),
                                  salt.encode('ascii'),
                                  100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password


def admin_in():
		global id_admin
		global password_admin
		global admin_menu
		global bg_image1
		global id_admin

		admin_menu=Toplevel()
		admin_menu.wm_title("Admin")
		# admin_menu.minsize(860,700)
		# admin_menu.maxsize(1960,900)
		# admin_menu.resizable(0,0)
		admin_menu.geometry("1199x600+100+50")
		k_font = tkinter.font.Font(family='Times new roman', size=16, weight=tkinter.font.BOLD)

		#===BG Image===================
		admin_menu.bg= PhotoImage(file="images/img1.png")
		admin_menu.bg_image1=Label(admin_menu,image=admin_menu.bg).place(x=0,y=0,relwidth=1,relheight=1)

	

		admin_label=Label(admin_menu,bd=5,relief="raised",text="Admin ID",font=('arial',20,'bold'),bg="light blue")
		admin_password_label=Label(admin_menu,bd=5,relief="raised",text="Password",font=('arial',20,'bold'),bg="light blue")
		id_admin=Entry(admin_menu,width=10,font=("times new roman",18,"bold"),bd=5,relief=SUNKEN)
		password_admin=Entry(admin_menu,width=10,font=("times new roman",18,"bold"),bd=5,relief=SUNKEN)
		loginbutton2=Button(admin_menu,bd=5,relief="raised",command=admin_check,text=" Login ",bg='light blue',height=1,width=9,font=k_font)
		password_admin.config(show="*")

		admin_label.place(x=370,y=50)
		admin_password_label.place(x=370,y=150)
		id_admin.place(x=370,y=100)
		password_admin.place(x=370,y=200)
		loginbutton2.place(x=380,y=250)

		admin_menu.mainloop()

def admin_check():
	global admin_id

	admin_id=id_admin.get()
	admin_password=password_admin.get()

	if admin_id=="admin" and admin_password=="admin":
		tkinter.messagebox.showinfo("Login","Admin Login Successful!")
		admin_menu.destroy()
		login_menu.destroy()
		Admin_Opt()
	else:
		tkinter.messagebox.showinfo("Login","Admin id or password INCORRECT. Please reenter")

def Admin_Opt():
		global opt_menu

		opt_menu=Tk()
		opt_menu.wm_title("Admin_menu")
		
		opt_menu.geometry("1199x600+100+50")
		k_font = tkinter.font.Font(family='Times new roman', size=50, weight=tkinter.font.BOLD)

		addbutton=Button(opt_menu,command=add_book,bd=5,relief=SUNKEN,text=" Add Dress ",bg='light pink',height=1,width=20,font=k_font)
		delbutton=Button(opt_menu,command=del_book,bd=5,relief=SUNKEN,text=" Remove Dress ",bg='light blue',height=1,width=20,font=k_font)
		backbutton=Button(opt_menu,command=reopen_login,bd=5,relief=SUNKEN,text=" Log out ",bg='light blue',height=1,width=20,font=k_font)

		addbutton.pack()
		delbutton.pack()
		backbutton.pack()

		opt_menu.mainloop()

def reopen_login():
	tkinter.messagebox.showinfo("Login","Admin Logout Successful!")
	opt_menu.destroy()

	f7=open('Bindex.txt','r')
	lines1=f7.readlines()
	f7.close()
	f8=open('Bindex.txt','w')
	for line1 in lines1:
		if line1.startswith('*'):
			continue
		else:
			f8.write(line1)
	f8.close()

	login_in()


def key_sort(fname):
	t=list()
	fin=open(fname,'r')
	for line in fin:
		line=line.rstrip('\n')
		words=line.split('|')
		t.append((words[0],words[1]))
	fin.close()
	t.sort()
	with open("temp.txt",'w') as fout:
		for pkey,addr in t:
			pack=pkey+"|"+addr+"|#"
			fout.write(pack+'\n')
	os.remove(fname)
	os.rename("temp.txt",fname)


def binary_search(fname, search_key):
	t = []
	fin = open(fname,'r')
	for lx in fin:
		lx = lx.rstrip()
		wx = lx.split('|')
		t.append((wx[0], wx[1]))
	fin.close()
	l = 0
	r = len(t) - 1
	while l <= r:
		mid = (l + r)//2
		if t[mid][0] == search_key:
			return int(t[mid][1])
		elif t[mid][0] <= search_key:
			l = mid + 1
		else:
			r = mid - 1
	return -1


def add_book():
	global book_id
	global book_name
	global author_name
	global add_menu

	add_menu=Tk()
	add_menu.wm_title("Add")
	add_menu.minsize(600,550)
	add_menu.maxsize(600,550)
	#add_menu.resizable(0,0)
	k_font = tkinter.font.Font(family='Times new roman', size=12, weight=tkinter.font.BOLD)

	book_id_label=Label(add_menu,font=('arial',18,'bold'),text="Dress ID (Should be of atleast length 5)")
	book_label=Label(add_menu,font=('arial',18,'bold'),text="Dress Name")
	author_label=Label(add_menu,font=('arial',18,'bold'),text="Brand")
	book_id=Entry(add_menu)
	book_name=Entry(add_menu)
	author_name=Entry(add_menu)
	addbutton1=Button(add_menu,command=add_check,text=" Add Dress ",bg='dark orange',height=1,width=10,font=k_font)

	book_id_label.grid(row=0,sticky=E)
	book_id.grid(row=0,column=1)
	book_label.grid(row=1,sticky=E)
	book_name.grid(row=1,column=1)
	author_label.grid(row=2,sticky=E)
	author_name.grid(row=2,column=1)
	addbutton1.grid(columnspan=2)

	add_menu.mainloop()

def add_check():
	global b_id
	b_id=book_id.get()
	b_name=book_name.get().upper()
	a_id=author_name.get()

	if len(b_name)==0:
		tkinter.messagebox.showinfo("Add Dress","You did not type a Dress name O_O")
		add_menu.lift()
		return(add_book)

	if len(b_id)!=5 or b_id.isdigit()==False:
		tkinter.messagebox.showinfo("Add Dress","Please renter the details(ID should be 5 positive integers)")
		add_menu.lift()
		return(add_book)

	if len(a_id) == 0:
		a_id = "Anonymous"

	pos = binary_search('Bindex.txt', b_id)
	if pos != -1:
		tkinter.messagebox.showinfo("Dress","Dress already present.Please try again")
		add_menu.lift()
		return(add_book)

	f22 = open ('BData.txt', 'a')
	pos = f22.tell()
	f33 = open ('Bindex.txt', 'a')
	buf = b_id + '|' + b_name + '|' + a_id + '|' + 'Y' + '|' + '#'
	f22.write(buf)
	f22.write('\n')
	buf = b_id + '|' + str(pos) + '|' + '#'
	f33.write(buf)
	f33.write('\n')
	f33.close()
	f22.close()
	key_sort('Bindex.txt')
	tkinter.messagebox.showinfo("Add","Dress added Successfully!")
	add_menu.destroy()


def del_book():
	global rb_id
	global del_menu

	del_menu=Tk()
	del_menu.wm_title("Delete")
	del_menu.minsize(1000,600)
	del_menu.maxsize(1000,600)
	del_menu.resizable(0,0)
	k_font = tkinter.font.Font(family='Times new roman', size=10, weight=tkinter.font.BOLD)

	Id=[]
	Title = []
	Author = []
	Availability = []

	f1 = open('Bindex.txt', 'r')
	f = open ("BData.txt", 'r')
	norecord = 0
	for line in f1:
		if not line.startswith('*'):
			norecord += 1
			line = line.rstrip('\n')
			word = line.split('|')
			f.seek(int(word[1]))
			line1 = f.readline().rstrip()
			word1 = line1.split('|')
			Id.append(word1[0])
			Title.append(word1[1])
			Author.append(word1[2])
			Availability.append(word1[3])
	f.close()
	#f1.close()

	borrow_list=Listbox(del_menu,height=50,width=20)
	borrow_list2=Listbox(del_menu,height=50,width=50)
	borrow_list3=Listbox(del_menu,height=50,width=50)
	borrow_list4=Listbox(del_menu,height=50,width=20)

	for num in range(0,norecord):
		borrow_list.insert(0,Id[num])
		borrow_list2.insert(0,Title[num])
		borrow_list3.insert(0,Author[num])
		borrow_list4.insert(0,Availability[num])


	b_label=Label(del_menu,text="Book ID")
	rb_id=Entry(del_menu)
	delbutton1=Button(del_menu,command=del_check,text=" Remove book ",bg='dark orange',height=1,width=10,font=k_font)
	borrow_list2.configure(background="pink")
	borrow_list3.configure(background="pink")
	borrow_list.configure(background="light grey")
	borrow_list4.configure(background="light grey")
	borrow_label=Label(del_menu,text="Id")
	borrow_label2=Label(del_menu,text="Dress")
	borrow_label3=Label(del_menu,text="Brand")
	borrow_label4=Label(del_menu,text="Availability")

	borrow_label.grid(row=6,column=0)
	borrow_label2.grid(row=6,column=1)
	borrow_label3.grid(row=6,column=3)
	borrow_label4.grid(row=6,column=6)

	borrow_list.grid(row=7,column=0)
	borrow_list2.grid(row=7,column=1)
	borrow_list3.grid(row=7,column=3)
	borrow_list4.grid(row=7,column=6)
	b_label.grid(row=0,sticky=E)
	rb_id.grid(row=0,column=1)
	delbutton1.grid(row=2,columnspan=1)
	del_menu.mainloop()

def del_check():

	global del_id
	del_id=rb_id.get()

	if len(del_id)==0:
		tkinter.messagebox.showinfo("Delete Dress","You did not type anything O_O")
		del_menu.lift()
		return(del_book)

	pos = binary_search('Bindex.txt', del_id)
	if(pos == -1):
		tkinter.messagebox.showinfo("Delete","Dress not present.Please re-enter")
		del_menu.destroy()
		return(del_book)
	else:
		f = open ('BData.txt', 'r')
		f.seek(pos)
		l1 = f.readline().rstrip()
		w1 = l1.split('|')
		if(w1[3] == 'N'):
			tkinter.messagebox.showinfo("Delete","Dress currently borrowed. Please try another Dress")
			del_menu.destroy()
			return(del_book)

	index = -1

	with open('Bindex.txt','r') as file:
		for line in file:
			words=line.split("|")
			if(words[0]==del_id):
					index=int(words[1])

	index=0
	with open("Bindex.txt",'r+') as file:
		line=file.readline()
		while line:
			words=line.split("|")
			if words[0]==del_id:
				file.seek(index,0)
				file.write("*")
				break
			else:
				index=file.tell()
				line=file.readline()
	tkinter.messagebox.showinfo("Delete","Dress Successfully removed")
	del_menu.destroy()


def Main_Menu():
	base = Tk()
	#Window title and size optimization
	base.wm_title("DRESS RENTAL STORE")
	base.geometry("1920x780+00+00")

	in_font = tkinter.font.Font(family='Lucida Calligraphy', size=25, weight=tkinter.font.BOLD)
	current_time1=datetime.datetime.now()
	current_time=str(current_time1)

	#Bunch of labels
	status = Label(base,text=("Date and time logged in: " + current_time),bd=1,relief=SUNKEN,anchor=W,bg='light pink')
	orionLabel=Label(base, text="DRESS RENTAL STORE",bg='purple',font=("Gabriola", "50","bold","italic"),fg="black")
	# welcomeLabel=Label(base,text=("Welcome! "+id),font=("Freestyle Script","30","bold"))
	# imageLibrary = PhotoImage(file="giphy.gif")
	topFrame=Frame(base)
	bottomFrame=Frame(base)

	#Positioning of labels
	status.pack(side=BOTTOM,fill=X)
	orionLabel.pack(fill=X)
	# welcomeLabel.pack(side="left")
	# Label(base, image=imageLibrary).pack()
	topFrame.pack()
	bottomFrame.pack(side=BOTTOM)

	#Buttons
	borrow_but=Button(bottomFrame,bg="purple",fg="white",text="Borrow Outfit",font=in_font,height=3,width=30,command=borrow_in)
	return_but=Button(bottomFrame,bg="pink",text="Return Outfit",font=in_font,height=3,width=30,command=return_in)
	search_but=Button(bottomFrame,bg="purple",fg="white",text="Search for Outfit",font=in_font,height=3,width=30,command=search_in)
	feedback_but=Button(bottomFrame,bg="pink",text="Feedback",font=in_font,height=3,width=30,command=feedback_in)

	#Positioning of buttons
	borrow_but.pack()
	return_but.pack()
	search_but.pack()
	feedback_but.pack()

	base.mainloop()


def borrow_in():
	global borrow_entry1
	global borrow_menu

	borrow_menu=Tk()

	borrow_menu.wm_title("Borrow")
	borrow_menu.minsize(900,550)
	borrow_menu.maxsize(1200,550)
	borrow_menu.resizable(0,0)

	Id=[]
	Title = []
	Author = []
	Availability = []

	f1 = open('Bindex.txt', 'r')
	f = open ("BData.txt", 'r')
	norecord = 0
	for line in f1:
		norecord += 1
		line = line.rstrip('\n')
		word = line.split('|')
		f.seek(int(word[1]))
		line1 = f.readline().rstrip()
		word1 = line1.split('|')
		Id.append(word1[0])
		Title.append(word1[1])
		Author.append(word1[2])
		Availability.append(word1[3])
	f.close()

	borrow_list=Listbox(borrow_menu,height=50,width=20)
	borrow_list1=Listbox(borrow_menu,height=50,width=50)
	borrow_list2=Listbox(borrow_menu,height=50,width=50)
	borrow_list3=Listbox(borrow_menu,height=50,width=20)

	for num in range(0,norecord):
		borrow_list.insert(0,Id[num])
		borrow_list1.insert(0,Title[num])
		borrow_list2.insert(0,Author[num])
		borrow_list3.insert(0,Availability[num])

	borrow_list.configure(background="aqua")
	borrow_list1.configure(background="pink")
	borrow_list2.configure(background="aqua")
	borrow_list3.configure(background="pink")
	borrow_label1=Label(borrow_menu,text="<<< Please enter the Dress ID that you wish to borrow >>>",font=("Times", "20","bold","italic"),bg="purple")
	borrow_label=Label(borrow_menu,text="Id")
	borrow_label2=Label(borrow_menu,text="Dress")
	borrow_label3=Label(borrow_menu,text="Brand")
	borrow_label4=Label(borrow_menu,text="Stocks")

	borrow_entry1=Entry(borrow_menu,width=50)
	borrow_button1=Button(borrow_menu,text="Borrow",command=borrow_check,font=("Times new roman","10","bold"),bg="pink")

	borrow_label1.grid(row=0,columnspan=20)
	borrow_label.grid(row=3,column=0)
	borrow_label2.grid(row=3,column=1)
	borrow_label3.grid(row=3,column=4)
	borrow_label4.grid(row=3,column=7)

	borrow_entry1.grid(row=1,columnspan=20)
	borrow_button1.grid(row=2,columnspan=20)
	borrow_list.grid(row=4,column=0)
	borrow_list1.grid(row=4,column=1)
	borrow_list2.grid(row=4,column=4)
	borrow_list3.grid(row=4,column=7)
	borrow_menu.mainloop()

def borrow_check():

	count = 0
	f = open('Record.txt', 'r')
	for l in f:
		l = l.split('|')
		if l[0] ==  id:
			count += 1
	if count >= 2:
		tkinter.messagebox.showinfo("Borrow", "Cannot borrow more than 2 outfits at a time")
		borrow_menu.destroy()

	else:
		date = datetime.date.today()
		enddate = date + timedelta(days = 7)
		bbook=borrow_entry1.get().upper()

		if len(bbook) == 0:
			tkinter.messagebox.showinfo("Borrow","You did not type anything O_O")
			borrow_menu.lift()
			return(borrow_in)

		pos = binary_search('Bindex.txt', bbook)
		if pos == -1:
			tkinter.messagebox.showinfo("Borrow","The outfit that you had entered is not in our database,sorry,please enter a different outfit")
			borrow_menu.lift()
		else:
			f2 = open('BData.txt', 'r+')
			f2.seek(pos)
			l2 = f2.readline()
			l2 = l2.rstrip('\n')
			w2 = l2.split('|')
			if(w2[3] == 'Y'):
				l3 = w2[0] + '|' + w2[1] + '|' + w2[2] + '|' + 'N|#'
				f2.seek(pos)
				f2.write(l3)
				f2.close()
				tkinter.messagebox.showinfo("Borrow","The outfit you have selected has been successfully borrowed. Please return it by:" +'\n'+ str(enddate) )

				buf = id + '|' + bbook + '|#\n'
				f3 = open('Record.txt', 'a')
				f3.write(buf)
				f3.close()
				key_sort('Record.txt')
				Done2=tkinter.messagebox.askyesno("Borrow","Do you want to borrow another outfit?")
				if Done2==True:
					borrow_menu.destroy()
					borrow_in()
				else:
					borrow_menu.destroy()
			else:
				tkinter.messagebox.showinfo("Borrow","This dress is currently unavailable, please select another outfit")
				borrow_menu.lift()


def return_in():
	global return_entry1
	global return_menu
	global record_verification

	return_menu=Tk()
	return_menu.minsize(900,500)
	return_menu.maxsize(1200,500)
	return_menu.wm_title("Return")
	return_menu.resizable(0,0)

	Id=[]
	Title = []
	Author = []
	Availability = []
	record_verification = []

	f = open ("Record.txt")
	norecord = 0
	for line in f:
		line = line.rstrip()
		words = line.split('|')
		if(words[0] == id):
			pos = binary_search('Bindex.txt', words[1])
			if pos != -1:
				norecord += 1
				f2 = open('BData.txt', 'r')
				f2.seek(pos)
				l1 = f2.readline()
				l1 = l1.rstrip()
				w1 = l1.split('|')
				Id.append(w1[0])
				record_verification.append(w1[0])
				Title.append(w1[1])
				Author.append(w1[2])
				Availability.append(w1[3])
	f.close()

	return_list=Listbox(return_menu,height=50,width=20)
	return_list1=Listbox(return_menu,height=50,width=50)
	return_list2=Listbox(return_menu,height=50,width=50)
	return_list3=Listbox(return_menu,height=50,width=20)

	for num in range(0,norecord):
		return_list.insert(0,Id[num])
		return_list1.insert(0,Title[num])
		return_list2.insert(0,Author[num])
		return_list3.insert(0,Availability[num])

	return_list.configure(background="aqua")
	return_list1.configure(background="pink")
	return_list2.configure(background="aqua")
	return_list3.configure(background="pink")
	return_label=Label(return_menu,text="Id")
	return_label2=Label(return_menu,text="Dress Name")
	return_label3=Label(return_menu,text="Brand")
	return_label4=Label(return_menu,text="	Stocks")

	return_button1=Button(return_menu,text="Return",command=return_check,font=("Times new roman","10","bold"),bg="pink",fg="black")
	return_entry1=Entry(return_menu,width=50)
	return_label1=Label(return_menu,text=" Please enter the OUTFIT ID that you wish to return ",font=("Times", "12","bold","italic"),bg="aqua",fg="black")
	return_label1.grid(row=0,columnspan=20)
	return_entry1.grid(row=1,columnspan=20)
	return_button1.grid(row=2,columnspan=20)

	return_label.grid(row=3,column=0)
	return_label2.grid(row=3,column=1)
	return_label3.grid(row=3,column=4)
	return_label4.grid(row=3,column=7)

	return_list.grid(row=4,column=0)
	return_list1.grid(row=4,column=1)
	return_list2.grid(row=4,column=4)
	return_list3.grid(row=4,column=7)

	return_menu.mainloop()


def return_check():
	import datetime as dt
	from datetime import timedelta
	date = dt.date.today()
	bbook = return_entry1.get().upper()

	if len(bbook) == 0:
		tkinter.messagebox.showinfo("Return","You did not type anything O_O")
		return_menu.lift()
		return(return_in)

	if(bbook in record_verification):
		pos = binary_search('Bindex.txt', bbook)
		if pos != -1:
			f1 = open('BData.txt', 'r+')
			f1.seek(pos)
			l1 = f1.readline().rstrip()
			w1 = l1.split('|')
			if(w1[3] == 'N'):
				tkinter.messagebox.showinfo("Return","The outfit you have selected has been successfully returned on"+'\n'+str(date))
				f1.seek(pos)
				line = w1[0] + '|' + w1[1] + '|' + w1[2] + '|Y|#'
				f1.write(line)

				f2=open('Record.txt','r')
				lines=f2.readlines()
				f2.close()
				f3=open('Record.txt','w')
				for l2 in lines:
					l3=l2.split('|')
					if l3[1] == bbook and l3[0] == id:
						continue
					else:
						f3.write(l2)
				f3.close()
				Done3=tkinter.messagebox.askyesno("Return","Do you want to return another outfit?")
				if Done3==True:
					f1.close()
					return_menu.destroy()
					return_in()
				else:
					return_menu.destroy()
			else:
				tkinter.messagebox.showinfo("This book has been returned, please select another outfit")
			f1.close()
	else:
		tkinter.messagebox.showinfo("Return","The outfit that you had entered is invalid.Please reenter a different outfit")
		return_menu.lift()


def search_in():
	global search_entry
	global search_menu
	search_menu=Tk()

	#search_menu.maxsize(500,100)
	#search_menu.maxsize(500,100)
	search_menu.wm_title("Search")
	#search_menu.resizable(0,0)
	search_menu.geometry("800x600")

	search_label1=Label(search_menu,text="Search out ,our latest collection and grab the best of all time costumes.\n For any occasion or any event\n we have the best collections of costumes in the market.",font=("Times", "15","bold","italic"),bg="purple")
	search_label1.place(x=20,y=20,height=70)

	search_entry = Entry(search_menu,width=100,bg="pink")
	search_entry.place(x=100,y=100,height=70)

	search_button=Button(search_menu,text="Search",height= 3,width= 20,command=search_check,font=("Times new roman","20","bold"),bg="pink",fg="black")
	search_button.place(x=250,y=300)

	search_menu.mainloop()

	


def search_check():
	search_word=search_entry.get().upper()
	search_menu.destroy()

	if len(search_word) == 0:
		tkinter.messagebox.showinfo("Search","You did not type anything O_O")
		return(search_in)

	pos = binary_search('Bindex.txt', search_word)

	if (pos == -1):
		tkinter.messagebox.showinfo("Search","Sorry,this outfit does not exist in our database")
	else:
		search_menu2=Tk()
		search_menu2.wm_title("Search")
		search_menu2.attributes("-topmost",True)
		tkinter.messagebox.showinfo("Search","It is in our database!")

		search_result=Listbox(search_menu2,height=10,width=50)
		f2 = open('BData.txt', 'r')
		f2.seek(pos)
		l1 = f2.readline()
		l1 = l1.rstrip()
		w1 = l1.split('|')
		b_id = w1[0]
		book = w1[1]
		author = w1[2]
		if(w1[3] == 'Y'):
			availability = 'Available'
		else:
			availability = 'Unavailable'
		f2.close()

		search_result.insert(1,"ID:" + b_id)
		search_result.insert(2,"Name:" + book)
		search_result.insert(3,"Author:" + author)
		search_result.insert(4,"Availability:" + availability)

		search_result.pack()
		search_menu2.mainloop()


def feedback_in():
	global feedback_bar
	global feedback_menu
	global feedback_input

	feedback_menu=Tk()
	feedback_menu.wm_title("Feedback")
	feedback_menu.geometry("800x600")

	feedback_bar=Entry(feedback_menu,width=130,bg="pink")
	feedback_label=Label(feedback_menu,text= "Our Happiness lies in your Satisfaction.\n Do share your experience with us.Thank you!",font=("Monotype corsiva","30","italic"),bg="purple")
	button1=Button(feedback_menu, text="Submit feedback",height=4,width=20,command=feedback_check,font=("Times new roman","10","bold"),bg="pink")

	feedback_bar.place(x=10,y=10,height=70)
	feedback_label.place(x=100,y=100)
	button1.place(x=300,y=300)
	feedback_menu.mainloop()

def feedback_check():
	user_feedback=feedback_bar.get()
	if len(feedback_bar.get())==0:
		tkinter.messagebox.showinfo("Feedback","You did not type anything O_O")
		feedback_menu.lift()
		return(feedback_in)
	else:
		tkinter.messagebox.showinfo("Feedback","Thank you for your valuable feedback! >_<")
		file = open('Feedback.txt', 'a')
		file.write(user_feedback + "\n")
		file.close()
		feedback_menu.destroy()


def feedback_read():
	login_menu.destroy()
	read_feedback_menu=Tk()
	read_feedback_menu.minsize=(1000,1000)
	read_feedback_menu.minsize=(1000,1000)
	read_feedback_menu.wm_title("Users' feedback")

	list=Listbox(read_feedback_menu)
	file = open('Feedback.txt' , 'r')
	num_feedback = len(file.readlines())
	file.close()
	file = open('Feedback.txt' , 'r')
	count = 1
	feedback = file.readlines()
	for i in range(0, num_feedback):
		list_feedback =str(count) + ('.') + (feedback[count - 1])
		list.insert(count,list_feedback)
		count += 1
	file.close()

	list.pack(side=LEFT,fill=BOTH,expand=YES)
	read_feedback_menu.mainloop()

id_input_login=''
password_input_login=''
login_menu=''
id=''
login_in()