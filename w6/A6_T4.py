def amount(filename):
    file = open(filename, "r")
    amountofnames = 0
    for row in file:
        amountofnames += 1
    file.close()
    return amountofnames


def shortlong(filename):
    filehandler = open(filename, "r")
    listname = []
    for name in filehandler:
        cleaned_name = name.strip()
        if cleaned_name != "":
            listname.append(cleaned_name)
    if not listname:
        return "", ""
    shoetestname = min(listname, key=len)
    longestname = max(listname, key=len)
    filehandler.close()
    return shoetestname, longestname
def avg(filename):
    sum=0
    numofrows=0
    filehandler2=open(filename,"r")
    rowss=filehandler2.readline()
    while rowss != "":
        sum += len(rowss.strip())
        numofrows+=1
        rowss=filehandler2.readline()
    mean=sum/numofrows
    filehandler2.close()   
    return mean 
def main():
    print("Program starting.")
    print("This program analyses a list of names from a file.")
    filename = input("Insert filename to read: ")
    numberOfNames = amount(filename)
    shortestname, longestname = shortlong(filename)
    average=avg(filename)
    print(numberOfNames)
    print(f"The shortest name is {shortestname} and longest name is  {longestname}")
    print(f"averange length is {average:.2f}")
main()