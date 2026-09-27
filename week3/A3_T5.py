print("Program starting.")
print("\nOptions:\n1 - Celsius to Fahrenheit \n2 - Fahrenheit to Celsius \n0 - Exit")
choice = int(input("Your choice:"))
if choice == 1: 
  cel=float(input("Insert the amount of Celsius:"))
  CtoF= cel* 9/5 + 32
  print(f'{cel}c equals to {CtoF}F')
elif choice == 2: 
  Fahrenheit=float(input("Insert the amount of Fahrenheit:"))
  FtoC= (Fahrenheit-32)/1.8
  print(f'{Fahrenheit}F equals to {FtoC}C')
print("Program ending.")
