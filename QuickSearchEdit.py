import re
import math
import os


def commodityInList(commodityInput, nameList, codeList):
    inUseBool = False
    nameIterator = 0
    while nameIterator<len(nameList):
        if nameList[nameIterator].lower()==commodityInput:
            inUseBool = True
            break
        elif codeList[nameIterator] == commodityInput:
            inUseBool = True
            break
        nameIterator+=1
    return inUseBool, nameIterator



def commodityExists(commodityInput):
    commodityList = []
    commodityFound = False
    commodityName = ""
    commodityCode = 0
    for row in open("commodityList.csv"):
        commodityList.append(row)
    i = 0
    while i<len(commodityList) and commodityFound == False:
        splitRowHolder = commodityList[i].split(":")
        for item in splitRowHolder:
            if item.lower()==commodityInput:
                commodityFound = True
                commodityCode = splitRowHolder[0]
                commodityName = splitRowHolder[1]
                break
            elif item == commodityInput:
                commodityFound = True
                commodityCode = splitRowHolder[0]
                commodityName = splitRowHolder[1]
                break
        i+=1
    if commodityFound == True:
        return commodityCode, commodityName
    else:
        return False, None
    
def quickSeachConstructor(nameList, codeList):
    nameList.insert(0,'Commodity Name')
    length = 16
    nameLength = 14
    commodityList = []
    quickList = [' Quick Search # ']
    codesList = [' Commodity Code ']

    quickSearch = ''
    for name in nameList:
        if len(name)>nameLength:
            nameLength = len(name)
    nameLength+=2
    quickSearch+=f" {'_'*((length)*2+(nameLength)+2)}\n"
    quickIterator = 1
    while quickIterator<6:
        quickList.append(f"{' '*7}{quickIterator}{' '*8}")
        codesList.append(f"{' '*5}{codeList[quickIterator-1]}{' '*6}")
        quickIterator+=1
    for name in nameList:
        left = math.floor((nameLength-len(name))/2)
        right = math.ceil((nameLength-len(name))/2)
        commodityList.append(f"{' '*left}{name}{' '*right}")
    quickSearchIterator = 0
    while quickSearchIterator<6:
        quickSearch+=f"|{quickList[quickSearchIterator]}|{commodityList[quickSearchIterator]}|{codesList[quickSearchIterator]}|\n|{('_'*(length))}|{('_'*(nameLength))}|{('_'*(length))}|\n"
        quickSearchIterator+=1
    if input(f"{quickSearch}\nDoes List look Correct? Y/N\t").lower() == 'n':
        return
    with open("eeee.csv", "w") as r:
        r.truncate()
        for line in quickSearch:
            r.write(line)




while True:
    quickSearchUserView = ''
    commodityNameList = []
    commodityCodeList = []
    quickSearchHolder = []
    for row in open('eeee.csv'):
        quickSearchHolder.append(row)
        quickSearchUserView+=row
    print(quickSearchUserView)
    NameCodeIterator = 3
    while NameCodeIterator<13:
        commodityNameList.append((re.findall(r'\S+',(((quickSearchHolder[NameCodeIterator]).split('|')))[2]))[0])
        commodityCodeList.append((re.findall(r'\S+',(((quickSearchHolder[NameCodeIterator]).split('|')))[3]))[0])
        NameCodeIterator+=2
    changeInput = input("What Quick Search Function Would You Like to Change?")
    if len(changeInput)<1 or (len(changeInput)==1 and changeInput.isnumeric()==False):
        input('Please Input Valid Amount of Characters\nPress Enter to Continue')
        os.system('cls||clear')
        continue
    if changeInput.isnumeric()==False:
        changeInput.lower()
    if changeInput == 'close':
        break
    changeInputBool, commodityLocation = commodityInList(changeInput, commodityNameList, commodityCodeList)
    if changeInput.isnumeric()==True and len(changeInput)==1:
        commodityLocation = int(changeInput)-1
    if changeInputBool == False and len(changeInput)>1:
        input('Commodity Does Not Exist in Quick Search\nPress Enter to Continue')
        os.system('cls||clear')
        continue
    commodityInput = input("Enter Commodity You Would Like to Switch too")
    if commodityInput.isnumeric()==False:
        commodityInput.lower()
    commodityInputBool = commodityInList(commodityInput, commodityNameList, commodityCodeList)
    if commodityInputBool[0] == True:
        input('Commodity Already Exists in Quick Search\nPress Enter to Continue')
        os.system('cls||clear')
        continue
    code, name = commodityExists(commodityInput)
    if code == False:
        input(f"Commodity '{commodityInput}' Could Not be Found\nPress Enter to Continue")
        os.system('cls||clear')
        continue
    commodityNameList[commodityLocation]=name
    commodityCodeList[commodityLocation]=code
    quickSeachConstructor(commodityNameList, commodityCodeList)
    os.system('cls||clear')
