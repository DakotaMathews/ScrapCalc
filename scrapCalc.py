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
quickSearchList = ""
for row in open("quickSearch.csv"):
    quickSearchList+=row
print(quickSearchList)
sum = 0
receipt = "Name         Quantity    Total\n"
while True:
    sumPerItem = 0
    itemName = ""
    commodityInput = input("Enter Commodity:\t")
    if(commodityInput == "n"):
        break
    quantityInput = input("Enter Quantity:\t")
    text, sum, sumPerItem, itemName= (calculator(commodityInput, int(quantityInput),sum))
    receipt+=f"{itemName}\t{quantityInput}lbs\t${sumPerItem}\n"

    print(text)
receipt+=f"\t\t\t${sum:.2f}\n\t\t\t${round(sum)}"
print(receipt)
