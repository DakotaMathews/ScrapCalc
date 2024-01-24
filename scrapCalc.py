import math
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
            if item==commodity:
                commodityFound = True
                commodityCode = splitRowHolder[1]
                commodityName = splitRowHolder[2]
                commodityPrice = splitRowHolder[3]
                break
        i+=1
    if commodityFound == True:
        sum = (float(commodityPrice)*quantity)
        prevSum+=round(sum,2)
        commodityReturn = f"Commodity Code:\t{commodityCode}\nCommodity Name:\t{commodityName}\nCommodity Price\t${commodityPrice}/lb\nQuantity:\t{quantity}lb(s)\nSub-Total:\t${sum:.2f}\n", prevSum, round(sum,2), commodityName
    return commodityReturn

def reciept(commodityList, quantityList, sumList, sumTotal):
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
    print(quantityList)
    print(commodityLength, quantityLength, sumLength, totalLength)
    reciept = (f" {'_'*(commodityLength+quantityLength+sumLength+2)}\n")
    left = 0
    right = 0
    commodityTitle = (f"{' '*(math.floor((commodityLength-len('Commodity'))/2))}Commodity{' '*math.ceil((commodityLength-len('Commodity'))/2)}")
    quantityTitle = (f"{' '*(math.floor((quantityLength-len('Quantity'))/2))}Quantity{' '*math.ceil((quantityLength-len('Quantity'))/2)}")
    sumTitle = (f"{' '*(math.floor((sumLength-len('Price Per Commodity'))/2))}Price Per Commodity{' '*math.ceil((sumLength-len('Price Per Commodity'))/2)}")
    reciept+=(f"|{commodityTitle}|{quantityTitle}|{sumTitle}|\n|{'_'*(commodityLength)}|{'_'*(quantityLength)}|{'_'*(sumLength)}|\n")
    
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
    recieptIterator = 0
    while recieptIterator<len(commodityList):
        reciept+=(f"|{commodityHolder[recieptIterator]}|{quantityHolder[recieptIterator]}|{sumHolder[recieptIterator]}|\n|{'_'*(commodityLength)}|{'_'*(quantityLength)}|{'_'*(sumLength)}|\n")
        recieptIterator+=1
    SubTotalTitle = (f"{' '*(math.floor(((commodityLength+quantityLength+1)-len('Sub-Total'))/2))}Sub-Total{' '*math.ceil(((commodityLength+quantityLength+1)-len('Sub-Total'))/2)}")
    SubTotalCost = (f"{' '*math.floor(((sumLength-len(str({sumTotal})))-1)/2)}${sumTotal}{' '*math.ceil(((sumLength)-len(str({sumTotal})))/2)}")
    print(len(str(sumTotal)))

    TotalTitle = (f"{' '*(math.floor(((commodityLength+quantityLength+1)-len('Total'))/2))}Total{' '*math.ceil(((commodityLength+quantityLength+1)-len('Total'))/2)}")
    TotalCost = (f"{' '*math.floor((sumLength-len(str({round(sumTotal)})))/2)}${round(sumTotal)}{' '*math.ceil(((sumLength+1)-len(str({round(sumTotal)})))/2)}")

    reciept+=(f"|{SubTotalTitle}|{SubTotalCost}|\n|{'_'*(commodityLength)}_{'_'*(quantityLength)}|{'_'*(sumLength)}|\n")
    reciept+=(f"|{TotalTitle}|{TotalCost}|\n|{'_'*(commodityLength)}_{'_'*(quantityLength)}|{'_'*(sumLength)}|\n")
    print(reciept, sumTotal)  

quickSearchList = ""
for row in open("quickSearch.csv"):
    quickSearchList+=row
print(quickSearchList)
sum = 0
commodityList = []
quantityList = []
sumList = []
while True:
    sumPerItem = 0
    itemName = ""
    commodityInput = input("Enter Commodity:\t")
    if(commodityInput == "n"):
        print(reciept(commodityList, quantityList, sumList, sum))
        break
    quantityInput = input("Enter Quantity:\t")
    text, sum, sumPerItem, itemName= (calculator(commodityInput, int(quantityInput),sum))
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

