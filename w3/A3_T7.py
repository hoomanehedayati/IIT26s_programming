print("Program starting.\nTesting decision structures.")
num=int(input("Insert an integer:"))
print("Options:\n1 - In one multi-branched decision\n2 - In multiple independent if-statements\n0 - Exit")
choice=int(input("Your choice:"))
if choice == 1:
  if num >= 400:
    num = num + 44
  elif 400 > num >= 200:
    num = num + 22
  elif 200 > num >= 100:
    num = num + 11
  print(f'Using one multi-branched decision structure.\nResult is {num}')
elif choice == 2:
  if num >= 400:
    num = num + 44
  if num >= 200:
    num = num + 22
  if num >= 100:
    num = num + 11
  print(f'Using multiple independent if-statements structure.\nResult is {num}')
elif choice == 0:
  print("Exiting...")
else:
  print("Unknown option.")
print("Program ending.")