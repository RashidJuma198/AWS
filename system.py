#System adm=inistration using Python
# Adding user 
import os

def new_user():
    confirm = "N"
    while confirm != "Y":
        username = input("Enter the username to add")
        print("Do you want to add "+username+" ?" + "(Y/N)")
        confirm = input().upper()
    os.system("sudo adduser ju" + username)
    
new_user()
        
        
        
        