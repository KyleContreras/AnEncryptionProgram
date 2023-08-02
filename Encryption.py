# Simple encryption program.


def Main():

    action = input("Enter 'e' to encrypt, 'd' to decrypt, or 'q' to exit: ")
    taskToDo = None
    
    if action == 'q' or action == 'Q':
        return print("Exiting application")
    elif action == 'e' or action == 'E' or action == 'd' or action == 'D':
        taskToDo = EncryptOrDecrypt(action)
    else:
        print("Please enter the correct the correct value.")
        Main()
    
    userMsg    = str(input("Enter your message: "))
    userMsg    = userMsg.upper()

    newString = str(WorkOnMsg(taskToDo, userMsg))
    print(newString)

    Main()
    

def EncryptOrDecrypt(actionToDo):
    action = actionToDo
    task = ''

    if action == 'e' or action == 'E':
        task = "encrypt"
        return task
    elif action == 'd' or action == 'D':
        task = "decrypt"
        return task
    else:
        print("Please enter the correct the correct value.")
        Main()


def WorkOnMsg(action, msg):
    newMsg = ''
    firstSpot = 0
    scndSpot = 0
    firstList = None
    secondList = None

    # Both Lists are capitalized in the assignment sheet, so I left them as is.  
    encryptedList = ["S", "E", "2", "R", "L", ".", "1", "W", "5", "A", "0", "Z",
                   "8", "D", "7", "H", "4", "B", "9", "M", "6", "J", "X", "3",
                   "F", "T", "N", "V", "Q", "G", "P", "U", "O", "Y", "C", "K",
                   "I"]

    decryptedList = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
                   "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X",
                   "Y", "Z", ".", "1", "2", "3", "4", "5", "6", "7", "8", "9",
                   "0"]

    if action == "encrypt":
        firstList = decryptedList
        secondList = encryptedList
    else:
        firstList = encryptedList
        secondList = decryptedList

    for x in msg:
        if x in firstList:
            firstSpot = firstList.index(x)
            scndSpot = secondList[firstSpot]
            newMsg = newMsg + scndSpot
        else:
            newMsg = newMsg + str(x)

    return newMsg

Main()



