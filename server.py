import sqlite3, threading

conn = sqlite3.connect('requests.db')
c = conn.cursor()

def removePermission(values):
    #REVERSE ACL COMMAND HERE
    print(values)

def task(i, values):
    print(values[i][3] + " requested access to " + values[i][0] + " with " + values[i][1] + " permissions for " + values[i][2] + " minutes becuase " + values[i][4])
    status = raw_input("Accept or Deny (A/D): ")
    randomID = values[i][5]
    if status == "A":
        print("Request Accepted")
        #ACL COMMAND HERE
        c.execute("UPDATE request SET status = 'Request Accepted' WHERE randomID = ?", ((randomID)))
        conn.commit()
        time = float(values[i][2])/0.0166667
        t = threading.Timer(time, removePermission, [values[i]])
        t.start()
    if status == "D":
        reason = raw_input("Request Denied, Give Reason: ")
        c.execute("UPDATE request SET status = ? WHERE randomID = ?", ((reason), (randomID)))
        conn.commit()

def main():
    while True:
        c.execute("SELECT * FROM request")
        values = c.fetchall()
        i = 0
        for j in values:
            if j[6] == '0':
                task(i, values)
            i = i + 1
        time.sleep(30)

main()
