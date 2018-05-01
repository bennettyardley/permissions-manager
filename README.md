# permissions-manager
A cool way to manage permission in Linux by assigning users temporary rights, when they need it. In a real world situation the database would be hosted with the server and the client would have to connect, but both are local for this project.

# client.py
Allows a user to request permissions to a certain folder. Simply input the folder name, permission needed, time needed, and reason. The server will respond to the request and automatically assign and remove the permissions.

# GUI.py
A GUI for client.py that makes input a lot easier through folder dialouges, checkboxes, and inputs. 

# server.py
Allows an operator to accept or deny requests from users. Has error checking incase a user gave bad input and allows the server to send a reason for a denial so the user can change their request.

# permissionsmanager.pdf
A PowerPoint presentation explaining the Permissions Manager project 

## Requirments
None :D

## To Do
* ACL commands for server.py 
* Update from sqlite3 to mysql
