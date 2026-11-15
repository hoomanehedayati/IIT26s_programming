def savefile(file,words):
  filehandler=open(file,"w")
  for i in range (len(words)):
    filehandler.write(words[i]+"\n")
  filehandler.close()
def turnword(word):
  newword=""
  alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
  alphabet2 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
  for i in word:
    if i in alphabet:
      index=alphabet.index(i)
      if index < 13 :
        newindex=index+13
      else:
        newindex=index-13  
      newword+=alphabet[newindex]
    elif i in alphabet2:
      index=alphabet2.index(i)
      if index < 13 :
        newindex=index+13
      else:
        newindex=index-13  
      newword+=alphabet2[newindex]   
    else:
      newword+=i  
  return newword  
def main():
  newwordlist=[]
  print("Program starting.\n")
  print("Collecting plain text rows for ciphering.")
  word=input("Insert row(empty stops):")
  while word != "":
    content=turnword(word)
    newwordlist.append(content)
    word=input("Insert row(empty stops):")
  print("\n#### Ciphered text ####")  
  for i in range (len(newwordlist)):
    print(newwordlist[i]) 
  print("")    
  print("#### Ciphered text ####")
  file=input("Insert filename to save:")
  if file =="":
    print("File name not defined.\nAborting save operation.")
  else:
    savefile(file,newwordlist) 
    print("Ciphered text saved!") 
  print("Program ending.")   
main()    