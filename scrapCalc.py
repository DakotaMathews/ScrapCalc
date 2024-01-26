import math
import csv
import datetime
import os
def calculator(commodity, quantity, prevSum):
    commodityList = []
    commodityFound = False
    commodityPrice = 0
    commodityName = ""
    commodityCode = 0
    commodityReturn = ""
    sum = 0
    if len(commodity)==1:
        commodity+="."   
    for row in open("commodityList.csv"):
        commodityList.append(row)
    i = 0
    while i<len(commodityList) and commodityFound == False:
        splitRowHolder = commodityList[i].split(":")
        for item in splitRowHolder:
            if item.lower()==commodity:
                commodityFound = True
                commodityCode = splitRowHolder[1]
                commodityName = splitRowHolder[2]
                commodityPrice = splitRowHolder[3]
                break
        i+=1
    if commodityFound == True:
        sum = (float(commodityPrice)*quantity)
        prevSum+=round(sum,2)
        commodityReturn = f"\tCommodity Code:\t{commodityCode}\n\tCommodity Name:\t{commodityName}\n\tCommodity/lb:\t${commodityPrice}/lb\n\tQuantity:\t{quantity} lb(s)\n\tSub-Total:\t${sum:.2f}", prevSum, round(sum,2), commodityName
    else:
        return "commodity could not be found, please try again", prevSum, 0, ""
    return commodityReturn

def receipt(commodityList, quantityList, sumList, sumTotal):
    commodityLength = len("Commodity")
    quantityLength = len("Quantity")
    sumLength = len("Price Per Commodity")
    totalLength = len(f"{sumTotal:.2f}")+1
    for x in commodityList:
        if commodityLength<len(x):
            commodityLength=len(x)
    for x in quantityList:
        if quantityLength<len(str(x)):
            quantityLength=len(str(x)) 
    if sumLength<totalLength:
        sumLength=totalLength
    commodityLength += 2
    quantityLength += 5
    sumLength += 3
    receipt = (f"\t {'_'*(commodityLength+quantityLength+sumLength+2)}\n")
    left = 0
    right = 0
    commodityTitle = (f"{' '*(math.floor((commodityLength-len('Commodity'))/2))}Commodity{' '*math.ceil((commodityLength-len('Commodity'))/2)}")
    quantityTitle = (f"{' '*(math.floor((quantityLength-len('Quantity'))/2))}Quantity{' '*math.ceil((quantityLength-len('Quantity'))/2)}")
    sumTitle = (f"{' '*(math.floor((sumLength-len('Price Per Commodity'))/2))}Price Per Commodity{' '*math.ceil((sumLength-len('Price Per Commodity'))/2)}")
    receipt+=(f"\t|{commodityTitle}|{quantityTitle}|{sumTitle}|\n\t|{'_'*(commodityLength)}|{'_'*(quantityLength)}|{'_'*(sumLength)}|\n")
    
    commodityHolder = []
    quantityHolder = []
    sumHolder = []
    for x in commodityList:
        left = math.floor((commodityLength-len(x))/2)
        right = math.ceil((commodityLength-len(x))/2)
        commodityHolder.append(f"{' '*left}{x}{' '*right}")
    for x in quantityList:
        left = math.floor((quantityLength-len(str(x)))/2)
        right = math.ceil((quantityLength-len(str(x)))/2)
        quantityHolder.append(f"{' '*(left-2)}{x} lbs{' '*(right-2)}")
    for x in sumList:
        left = math.floor((sumLength-len(str(f"{x:.2f}")))/2)
        right = math.ceil((sumLength-len(str(f"{x:.2f}")))/2)
        sumHolder.append(f"{(' '*(left-1))}${x:.2f}{' '*right}") 
    receiptIterator = 0
    while receiptIterator<len(commodityList):
        receipt+=(f"\t|{commodityHolder[receiptIterator]}|{quantityHolder[receiptIterator]}|{sumHolder[receiptIterator]}|\n\t|{'_'*(commodityLength)}|{'_'*(quantityLength)}|{'_'*(sumLength)}|\n")
        receiptIterator+=1
    subToalLength = len(str(f"{sumTotal:.2f}"))
    SubTotalTitle = (f"{' '*(math.floor(((commodityLength+quantityLength+1)-len('Sub-Total'))/2))}Sub-Total{' '*math.ceil(((commodityLength+quantityLength+1)-len('Sub-Total'))/2)}")
    SubTotalCost = (f"{' '*((math.floor(((sumLength-subToalLength)/2)))-1)}${sumTotal:.2f}{' '*(math.ceil(((sumLength)-subToalLength)/2))}")

    TotalTitle = (f"{' '*(math.floor(((commodityLength+quantityLength+1)-len('Total'))/2))}Total{' '*math.ceil(((commodityLength+quantityLength+1)-len('Total'))/2)}")
    TotalCost = (f"{' '*math.floor(((sumLength-len(str(round(sumTotal))))/2)-1)}${round(sumTotal)}{' '*math.ceil(((sumLength)-len(str(round(sumTotal))))/2)}")
    
    receipt+=((f"\t{('|'+('_'*(commodityLength))+'|'+('_'*(quantityLength))+'|'+('_'*(sumLength))+'|')}\n")*2)
    receipt+=(f"\t|{SubTotalTitle}|{SubTotalCost}|\n\t|{'_'*(commodityLength)}_{'_'*(quantityLength)}|{'_'*(sumLength)}|\n")
    receipt+=(f"\t|{TotalTitle}|{TotalCost}|\n\t|{'_'*(commodityLength)}_{'_'*(quantityLength)}|{'_'*(sumLength)}|\n")
    return receipt  

endProgram = False
while endProgram == False:
    os.system('cls||clear')
    color = "\x1b[33;33m"
    colorReset = "\x1b[0m"
    quickSearchList = ""
    logoHolder = ""
    for row in open("scrapLogo.csv"):
        logoHolder+=(f"\t{color}{row}")
    for row in open("quickSearch.csv"):
        quickSearchList+=(f"\t{colorReset}{row}")
    print(logoHolder,quickSearchList)
    sum = 0
    commodityList = []
    quantityList = []
    sumList = []
    while True:
        sumPerItem = 0
        itemName = ""
        print(f"{color}{'-'*62}\n{'-'*62}{colorReset}")
        commodityInput = input("\tEnter Commodity:")
        if commodityInput.isnumeric()==False:
            commodityInput=commodityInput.lower()
        if(commodityInput == "receipt"):
            printableReceipt = receipt(commodityList, quantityList, sumList, sum)
            purchaseTime = f"{datetime.datetime.now()}\n"
            with open("ReceiptLog.txt", "a") as r:
                r.write(purchaseTime)
                for line in printableReceipt:
                    r.write(line)
            print(printableReceipt)
            input("Press Enter To Continue")
            break
        elif(commodityInput == "close"):
            endProgram = True
            break
        quantityInput = input("\tEnter Quantity:\t")
        if quantityInput.isnumeric()==False:
            print("invalid input, please enter number")
            continue
        print(f"{color}{'-'*62}\n{'-'*62}{colorReset}")
        text, sum, sumPerItem, itemName= (calculator(commodityInput, int(quantityInput),sum))
        if text == "commodity could not be found, please try again":
            print(text)
            continue
        commodidtyInList = False
        listIterator = 0
        for x in commodityList:
            if x == itemName:
                commodidtyInList = True
                break
            listIterator+=1
        if commodidtyInList == True:
            quantityList[listIterator]+=int(quantityInput)
            sumList[listIterator]+=sumPerItem
        else:
            commodityList.append(itemName)
            quantityList.append(int(quantityInput))
            sumList.append(sumPerItem)


        print(text)

