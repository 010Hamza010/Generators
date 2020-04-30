from random import choice
from string import ascii_letters as letters, digits as numbrs, punctuation as sp
from os import system,name


StrengthStrings = [letters,letters+numbrs,letters+numbrs+sp]

def GeneratePass(L,S):
	NewList = [char for char in StrengthStrings[S-1]]
	Password = ''
	i=0
	while i<=L-1:
		c = choice(NewList)
		NewList.remove(c)
		Password+=c
		i+=1
	with open('Password.txt','w') as file:
		file.write(Password)
	return Password

if name == 'posix':
	system('clear')
elif name == 'nt':
	system('cls')

print('-'*30, ' Password Generator ', '-'*30)

while True:
	while True:
		Length = input('Password Length: ')
		try:
			Length = int(Length)
		except:
			pass
		else:
			if Length > 0:
				break

	print('[3]Strong\n[2]Normal\n[1]Weak')

	while True:
		PasswordStrength = input('Chose A Strength: ')
		try:
			PasswordStrength = int(PasswordStrength)
		except:
			pass
		else:
			if PasswordStrength in range(1,4):
				break
	print('\n'+GeneratePass(Length,PasswordStrength)+'\n')

	while True:
		print('[O]ther one\n[M]ore\n[E]xit')
		ToDo = input('What To Do: ').lower()
		if ToDo in ['o','m','e']:
			if ToDo == 'o':
				print('\n'+GeneratePass(Length,PasswordStrength)+'\n')
			if ToDo == 'm':
				break
			if ToDo == 'e':
				exit()