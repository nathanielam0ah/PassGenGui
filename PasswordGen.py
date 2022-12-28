#!/usr/bin/env python3
import random, string

def GetLength(): #Receives desired length
	length=input("Type the desired length (x to exit): ")
	if length=="x": exit()
	return int(length) if length.isdigit() else 0

def Generator(length=8): #Generates random ascii string
	printable=f"{string.ascii_letters}{string.ascii_letters.upper()}{string.digits}{string.punctuation}"
	printable=list(printable)
	random.shuffle(printable)
	initPassword=random.choices(printable,k=length)
	initPassword="".join(initPassword)
	return initPassword

if __name__ == "__main__":
	while 1:
		passwd_length=GetLength()
		if passwd_length==0:
			passwd=Generator()
			print(f'password (default=8):\t\t{passwd}')
		else:
			passwd=Generator(passwd_length)
			print(f'password ({str(len(passwd))}):\t\t{passwd}')