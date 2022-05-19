import tkinter as tk 
from tkinter import ttk,messagebox
from csv import DictWriter,reader
import os
import datetime
import time

window= tk.Tk()
window.title("Sledge Distillery Compliance Application")

canvas = tk.Canvas(window,height= 100,width = 400)
canvas.grid(row=0)

logo = tk.PhotoImage(file = "sdca_logo.png")
logo_label = tk.Label(canvas,image = logo)
logo_label.grid(row = 0 , column = 1)

canvas = tk.Canvas(window,height= 25,width = 400)
canvas.grid(row=1)

labelframe1 = ttk.LabelFrame(window, text="Add New User",height = 400,width = 400)  
labelframe1.grid(row=2)

# create the labels for user data entry

firstname_label = ttk.Label(labelframe1, text = "First Name : ")
firstname_label.grid(row = 1,column = 0, sticky= tk.W , padx =5,pady = 5)

lastname_label = ttk.Label(labelframe1, text = "Last Name : ")
lastname_label.grid(row = 2,column = 0, sticky= tk.W , padx =5,pady = 5)

email_label = ttk.Label(labelframe1, text = "Email : ")
email_label.grid(row = 3,column = 0, sticky= tk.W , padx =5,pady = 5)

phone_label = ttk.Label(labelframe1, text = "Phone : ")
phone_label.grid(row = 4,column = 0, sticky= tk.W, padx =5,pady = 5)

driver_label = ttk.Label(labelframe1, text = "Driver's License : ")
driver_label.grid(row = 5,column = 0, sticky= tk.W, padx =5,pady = 5)

state_label = ttk.Label(labelframe1, text = "State : ")
state_label.grid(row = 6,column = 0, sticky= tk.W, padx =5,pady = 5)

# create entry box to collect entry from user 

firstname = tk.StringVar()
firstname_entrybox = ttk.Entry(labelframe1, width= 20 , textvariable = firstname)
firstname_entrybox.grid (row = 1,column = 2 , padx =5,pady = 5)
firstname_entrybox.focus()

lastname = tk.StringVar()
lastname_entrybox = ttk.Entry(labelframe1, width= 20 , textvariable = lastname)
lastname_entrybox.grid (row = 2,column = 2 , padx =5,pady = 5)

email = tk.StringVar()
email_entrybox = ttk.Entry(labelframe1, width= 20 , textvariable = email)
email_entrybox.grid (row = 3 ,column = 2, padx =5,pady = 5)

phone = tk.StringVar()
phone_entrybox = ttk.Entry(labelframe1, width= 20 , textvariable = phone)
phone_entrybox.grid (row = 4 ,column = 2, padx =5,pady = 5)

driver_license = tk.StringVar()
driver_license_entrybox = ttk.Entry(labelframe1, width= 20 , textvariable = driver_license)
driver_license_entrybox.grid (row = 5,column = 2, padx =5,pady = 5)

state = tk.StringVar()
state_entrybox = ttk.Entry(labelframe1, width= 20 , textvariable = state)
state_entrybox.grid (row = 6,column = 2, padx =5,pady = 5)


# checkbox 

check_val = tk.IntVar()
checkbtn = ttk.Checkbutton(labelframe1,text = "Please Check the filled information ", variable = check_val)
checkbtn.grid(row = 7, columnspan = 3 , padx =5,pady = 5)



#create buttons 
def senddata():
	user_fname = firstname.get()
	user_lname = lastname.get()
	user_email = email.get()
	user_phone = phone.get()
	user_license = driver_license.get()
	user_state = state_get()
	if check_val.get() == 0:
		messagebox.showinfo("information","Please tick the Check Box ")
	else:
	#	with open("data.txt","a") as f :
	#		f.write(f'{user_fname},{user_lname},{user_email},{user_phone},{user_license}')

		with open("data.csv",'a',newline = "") as f :
			dict_writer = DictWriter(f,fieldnames = ['Firstname','Lastname','Email','Phone','Driver License','State'])
			if os.stat('data.csv').st_size == 0 :
				dict_writer.writeheader()
			dict_writer.writerow({
				'Firstname' : user_fname ,
				'Lastname' : user_lname,
				'Email' : user_email,
				'Phone' : user_phone,
				'Driver License' : user_license,
				'State' : user_state,
	
				})
		messagebox.showinfo('','New user added successfully')

	firstname_entrybox.delete(0,tk.END)
	lastname_entrybox.delete(0,tk.END)
	email_entrybox.delete(0,tk.END)
	phone_entrybox.delete(0,tk.END)
	driver_license_entrybox.delete(0,tk.END)
	state_entrybox.delete(0,tk.END)

submit_button = ttk.Button(labelframe1, text = "Submit" ,command = senddata) 
submit_button.grid(row= 8 , column = 0, padx =5,pady = 5)

def cleardata():
	firstname_entrybox.delete(0,tk.END)
	lastname_entrybox.delete(0,tk.END)
	email_entrybox.delete(0,tk.END)
	phone_entrybox.delete(0,tk.END)
	driver_license_entrybox.delete(0,tk.END)
	state_entrybox.delete(0,tk.END)	

clear_button = ttk.Button(labelframe1, text = "Clear" ,command = cleardata) 
clear_button.grid(row= 8 , column = 2, padx =5,pady = 5)

canvas = tk.Canvas(window,height= 25,width = 400)
canvas.grid(row=3)



#code for existing user 
labelframe2 = ttk.LabelFrame(window, text="Existing User",height = 400,width = 400)  
labelframe2.grid(row=4)

driver_label1 = ttk.Label(labelframe2, text = "Driver's License : ")
driver_label1.grid(row = 1,column = 0,padx =20,pady = 20 )

driver_license1 = tk.StringVar()
driver_license_entrybox1 = ttk.Entry(labelframe2, width= 20 , textvariable = driver_license1)
driver_license_entrybox1.grid (row = 1, column = 2 ,padx =20,pady = 20)


#create buttons 
def getdataall():
	with open("data.csv",'r') as f :
		csv_reader = reader(f)
		next(csv_reader)
		for row in csv_reader : 
			listBox.insert("", "end", values=(row[0],row[1],row[2],row[3],row[4],row[5]))


show_all = ttk.Button(labelframe2, text = "Show All" ,command = getdataall) 
show_all.grid(row= 3 , column = 0, padx =5,pady = 5)


def transact():
	top = tk.Toplevel(window) 
	user_license1 = driver_license1.get()
	firstname = lastname = email = phone = driver_state = ''
	upper = 0

	canvas = tk.Canvas(top,height= 100,width = 400)
	canvas.grid(row=0)

	logo = tk.PhotoImage(file = "sdca_logo.png")
	logo_label = tk.Label(canvas,image = logo)
	logo_label.grid(row = 0 , column = 1)

	canvas = tk.Canvas(top,height= 25,width = 400)
	canvas.grid(row=1)

	toplabelframe1 = ttk.LabelFrame(top, text="User Details",height = 400,width = 400)  
	toplabelframe1.grid(row=2)

	with open("data.csv",'r') as f :
		csv_reader = reader(f)
		next(csv_reader)
		for row in csv_reader:
			for i in row :
				if row[4] == user_license1 : 
					firstname = row[0]
					lastname = row[1]
					email = row[2]
					phone = row[3]
					driver_state = row[5]
				
					topfirstname_label = ttk.Label(toplabelframe1, text = "First Name : ")
					topfirstname_label.grid(row = 1,column = 0, sticky= tk.W , padx =5,pady = 5)

					toplastname_label = ttk.Label(toplabelframe1, text = "Last Name : ")
					toplastname_label.grid(row = 2,column = 0, sticky= tk.W , padx =5,pady = 5)

					topemail_label = ttk.Label(toplabelframe1, text = "Email : ")
					topemail_label.grid(row = 3,column = 0, sticky= tk.W , padx =5,pady = 5)

					topphone_label = ttk.Label(toplabelframe1, text = "Phone : ")
					topphone_label.grid(row = 4,column = 0, sticky= tk.W, padx =5,pady = 5)

					topdriver_label = ttk.Label(toplabelframe1, text = "Driver's License : ")
					topdriver_label.grid(row = 5,column = 0, sticky= tk.W, padx =5,pady = 5)

					topstate_label = ttk.Label(toplabelframe1, text = "State : ")
					topstate_label.grid(row = 6,column = 0, sticky= tk.W, padx =5,pady = 5)

					#====
					valuefirstname_label = ttk.Label(toplabelframe1, text = firstname)
					valuefirstname_label.grid(row = 1,column = 1, sticky= tk.W , padx =5,pady = 5)

					valuelastname_label = ttk.Label(toplabelframe1, text = lastname)
					valuelastname_label.grid(row = 2,column = 1, sticky= tk.W , padx =5,pady = 5)

					valueemail_label = ttk.Label(toplabelframe1, text = email)
					valueemail_label.grid(row = 3,column = 1, sticky= tk.W , padx =5,pady = 5)

					valuephone_label = ttk.Label(toplabelframe1, text = phone)
					valuephone_label.grid(row = 4,column = 1, sticky= tk.W, padx =5,pady = 5)

					valuedriver_label = ttk.Label(toplabelframe1, text = user_license1)
					valuedriver_label.grid(row = 5,column = 1, sticky= tk.W, padx =5,pady = 5)

					valuestate_label = ttk.Label(toplabelframe1, text = driver_state)
					valuestate_label.grid(row = 6,column = 1, sticky= tk.W, padx =5,pady = 5)

					

		toplabelframe2 = ttk.LabelFrame(top, text="Transaction Details",height = 400,width = 400)  
		toplabelframe2.grid(row=4)

		cols = ("Transaction ID","Transaction Date","Quantity")
		listBox = ttk.Treeview(toplabelframe2, columns=cols, show='headings')
		list1 = []
		monthly_transaction = []
		with open("transaction_data.csv",'r') as f :
			csv_reader = reader(f)
			next(csv_reader)
			for row in csv_reader:
				if user_license1 == row[0]:
					list1.append(row)

			#print(list1)
			list1.reverse()
			for i in list1 : 
				listBox.insert("", "end", values=(i[1],i[2],i[3]))
					#upper = upper+int(row[3])
			
			#monthly_transaction.append(list1[0])
			'''latest_transaction = monthly_transaction[0]
			f_date = latest_transaction[2]
			inter = f_date.split('-')
			f_day = int(inter[0])
			f_month = int(inter[1])
			f_year = int(inter[2])'''
			final_current_date = datetime.date.today()

			for i in range(len(list1)) :
				latest_transaction = list1[i]
				f_date = latest_transaction[2]
				inter = f_date.split('-')
				f_day = int(inter[0])
				f_month = int(inter[1])
				f_year = int(inter[2])
				next_current_date = datetime.date(f_year,f_month,f_day)
				duration = (final_current_date-next_current_date).days
				if duration <= 30 :
					monthly_transaction.append(list1[i])

			for j in monthly_transaction : 
				upper = upper+int(j[3])
				
			if upper >= 1500 :
				messagebox.showerror(" ","Maximum Quantity for 30 days - 1500 ml  Achieved !") 

		for col in cols:
			listBox.heading(col, text=col)    
			listBox.grid(row=2)

		canvas = tk.Canvas(toplabelframe2,height= 50,width = 400)
		canvas.grid(row=6)


		if firstname == '' and lastname == '' and email == '' and phone == '' and driver_state == '':  
			messagebox.showerror(" ","User Data not Found !") 

	#driver_license_entrybox1.delete(0,tk.END)

	toplabelframe3 = ttk.LabelFrame(top, text="New Transaction",height = 400,width = 400)  
	toplabelframe3.grid(row=3)


	label750= ttk.Label(toplabelframe3, text = "Quantity of 750 ml :")
	label750.grid(row = 1,column = 0, sticky= tk.W , padx =5,pady = 5)

	label375 = ttk.Label(toplabelframe3, text = "Quantity of 375 ml :")
	label375.grid(row = 2,column = 0, sticky= tk.W , padx =5,pady = 5)

	value_750 = tk.StringVar()
	combo750 = ttk.Combobox(toplabelframe3,width = 20,textvariable = value_750 , state = "readonly")
	combo750['value'] = ('0','1','2')
	combo750.current(0)
	combo750.grid(row = 1,column = 1, sticky= tk.W , padx =5,pady = 5)

	value_375 = tk.StringVar()
	combo375 = ttk.Combobox(toplabelframe3,width = 20,textvariable = value_375 , state = "readonly")
	combo375['value'] = ('0','1','2',"3","4")
	combo375.current(0)
	combo375.grid(row = 2,column = 1, sticky= tk.W , padx =5,pady = 5)

	def sendtransaction():
		currenttime = datetime.datetime.now()
		transaction_id = int(time.time())
		transaction_date = currenttime.strftime("%d-%m-%Y")
		a = int(combo750.get())
		b = int(combo375.get())
		user_license = driver_license1.get()
		quantity = 750*a + 375*b
		total = quantity+upper
		allow = 1500 - upper
		if total <= 1500 :
			with open("transaction_data.csv",'a',newline = "") as f :
				dict_writer = DictWriter(f,fieldnames = ['Driver License','Transaction Id', 'Transaction Date','Quantity'])
				if os.stat('transaction_data.csv').st_size == 0 :
					dict_writer.writeheader()
				dict_writer.writerow({
					'Driver License': user_license ,
					'Transaction Id':transaction_id, 
					'Transaction Date':transaction_date,
					'Quantity' : quantity
					})
			messagebox.showinfo('','Transaction Successfull')

		elif allow > 0 : 
			messagebox.showerror(" ","Maximum {} ml is allow. Please reselect appropriate option ". format(allow)) 

		else : 
			messagebox.showinfo(" ","Maximum quantity for 30 days already achieved !") 


	New_Transaction = ttk.Button(toplabelframe3, text = "Submit" ,command = sendtransaction) 
	New_Transaction.grid(row= 6 , column = 0, padx =50,pady = 5)

	back = ttk.Button(toplabelframe3, text = "Back" ,command = top.destroy) 
	back.grid(row= 6 , column = 1, padx =50,pady = 5)

	top.mainloop() 
	

submit_button1 = ttk.Button(labelframe2, text = "Submit" ,command = transact) 
submit_button1.grid(row= 3 , column = 1 , padx =5,pady = 5)

def cleardata1():
	driver_license_entrybox1.delete(0,tk.END)	

clear_button1 = ttk.Button(labelframe2, text = "Clear" ,command = cleardata1) 
clear_button1.grid(row= 3 , column = 2, padx =5,pady = 5)

labelframe3 = ttk.LabelFrame(window, text="User Data",height = 400,width = 400)  
labelframe3.grid(row=5)

cols = ('FirstName','Last Name','Email','Phone',"Driver's License","State")
listBox = ttk.Treeview(labelframe3, columns=cols, show='headings')


for col in cols:
    listBox.heading(col, text=col)    
listBox.grid(row=2)

canvas = tk.Canvas(window,height= 50,width = 400)
canvas.grid(row=6)

window.mainloop()

