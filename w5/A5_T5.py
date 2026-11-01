def insertword():
    word = input("Insert word: ")
    return word
def currentword(Word):
    print(f'Current word - "{Word}"')
def reserve(Word):
    print(f'Word reversed - "{Word[::-1]}"')
print("Program starting.")
Word = ""
while True:

  print("Options:\n1 - Insert word\n2 - Show current word\n3 - Show current word in reverse\n0 - Exit")
  choice = input("Your choice:")
  if choice =="1":
    word=insertword()
  elif choice =="2":
    currentword(word)
  elif choice =="3":
    reserve(word)
  elif choice =="0":
    print("Unknown option! try again.")   
    break 
  else:
    print("Unknown option! try again.")
print("\nProgram ending.")    