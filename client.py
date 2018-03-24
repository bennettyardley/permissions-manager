import sqlite3, getpass, time, uuid

conn = sqlite3.connect('requests.db')
c = conn.cursor()

def wait(randomID):
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
	print("Server responded: " + status + "\n")
	conn = sqlite3.connect('requests.db')
    c = conn.cursor()
    c.execute("DELETE FROM request WHERE randomID = ?", (randomID,))
	conn.commit()
	conn.close()
	request()

def request():
	print("*"*36)
	print("*           New Request            *")
	print("*"*36)
	package = []
	folder = raw_input("Which Folder Do You Need Permissions To?: ")
	package.append(folder)
	permission = raw_input("What Permissions Do You Need? (ex. r-x or rw-): ")
	package.append(permission)
	length = raw_input("How Long Will You Need Access? (In Minutes): ")
	package.append(length)
	username = getpass.getuser()
	package.append(username)
	reason = raw_input("Why Do You Need Access? (Enter for Default): ")
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
	wait(randomID)

request()
