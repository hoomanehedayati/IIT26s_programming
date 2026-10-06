print("Program starting.\n")
x=0
y=0
while True:
  word=input("Insert a word (empty stops):")
  if word == "":
    break
  x += 1
  y += len(word)
print(f"\nYou inserted:\n{x} words\n{y} characters\n")
print("\nProgram ending.")