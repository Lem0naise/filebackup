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
import subprocess

try:
	os.mkdir(os.getcwd() + "\\assets\BackedUpFiles")
	print("BackedUpFiles Folder created")
except:
	pass

root = Tk()
root.geometry('400x320')
root.title("Backup Files")
root.resizable(0,0)
frame = Frame(root)

def backup():
	global backuppath
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
	elif delaymenu.get() == "1 month":
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
	tasktriggertime = 1

	trigger = task_def.Triggers.Create(tasktriggertime)
	trigger.StartBoundary = start_time.isoformat()

	#change repitition to whatever time selected
	RepPattern = trigger.Repetition
	if mtw<60:
		RepPattern.Interval = "PT" + str(int(mtw)) + "M"
	else:
		RepPattern.Interval = "PT" + str(int(mtw/60)) + "H"

	# Create action
	TASK_ACTION_EXEC = 0
	action = task_def.Actions.Create(TASK_ACTION_EXEC)
	action.ID = 'File Backup'
	action.Arguments = ""

	location1 = '"' + os.getcwd() + '\\assets\\file_1.bat' + '"'
	action_path_var = '"' + location1 + '"'
	action.Path = location1
	#put stuff



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
	try:
		with open("assets/file_1.bat", "x") as temp:
			pass
	except:
		pass

	#reads file
	try:
		with open("assets/filestobackup.fbk") as filelistfile:
			notes = (filelistfile.readlines())
			line1 = str(notes[0])
			
	except:	
		print("Creating File...")
		try:
			with open("assets/filestobackup.fbk", "x") as temp:
				pass
		except:
			with open("assets/filestobackup.fbk", "w") as temp:
				temp.write(" ")
	splitlocation1 = [s for s in line1.split("/")]
	global isfile2
	try:			
		if location2 == os.getcwd() + "\\assets\\BackedUpFiles\\" :
			pass
		else:
			location2 = filename2
	except UnboundLocalError:
		try:
			location2 = filename2
			isfile2 = True
			
		except NameError:
			isfile2 = False
			location2 = os.getcwd() + "\\assets\\BackedUpFiles\\" 
			
	
	if isfile2 == False:
		print("shouldn't add bracket")
		fn = 'xcopy "' + line1 + '" "' + location2 + splitlocation1.pop() + '" ' + "/Y /e /i"
	else:
		fn = 'xcopy "' + line1 + '" "' + location2 + "/" + splitlocation1.pop() + '" ' + "/Y /e /i"

	with open("assets/file_1.bat", "w") as temp:
		temp.write(fn)

	subprocess.call([r'assets\\file_1.bat'])

def gotostart():
	try:
		start()
	except:
		print("Could not start")
def helpmenu():
	#deleting buttons and labels and combobox

	try:
		lbl1.destroy()
	except:
		pass
	try:
		button2.destroy()
	except:
		raise
	try:
		button4.destroy()
	except:
		raise
	try:
		lbl2.destroy()
	except:
		raise
	try:
		button3.destroy()
	except:
		raise
	try:
		help_icon_button.destroy()
	except:
		raise
	try:
		delaymenu.destroy()
	except:
		raise
	try:
		lbl69.destroy()
	except:
		pass

	#placing back button
	global button6
	button6 = Button(image=back_arrow, command = gotostart, borderwidth = 0)
	button6.place(x=0,y=290)

	#placing text
	global hlptxt1
	global hlptxt2
	global hlptxt3
	global hlptxt4
	global hlptxt5
	global hlptxt6

	hlptxt1 = Label(text="1. How do I pick a folder to backup?", borderwidth = 0, fg = "grey20")
	hlptxt1.place(x=200,y=20, anchor = "center")

	hlptxt2 = Label(text="Click on \'Select Folder\' to pick a directory to backup.", borderwidth = 0, fg = "grey50")
	hlptxt2.place(x=200,y=50, anchor = "center")

	hlptxt3 = Label(text="2. How do I chose the location of the backed up file?", borderwidth = 0, fg = "grey20")
	hlptxt3.place(x=200,y=100, anchor = "center")

	hlptxt4 = Label(text="""                     Click on \'Select Directory\' to pick where your file is backed up,
                     by default it is backed up to 'BackedUpFiles' in the 'assets' folder
	of where you installed the program.""", borderwidth = 0, fg = "grey50")
	hlptxt4.place(x=170,y=150, anchor = "center")

	hlptxt5 = Label(text="3. How do I pick how often the file is backed up?", borderwidth = 0, fg = "grey20")
	hlptxt5.place(x=200,y=210, anchor = "center")

	hlptxt6 = Label(text="""                   Click on the box labeled \'Time Between Backups:\' and pick how often
	you would like your file to be backed up.""", borderwidth = 0, fg = "grey50")
	hlptxt6.place(x=170,y=250, anchor = "center")

	credits = Label(text="""Created By Lemonaise and Ma1war3!""", borderwidth = 0, fg = "grey20")
	credits.place(x=200,y=300, anchor = "center")

def start():
	try:
		button6.destroy()
	except:
		pass
	try:
		hlptxt1.destroy()
	except:
		pass
	try:
		hlptxt2.destroy()
	except:
		pass
	try:
		hlptxt3.destroy()
	except:
		pass
	try:
		hlptxt4.destroy()
	except:
		pass
	try:
		hlptxt5.destroy()
	except:
		pass
	try:
		hlptxt6.destroy()
	except:
		pass
	try:
		creadits.destroy()
	except:
		pass
	#setting window size


	#importing images
	backupbtn = Image.open("assets\\Buttons&Text\\backup.png")
	backupbtn = backupbtn.resize((75,31), Image.ANTIALIAS)
	backupbutton = ImageTk.PhotoImage(backupbtn)

	selectfolderbtn = Image.open("assets\\Buttons&Text\\select_folder.png")
	selectfolderbtn = selectfolderbtn.resize((150,38), Image.ANTIALIAS)
	selectfolderbutton = ImageTk.PhotoImage(selectfolderbtn)

	selecttargetfolderbtn = Image.open("assets\\Buttons&Text\\select_directory.png")
	selecttargetfolderbtn = selecttargetfolderbtn.resize((150,38), Image.ANTIALIAS)
	selecttargetfolderbutton = ImageTk.PhotoImage(selecttargetfolderbtn)

	hlp_icon = Image.open("assets\\Buttons&Text\\help_icon.png")
	hlp_icon = hlp_icon.resize((26,26), Image.ANTIALIAS)
	help_icon = ImageTk.PhotoImage(hlp_icon)

	global back_arrow
	back_arrw = Image.open("assets\\Buttons&Text\\back_arrow.png")
	back_arrw = back_arrw.resize((29,29), Image.ANTIALIAS)
	back_arrow = ImageTk.PhotoImage(back_arrw)

	#variables
	filetobackup = StringVar()
	drivelocation = StringVar()
	global filenameactual
	filenameactual = ""
	global filedirectoryactual
	filedirectoryactual = "BackedUpFiles"
	timeslist = ["1 min", "5 min", "10 min", "30min", "1 hour", "6 hours", "12 hours", "1 day", "1 week", "1 month", "1 year"]
	global lbl1
	global button2
	global lbl3
	global button4
	global lbl2
	global button3
	global help_icon_button
	global delaymenu
	global lbl69
	#displays files

	global folder_path
	global filename2 
	def browsebutton():
		global filenameactual
		filename = filedialog.askdirectory()

		temp = [s for s in filename.split("/")]
		filenameactual = temp.pop()

		folder_path.set(filename)
		with open("assets/filestobackup.fbk", "w") as temp2:
			temp2.write(filename)
		global lbl1
		lbl1 = Label(master=root,text="' " + filenameactual + " ' will be backed-up to:" + "' " + filedirectoryactual + " '")
		lbl1.place(x=200, y=20, anchor = "center")

	def browsebutton2():
		global lbl69
		global filename2
		filename2 = filedialog.askdirectory()

		folder_path_target.set(filename2)
		with open("assets/filestoupback.fbk", "w") as temp2:
			temp2.write(filename2)

		global location2
		#setting location2 if selected
		location2 = filename2 

		temp = [s for s in location2.split("/")]
		filedirectoryactual = temp.pop()
		lbl1.destroy()
		lbl69 = Label(master=root,text="'" + filenameactual + "' will be backed-up to: " + "'" + filedirectoryactual + "'")
		lbl69.place(x=200, y=20, anchor = "center")


		
	folder_path = StringVar()
	button2 = Button(image = selectfolderbutton, command=browsebutton, borderwidth = 0)
	button2.place(x=200, y=80, anchor = "center")
		
	folder_path_target = StringVar()
	button4 = Button(image = selecttargetfolderbutton, command=browsebutton2, borderwidth = 0)
	button4.place(x=200, y=120, anchor = "center")

	lbl2 = Label(root, text = "Time Between Backups:")
	lbl2.place(x=200, y=180, anchor = "center")
	global delaymenu
	delaymenu = ttk.Combobox(root, values = timeslist, state = "readonly", width = 60)
	delaymenu.place(x=200, y=200, anchor = "center")
	button3 = Button(image = backupbutton, command=backup, borderwidth = 0)
	button3.place(x=200, y=230, anchor = "center")

	help_icon_button = Button(image = help_icon, borderwidth = 0, command = helpmenu)
	help_icon_button.place(x=390, y=305, anchor = "center")

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