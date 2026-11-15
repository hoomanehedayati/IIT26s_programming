def writefile(filename,fname,lanme):
  filehandler=open(filename,"w")
  filehandler.write(fname + "\n")
  filehandler.write(lanme+"\n")
def main():
  print("Program starting.")
  fname=input("Insert first name:")
  lname=input("Insert last name:")
  filename=input("Insert filename:")
  writefile(filename,fname,lname)
  print("Program ending.")
main()  