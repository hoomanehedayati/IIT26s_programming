def readfile(filename):
  file=open(filename,"r")
  return file
def analyse(filename):
  content=readfile(filename)
  total=0
  count=0
  row=content.readline()
  greatestnum=int(row)
  while row != "":
    count+=1
    total+=int(row)
    if int(row) > greatestnum:
      greatestnum=int(row)
    row=content.readline()  
  avg=total/count
  content.close() 
  return count,total,greatestnum,avg 

def main():
  print("Program starting.")
  filename=input("Insert filename:")
  print("#### Number analysis - START ####")
  print(f'File "{filename}" results:')
  print("Count;Sum;Greatest;Average")
  answers=analyse(filename)
  print(f"{answers[0]};{answers[1]};{answers[2]};{answers[3]:.2f}")
  print("")
  print("#### Number analysis - END ####")
  print("Program ending.")
main()  
