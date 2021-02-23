#importing stuff
import tkinter as tkinter
from tkinter import ttk
from tkinter import *
from tkinter import filedialog
import os
import win32api
from PIL import Image, ImageTk
import datetime
import win32com.client

def backup():
	#do backup stuff
	print(delaymenu.get())
	pass
def start():
	#setting window size
	root = Tk()
	root.geometry('400x350')
	root.resizable(0,0)
	root.title("Backup Files")
	frame = Frame(root)

	#variables
	filetobackup = StringVar()
	drivelocation = StringVar()
	timeslist = ["1 min", "5 min", "10 min", "30min", "1 hour", "6 hours", "12 hours", "1 day", "1 week", "1 month", "1 year"]
	#displays files

	global folder_path
	def browsebutton():

		filename = filedialog.askdirectory()
		folder_path.set(filename)
		with open("assets/filestobackup.fbk", "w") as temp2:
			temp2.write(filename)
		
	folder_path = StringVar()
	lbl1 = Label(master=root,textvariable=folder_path)
	lbl1.pack()
	button2 = Button(text="Select Folder To Backup", command=browsebutton)
	button2.pack()
	lbl2 = Label(root, text = "Backup Every:")
	lbl2.pack()
	global delaymenu
	delaymenu = ttk.Combobox(root, values = timeslist, state = "readonly", width=5)
	delaymenu.pack(fill='x')
	button3 = Button(text="Backup", command=backup)
	button3.pack()

	#idek what this does but i need it so like its here
	root.mainloop() 

#read from textfile, if doesnt exit:
try:
	with open("assets/filestobackup.fbk") as filelistfile:
		notes = (filelistfile.readlines())
		line1 = str(notes[0])
		print(line1)
		
except:	
	print("Creating File...")
	try:
		with open("assets/filestobackup.fbk", "x") as temp:
			pass
	except:
		with open("assets/filestobackup.fbk", "w") as temp:
			temp.write(" ")
			
start()
#if does:
#backup()