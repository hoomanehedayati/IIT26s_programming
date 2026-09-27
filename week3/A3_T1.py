print("Program starting.")
print("Insert two integers.")
first=int(input("Insert first integer:"))
second=int(input("Insert second integer:"))
print("Comparing inserted integers.")
if first > second :
  print("First integer is greater.")
elif second > first :
  print("Second integer is greater.")
elif second == first :
  print("Integers are the same")
print()
print("Adding integers together")
sum = first + second
print(f'{first} + {second} = {sum}\n')
print("Checking the parity of the sum...")
if sum%2 == 0:
  print("Sum is even.")
elif sum%2 ==1:
  print("Sum is odd.")
print("Program ending.")
