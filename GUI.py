from tkinter import *
import tkFileDialog as filedialog
import ScrolledText, sqlite3, getpass, time, uuid

def closeStatusWindow(randomID):
    global statusGUI
    statusGUI.destroy()

    conn = sqlite3.connect('requests.db')
    c = conn.cursor()
    c.execute("DELETE FROM request WHERE randomID = ?", (randomID,))
    conn.commit()
    conn.close()

def createRequest(randomID):
    global statusGUI
    statusGUI.destroy()

    conn = sqlite3.connect('requests.db')
    c = conn.cursor()
    c.execute("DELETE FROM request WHERE randomID = ?", (randomID,))
    conn.commit()
    conn.close()

    requestWindow()

def statusWindow(randomID):
    while True:
        time.sleep(5)
        conn = sqlite3.connect('requests.db')
        c = conn.cursor()
        for row in c.execute("SELECT status FROM request WHERE randomID = ?", (randomID,)):
            status = row[0]
            break
        if status == '0':
            conn.close()
            continue
        else:
            break

    global statusGUI
    statusGUI = Tk()

    statusLabel = Label(statusGUI, text="Server Responded:  " + str(status))
    statusLabel.pack()

    closeButton = Button(statusGUI, text="Close", command= lambda: closeStatusWindow(randomID)).pack()
    newRequest = Button(statusGUI, text="New Request", command= lambda: createRequest(randomID)).pack()

    statusGUI.mainloop()

def request(permission, length, reason):
    package = []

    global directory
    folder = directory
    package.append(folder)

    package.append(permission)
    package.append(length)

    username = getpass.getuser()
    package.append(username)

    package.append(reason)

    randomID = str(uuid.uuid4())
    package.append(randomID)

    status = '0'
    package.append(status)

    print("\nSending Request To Server\n")
    conn = sqlite3.connect('requests.db')
    c = conn.cursor()
    c.execute("INSERT INTO request VALUES (?,?,?,?,?,?,?)", package)
    conn.commit()
    conn.close()

    statusWindow(randomID)

def getDirectory():
    global directory
    directory = filedialog.askdirectory()

def getInput():
    global readVar
    global writeVar
    global executeVar
    read = readVar.get()
    write = writeVar.get()
    execute = executeVar.get()

    permList = []

    if read == 0:
        permList.append("-")
    if read == 1:
        permList.append("r")
    if write == 0:
        permList.append("-")
    if write == 1:
        permList.append("w")
    if execute == 0:
        permList.append("-")
    if execute == 1:
        permList.append("x")
    permissions = ''.join(permList)

    global timeNeededEntry
    global textfield
    minutes = timeNeededEntry.get()
    reason = textfield.get(1.0, END)

    global requestDialouge
    requestDialouge.destroy()

    request(permissions, minutes, reason)

def requestWindow():
    global requestDialouge
    requestDialouge = Tk()

    openButton = Button(requestDialouge, text="Open Folder", command=getDirectory).pack()

    global readVar
    readVar = IntVar()
    readButton = Checkbutton(requestDialouge, text="Read", variable=readVar).pack()
    global writeVar
    writeVar = IntVar()
    writeButton = Checkbutton(requestDialouge, text="Write", variable=writeVar).pack()
    global executeVar
    executeVar = IntVar()
    executeButton = Checkbutton(requestDialouge, text="Execute", variable=executeVar).pack()

    timeNeededLabel = Label(requestDialouge, text="Time Needed (Minutes): ")
    timeNeededLabel.pack()
    global timeNeededEntry
    timeNeededEntry = Entry(requestDialouge)
    timeNeededEntry.pack()

    reasonLabel = Label(requestDialouge, text="Reason: ")
    reasonLabel.pack()
    global textfield
    textfield = ScrolledText.ScrolledText(requestDialouge)
    textfield.pack()

    submitButton = Button(requestDialouge, text="Submit Request", command=getInput).pack()

    requestDialouge.mainloop()

requestWindow()
