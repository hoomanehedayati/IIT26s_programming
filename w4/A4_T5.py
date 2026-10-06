print("Program starting.\n")
num1=int(input("Insert starting point:"))
num2=int(input("Insert stopping point:"))
num3=int(input("Insert inspection point:"))
if num1 >= num2:
  print("\nStarting point value must be less than the stopping point value.")
elif num3 < num1 or num3 > num2:
  print("\nInspection value must be within the range of start and stop.")
else: 
  print("First loop - inspection with break:")
  for i in range(num1, num2):
    if i == num3:
      break
    print(i,end=" ")
  print("\nSecond loop - inspection with continue:")
  for i in range(num1,num2):
    if i == num3:
      continue
    print(i,end=" ")
print("\nProgram ending.")    