#import os
#Using os module to list the number of files in our project

#os.system("ls")

import subprocess

#Running subprocess with one argument
#subprocess.run(['ls'])

#Running subprocess with two argument

#subprocess.run(["ls","-l"])

#Running subprocess with three argument

#subprocess.run(["ls","-l","README.md"])

#Retrieving system information using subprocess

command = "uname"
commandArgument = "-a"

print(f'I am Gathering information using {command} command with {commandArgument} argument')

subprocess.run([command,commandArgument])

#Getting disk info

subprocess.run(["df"])

#Gathering active process information 

command = "ps"
commandArg = "-x"

print (f'Gathering active process information  using command : {command} {commandArg}') 
subprocess.run([command,commandArg])