print("Program starting.")
word=str(input("Insert a closed compound word: "))
len=len(word)
Firstcharacter=word[0]
Reverse=word[::-1]
print(f"The word you inserted is '{word}' and in reverse it is '{Reverse}'")
print(f"The inserted word length is {len} ")
print(f"Last character is '{word[len-1]}'")
print(f"Take substring from the inserted word by inserting...")
start=int(input("1) Starting point: "))
end=int(input("2) Ending point: "))
step=int(input("3) Step size: "))
print(f"The word '{word}' sliced to the defined substring is '{word[start:end:step]}'\nProgram ending.")
