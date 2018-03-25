import sqlite3, threading, time

conn = sqlite3.connect('requests.db')
c = conn.cursor()

def removePermission(values):
    #REVERSE ACL COMMAND HERE
    print(values)

def task(i, values):
    print("\n" + values[i][3] + " requested access to " + values[i][0] + " with " + values[i][1] + " permissions for " + values[i][2] + " minutes becuase " + values[i][4])
    try:
        float(values[i][2])
        status = raw_input("Approve? (y/n): ")
    except:
        status = "n2"
    randomID = values[i][5]
    if status == "y":
        print("Request Accepted")
        #ACL COMMAND HERE
        c.execute("UPDATE request SET status = 'Request Accepted' WHERE randomID = ?", ((randomID,)))
        conn.commit()
        time = float(values[i][2])/0.0166667
        t = threading.Timer(time, removePermission, [values[i]])
        t.start()
    if status == "n":
        reason = raw_input("Request Denied, Give Reason: ")
        c.execute("UPDATE request SET status = ? WHERE randomID = ?", ((reason), (randomID)))
        conn.commit()
    if status == "n2":
        print("User did not give numbers for time")
        c.execute("UPDATE request SET status = 'Must use numbers for time' WHERE randomID = ?", ((randomID,)))
        conn.commit()

def main():
    c.execute('''CREATE TABLE IF NOT EXISTS request
				(folder text, permission text, length text, username text, reason text, randomID text, status text)''')
    conn.commit()
    print("Server Started! Waiting for Requests.")
    while True:
        c.execute("SELECT * FROM request")
        values = c.fetchall()
        i = 0
        for j in values:
            if j[6] == '0':
                task(i, values)
            i = i + 1
        time.sleep(5)

main()
