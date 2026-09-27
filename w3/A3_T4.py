print("Program starting.")
name = input("This is a program with simple menu, where you can choose which operation the program performs.\n"
			 "Before the menu, please insert your name:")
print("Options\n1 - Print welcome message\n"
	"2 - Print the name backwards\n"
	"3 - Print the first character\n"
	"4 - Show the amount of characters in the name\n"
	"0 - Exit")
choice = int(input("Your choice:"))
if choice == 1:
  print(f'Welcome {name}!')
elif choice == 2:
  print(f'{name[::-1]}')
elif choice == 3:
  print(f'The first character in name {name} is {name[0]}')
elif choice == 4:
  print(len(name))
elif choice == 0:
  print("Exiting...")
else:
  print("Unknown choice")
print("Program ending.") 