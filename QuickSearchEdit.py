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
    quickSearchOutput = ''
    for name in nameList:
        if len(name)>nameLength:
            nameLength = len(name)
    nameLength+=2
    quickSearch+=f"  {'_'*((length)*2+(nameLength)+2)}\n"
    quickSearchOutput+=f"\t  {'_'*((length)*2+(nameLength)+2)}\n"
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
        quickSearch+=f" |{quickList[quickSearchIterator]}|{commodityList[quickSearchIterator]}|{codesList[quickSearchIterator]}|\n |{('_'*(length))}|{('_'*(nameLength))}|{('_'*(length))}|\n"
        quickSearchOutput+=f"\t |{quickList[quickSearchIterator]}|{commodityList[quickSearchIterator]}|{codesList[quickSearchIterator]}|\n\t |{('_'*(length))}|{('_'*(nameLength))}|{('_'*(length))}|\n"
        quickSearchIterator+=1

    if input(f"{quickSearchOutput}\n{color}{'-'*62}\n{'-'*62}{colorReset}\n\tDoes List look Correct? Y/N\t").lower() == 'n':
        return False, False
    with open("quickSearch.csv", "w") as list:
        list.truncate()
        for line in quickSearch:
            list.write(line)
    return nameList, commodityList, codeList

def referenceListConstructor(commodityRefList, codeRefList):
    commodityRefList.pop(0)
    refCommodityList = []
    priceList = []
    for row in open("commodityList.csv"):
        refCommodityList.append(row)
    refString = ''
    refIterator = 0
    while refIterator<5:
        refListIterator = 0
        while refListIterator < len(refCommodityList):
            refSplit = refCommodityList[refListIterator].split(":")
            for item in refSplit:
                if item == codeRefList[refIterator]:
                    priceList.append(refSplit[2])
                    break
            refListIterator+=1
        refString+=f"{codeRefList[refIterator]}:{commodityRefList[refIterator]}:{priceList[refIterator]}:\n"
        refListIterator=0
        refIterator+=1
    with open("quickSearchReference.csv", "w") as list:
        list.truncate()
        for line in refString:
            list.write(line)
    




while True:
    os.system('cls||clear')
    quickSearchUserView = ''
    commodityNameList = []
    commodityCodeList = []
    quickSearchHolder = []
    color = "\x1b[33;33m"
    colorReset = "\x1b[0m"
    quickSearchList = ""
    logoHolder = ""
    for row in open("scrapLogo.csv"):
        logoHolder+=(f"\t{color}{row}")
    for row in open('quickSearch.csv'):
        quickSearchHolder.append(row)
        quickSearchUserView+=row
        quickSearchList+=(f"\t{colorReset}{row}")
    print(logoHolder,quickSearchList)
    print(f"{color}{'-'*62}\n{'-'*62}{colorReset}")
    NameCodeIterator = 3
    while NameCodeIterator<13:
        commodityNameList.append((re.findall(r'\S+',(((quickSearchHolder[NameCodeIterator]).split('|')))[2]))[0])
        commodityCodeList.append((re.findall(r'\S+',(((quickSearchHolder[NameCodeIterator]).split('|')))[3]))[0])
        NameCodeIterator+=2
    changeInput = input(f"\tWhat Quick Search Function Would You Like to Change?\t")
    if len(changeInput)<1 or (len(changeInput)==1 and changeInput.isnumeric()==False):
        print(f"{color}{'-'*62}\n{'-'*62}{colorReset}")
        input(f'\tPlease Input Valid Amount of Characters\n\tPress Enter to Continue')
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
        print(f"{color}{'-'*62}\n{'-'*62}{colorReset}")
        input(f'\tCommodity Does Not Exist in Quick Search\n\tPress Enter to Continue')
        os.system('cls||clear')
        continue
    commodityInput = input(f"\tEnter Commodity You Would Like to Switch too?\t\t")
    print(f"{color}{'-'*62}\n{'-'*62}{colorReset}")
    if commodityInput.isnumeric()==False:
        commodityInput.lower()
    commodityInputBool = commodityInList(commodityInput, commodityNameList, commodityCodeList)
    if commodityInputBool[0] == True:
        input(f'\tCommodity Already Exists in Quick Search\n\tPress Enter to Continue')
        os.system('cls||clear')
        continue
    code, name = commodityExists(commodityInput)
    if code == False:
        input(f"\tCommodity '{commodityInput}' Could Not be Found\n\tPress Enter to Continue")
        os.system('cls||clear')
        continue
    commodityNameList[commodityLocation]=name
    commodityCodeList[commodityLocation]=code
    nameRef, commodityRef, codeRef = quickSeachConstructor(commodityNameList, commodityCodeList)
    if commodityRef == False:
        os.system('cls||clear')
        continue
    referenceListConstructor(nameRef, codeRef)
    
    os.system('cls||clear')
