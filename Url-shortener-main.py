from pyshorteners import Shortener
import sys
import keyboard








def exit_and_restart():

	print("Press 'Enter' to covert more or press 'Esc' to exit: ")

	while True:
		try:
			if keyboard.is_pressed('ENTER'):
				print("Starting")
				User_interface()
				break
			if keyboard.is_pressed('Esc'):
				print("Exiting...")
				print("Have a nice day :) ")

				sys.exit(0)
				
		except:
			break



	

API_name=['1.TinyURL','2.Chilp.it','3.Da.gd','4.Git.io(Only Github urls)','5.Is.gd','6.Osdb.link','7.Qps.ru','8.NullPointer','9.Clck.ru']

s = Shortener()

def shortener_main():
	
	Link=input("Paste your link here: ")

	print()
	



	print("In which URL do you want to shorten the link: ")
	print('\n'.join(map(str, API_name)))

	API=input("Type the number here(Type 1 for default): ")


	if API=='1':
		Short_link=s.tinyurl.short(Link)
		print()
		print('Here is your link-->',  Short_link)
		print()
		exit_and_restart()

	elif API=='2':
		Short_link=s.chilpit.short(Link)
		print()
		print('Here is your link-->',  Short_link)
		print()
		exit_and_restart()

	elif API=='3':
		Short_link=s.dagd.short(Link)
		print()
		print('Here is your link-->',  Short_link)
		print()
		exit_and_restart()

	elif API=='4':
		Short_link=s.gitio.short(Link)
		print()
		print('Here is your link-->',  Short_link)
		print()
		exit_and_restart()

	elif API=='5':
		Short_link=s.isgd.short(Link)
		print()
		print('Here is your link-->',  Short_link)
		print()
		exit_and_restart()

	elif API=='6':
		Short_link=s.osdb.short(Link)
		print()
		print('Here is your link-->',  Short_link)
		print()
		exit_and_restart()

	elif API=='7':
		Short_link=s.qpsru.short(Link)
		print()
		print('Here is your link-->',  Short_link)
		print()
		exit_and_restart()

	elif API=='8':
		Short_link=s.nullpointer.short(Link)
		print()
		print('Here is your link-->',  Short_link)
		print()
		exit_and_restart()
	
	elif API=='8':
		Short_link=s.nullpointer.short(Link)
		print()
		print('Here is your link-->',  Short_link)
		print()
		exit_and_restart()
	
	elif API=='9':
		Short_link=s.clckru.short(Link)
		print()
		print('Here is your link-->',  Short_link)
		print()
		exit_and_restart()
	
	else:
		print()
		print("ERROR--->Please type the valid digit")
		print()
		exit_and_restart()








def User_interface():

	print("""
________________________________________________________________________________	
█▄─██─▄█▄─▄▄▀█▄─▄███▀▀▀▀▀██─▄▄▄▄█─█─█─▄▄─█▄─▄▄▀█─▄─▄─█▄─▄▄─█▄─▀█▄─▄█▄─▄▄─█▄─▄▄▀█
██─██─███─▄─▄██─██▀████████▄▄▄▄─█─▄─█─██─██─▄─▄███─████─▄█▀██─█▄▀─███─▄█▀██─▄─▄█
▀▀▄▄▄▄▀▀▄▄▀▄▄▀▄▄▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▀▄▀▄▀▄▄▄▄▀▄▄▀▄▄▀▀▄▄▄▀▀▄▄▄▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀
                                                           -Made by SidTheMiner""")


	print()
	
	

	user_input = input("Press Enter to start: ")
	user_input=True     
	
	if user_input == True:
		print()
		shortener_main()


User_interface()




        
        


