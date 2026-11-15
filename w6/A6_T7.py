
def savefile(file, words):
    filehandler = open(file, "w")
    for i in range(len(words)):
        filehandler.write(words[i] + "\n")
    filehandler.close()
def turnword(word):
    newword = ""
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    alphabet2 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    for i in word:
        if i in alphabet:
            index = alphabet.index(i)
            if index < 13:
                newindex = index + 13
            else:
                newindex = index - 13
            newword += alphabet[newindex]

        elif i in alphabet2:
            index = alphabet2.index(i)
            if index < 13:
                newindex = index + 13
            else:
                newindex = index - 13
            newword += alphabet2[newindex]
        else:
            newword += i
    return newword
def main():
    print("Travel starting.")
    locations = ["home", "Galba's palace", "Otho's palace","Vitellius' palace", "Vespasian's palace"]
    filehandler=open("w6/player_progress.txt","r")
    lines=filehandler.readlines()
    filehandler.close()
    lastline=lines[-1].strip().split(";")
    currentloc=int(lastline[0])
    nextloc=int(lastline[1])
    passphrase=lastline[2]
    print(f"Currently at {locations[currentloc]}")
    print(f"Travelling to {locations[nextloc]}...")
    print(f"...Arriving to {locations[nextloc]}.")
    print("Passing the guard at the entrance.")
    print(f'"{turnword(passphrase).capitalize()}!"')
    print("Looking for the message in the palace...")
    filenamee=str(nextloc)+"_"+passphrase+".gkg"
    filehandler=open(filenamee,"r")
    message=filehandler.readline().strip()
    filehandler.close()
    print("Ah, there it is! Seems cryptic.")
    print("[Game] Progress autosaved!")
    print("Deciphering Emperor's message...")
    plainmessage=turnword(message)
    newfilename=str(nextloc)+"_"+plainmessage+".txt"
    savefile(newfilename,[plainmessage])
    print("Looks like I've got now the plain version copy of the Emperor's message.")
    if nextloc < 4:
        newpassphrase = input("Enter next passphrase: ")
        filehandler = open("player_progress.txt", "a")
        filehandler.write(str(nextloc) + ";" + str(nextloc + 1) + ";" + newpassphrase + "\n")
        filehandler.close()
    print("Time to leave...")
    print("Travel ending.")
main()
