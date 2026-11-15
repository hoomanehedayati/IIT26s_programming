
def read(filename):
  filehandler=open(filename,"r")
  content=filehandler.read()
  filehandler.close()
  return content
def write(filename,destination):
  content=read(filename)
  filehandler2=open(destination,"w")
  filehandler2.write(content)
  filehandler2.close()

def main():
  print("Program starting.")
  print("This program can copy a file.")
  filename=input("Insert source filename:")
  destination=input("Insert destination filename:")
  print(F"Reading file '{filename}' content.")
  read(filename)
  print("File content ready in memory.")
  print(F"Writing content into file {destination}.")
  write(filename,destination)
  print("Copying operation complete.")
  print("Program ending.")

main()