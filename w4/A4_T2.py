print("Program starting.\n")
num1 = int(input("Insert starting value: "))
num2 = int(input("Insert stopping value: "))
print("Starting for-loop:")
for i in range (num1, num2 + 1):
  if i == num2:
    print(i, end ="")
  else:
    print(i, end =" ")

print("\nProgram ending.")
