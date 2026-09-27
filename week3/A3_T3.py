print("Program starting.")
name = input("This is a program with simple menu, where you can choose which operation the program performs.\nBefore the menu, please insert your name:")
print("\nOptions:\n 1 - Print welcome message\n 0 - Exit")
choose=int(input("Your choice:"))
if choose == 1:
  print(f'Welcome {name}!')
elif choose == 0:
  print("Exiting...")
else:
  print("Unknown option.")
print("Program ending.")