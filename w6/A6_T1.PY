def readfile(filename):
  filehandler=open(filename,"r",encoding="UTF-8")
  content=""
  row=filehandler.readline()
  while row != "":
    content+=row
    row=filehandler.readline()
    filehandler.close()
  return content
def main():
  print("program starting.")
  print("This program can read a file.")
  filename=input("Insert filename:")
  filecontent=readfile(filename)
  print(F'#### START "{filename}" ####')
  print(filecontent)
  print(F'#### END "{filename}" ####')
  print("program ending")
main()  