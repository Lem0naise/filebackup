#importing stuff
import datetime
import win32com.client
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
	global mtw
	#do backup stuff
	print(delaymenu.get())
	if delaymenu.get() == "1 min":
		mtw = 1
	elif delaymenu.get() == "5 min":
		mtw = 5
	elif delaymenu.get() == "10 min":
		mtw = 10
	elif delaymenu.get() == "30 min":
		mtw = 30
	elif delaymenu.get() == "1 hour":
		mtw = 60
	elif delaymenu.get() == "6 hours":
		mtw = 360
	elif delaymenu.get() == "12 hours":
		mtw = 720
	elif delaymenu.get() == "1 day":
		mtw = 1440
	elif delaymenu.get() == "1 week":
		mtw = 10080
	elif delaymenu.get() == "1 month (30 days)":
		mtw = 43200
	elif delaymenu.get() == "1 year":
		mtw = 525600

	#adds backup task an dat
	scheduler = win32com.client.Dispatch('Schedule.Service')
	scheduler.Connect()
	root_folder = scheduler.GetFolder('\\')
	task_def = scheduler.NewTask(0)

	# Create trigger
	
	#change minutes to whatever time selected
	start_time = datetime.datetime.now() + datetime.timedelta(minutes=mtw)
	TASK_TRIGGER_TIME = 1
	trigger = task_def.Triggers.Create(TASK_TRIGGER_TIME)
	trigger.StartBoundary = start_time.isoformat()

	# Create action
	TASK_ACTION_EXEC = 0
	action = task_def.Actions.Create(TASK_ACTION_EXEC)
	action.ID = 'File Backup'
	action.Path = 'xcopy.exe'
	#put stuff
	action.Arguments = '""'

	# Set parameters
	task_def.RegistrationInfo.Description = 'Backup Folder'
	task_def.Settings.Enabled = True
	task_def.Settings.StopIfGoingOnBatteries = False

	# Register task
	# If task already exists, it will be updated
	TASK_CREATE_OR_UPDATE = 6
	TASK_LOGON_NONE = 0
	root_folder.RegisterTaskDefinition(
		'Backup Folder',  # Task name
		task_def,
		TASK_CREATE_OR_UPDATE,
		'',  # No user
		'',  # No password
		TASK_LOGON_NONE)


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