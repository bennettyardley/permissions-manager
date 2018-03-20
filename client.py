import sqlite3, getpass, time, uuid

conn = sqlite3.connect('requests.db')
c = conn.cursor()

def wait(randomID):
	while True:
		time.sleep(5)
		for row in c.execute("SELECT status FROM request WHERE randomID = ?", (randomID,)):
			status = row[0]
			break
		if status == '0':
			continue
		else:
			break
	print(status)
	request()

def request():
    package = []
    #NEED ERROR (GOOD VALUE) CHECKING
    folder = raw_input("Which Folder Do You Need Permissions To?: ")
    package.append(folder)
	#WHAT SHOULD DEFAULT BE
    permission = raw_input("What Permissions Do You Need? (Enter for Default): ")
    package.append(permission)
    length = raw_input("How Long Will You Need Access? (In Minutes): ")
    package.append(length)
    username = getpass.getuser()
    package.append(username)
    reason = raw_input("Why Do You Need Access? (Enter for Blank): ")
    package.append(reason)
    randomID = str(uuid.uuid4())
    package.append(randomID)
    status = '0'
    package.append(status)
    c.execute("INSERT INTO request VALUES (?,?,?,?,?,?,?)", package)
    conn.commit()
    wait(randomID)

def main():
	c.execute('''CREATE TABLE IF NOT EXISTS request
				(folder text, permission text, length text, username text, reason text, randomID text, status text)''')
	conn.commit()
	request()
main()
