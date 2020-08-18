import pyttsx3
import os
#importing module is necessary when you are using one module otherwise error pops up!!


engine  = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty("voice", voices[1].id )

pyttsx3.speak("Welcome to my tools")


#experimenting with the software

print("Open Google Chrome\n")
print("Open Notepad\n")
print("Open Windows Media Player\n")
print("Open Youtube\n")
print("Type quit if you want to exit the software")
print()

while True:
	
	print("Type Your Choice: \n")
	p = input()
	print("\n")
	print("Progressing...")
	print("May take sometime...")

	p.lower()#By this there will be no error if someone types in lower case!!


#first we converted 'p' into an integer it was in string type
#learnt more about if and else statements so did some experiments lol
#ensure that two functions don't have a same word in it otherwise the command gets fucked up.

	

	if 'notepad' in p:
		pyttsx3.speak("launching notepad")
		os.system("start notepad")


	elif ('google' in p) or ('chrome' in p):
		pyttsx3.speak("Launching Chrome") 
		os.system("start chrome")

	elif 'player' in p:

		pyttsx3.speak("launching Windows Media Player")
		os.system("start wmplayer")

	elif 'youtube' in p:

		pyttsx3.speak("launching Youtube")
		os.system("start chrome  www.youtube.com")
 
	elif 'quit' in p:
		break

	else:

		print("This Function is not supported in this software")
		pyttsx3.speak("Sorry, I don't have a solution for this please Search the google")

		a = input("Do you want to open google?")
		a.lower()
		print("Type Yes to Open")
		print("Type No to deny")
		if 'yes' in a:
			pyttsx3.speak("Launching chrome")
			os.system("start chrome   www.google.com")
		else:
			print("Thanks for using!") 
		

	pyttsx3.speak("Thanks for using")

