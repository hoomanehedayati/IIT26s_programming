print("Program starting.")
word = str(input("Insert first word:"))
char = str(input("Insert a character:"))
if char in word:
  print(f'Word "{word}" contains character "{char}"')
else:
  print(f'Word "{word}" doesn\'t contain character "{char}"')
secondword=str(input("Insert second word:"))
if word>secondword :
  print(f'The second word "{secondword}" is before the first word "{word}" alphabetically.')
elif secondword>word :
  print(f'The first word "{word}" is before the second word "{secondword}" alphabetically.')
else:
  print(f'Both inserted words are the same alphabetically,"{word}"')
  print("Program ending.")