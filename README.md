# permissions-manager
A cool way to manage permission in Linux by assigning user temporary rights, when they need it. In a real world situation the database would be hosted with the server and the client would have to connect, but both are local.

# client.py
Allows a user to request permissions to a certain folder

# server.py
Allows a operator to accept or deny requests from users

## To Do
* Add error checking for the inputs in client.py and GUI.py
* Set some default values for client.py
* GUI with tkinter
* ACL commands for server.py 
* Delete Record once it is finished, a problem because the client wont see the status in time and it only will get deleted when you accept the request
* Improve the readme with required packages and more details
* Improve functions for easier to read code
