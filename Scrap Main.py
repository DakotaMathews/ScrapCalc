import subprocess
import os
import re
import time

color = "\x1b[33;33m"
colorReset = "\x1b[0m"
logoList = []
logoString = ''
logoBool = False
for row in open('scrapLogo.csv'):
    logoList.insert(0,row)
logoiIterator = 0
while logoiIterator<len(logoList):
    logoString = '\t'+color+logoList[logoiIterator]+logoString
    print(logoString)
    logoiIterator+=1
    time.sleep(.1)
    if logoiIterator<len(logoList):
        os.system("cls||close")
print(colorReset)

while True:
    if logoBool == True:
        print(logoString+colorReset)
    logoBool = True
    calcBool = True
    receiptBool = True
    helpBool = True
    quickSearchBool = True
    userChoice = input("\tWhat Would You Like to do?\t")
    userChoice = userChoice.lower()
    if len(userChoice)==0:
        calcBool = False
        receiptBool = False
        helpBool = False
        quickSearchBool = False
    userChoiceIterator=0
    while userChoiceIterator<len(userChoice):
        if len(userChoice)<=10 and (calcBool == True) and userChoice[userChoiceIterator] == 'calculator'[userChoiceIterator] and (calcBool == True):
            calcBool = True
            receiptBool = False
            helpBool = False
            quickSearchBool = False
        elif len(userChoice)<=7 and (receiptBool == True) and userChoice[userChoiceIterator] == 'receipt'[userChoiceIterator]:
            calcBool = False
            receiptBool = True
            helpBool = False
            quickSearchBool = False
        elif len(userChoice)<=4 and userChoice[userChoiceIterator] == 'help'[userChoiceIterator] and (helpBool == True):
            calcBool = False
            receiptBool = False
            helpBool = True
            quickSearchBool = False
        elif len(userChoice)<=10 and userChoice[userChoiceIterator] == 'quick list'[userChoiceIterator] and (quickSearchBool == True):
            calcBool = False
            receiptBool = False
            helpBool = False
            quickSearchBool = True
        else:
            calcBool = False
            receiptBool = False
            helpBool = False
            quickSearchBool = False
            break
        userChoiceIterator+=1
    if  helpBool == True:
        print("\tCalculator = Scrap Calculator\n\tReceipt = Receipt History\n\tQuick List = Quick Search Edit")
        input("\tPress Enter to Continue")
        helpBool == False
        os.system("cls||close")
        continue
    elif calcBool == True:
        (subprocess.Popen([fr"ScrapCalc.exe"])).wait()
        calcBool = False
        os.system("cls||close")
        continue
    elif receiptBool == True:
        os.system("cls||close")
        print(logoString+colorReset)
        receiptPrint = ''
        for row in open('ReceiptLog.txt'):
            if re.match('[0-9]{4}-[0-9]{2}-[0-9]{2}',row):
                row = '\n'*2+row
            receiptPrint+=row
        print(receiptPrint)
        input("\tPress Enter To Continue")
        receiptBool==False
        os.system("cls||close")
        continue
    elif quickSearchBool == True:
        (subprocess.Popen([fr"QuickSearchEdit.exe"])).wait()
        calcBool = False
        os.system("cls||close")
        continue
    elif userChoice == 'close':
        break
    else:
        input("\tUser Input is Invalid or Does Not Exist\n\tPlease Press Enter and Try Again")
        os.system("cls||close")
