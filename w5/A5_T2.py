def frameword(pWord):
  print("*"*(len(pWord)+4))
  print(f"* {pWord} *")
  print("*"*(len(pWord)+4))
  return None
def main():
  print("Program starting.")
  word = input("Insert word:")
  frameword(word)
  print("Program ending.")
  return None
main()
