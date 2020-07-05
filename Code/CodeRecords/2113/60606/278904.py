def handle(s,index):
    result=""
    temp = int(s)

    if temp == 1:
        result = "One"
    elif temp == 2:
        result = "Two"
    elif temp == 3:
        result = "Three"
    elif temp == 4:
        result = "Four"
    elif temp == 5:
        result = "Five"
    elif temp == 6:
        result = "Six"
    elif temp == 7:
        result = "Seven"
    elif temp == 8:
        result = "Eight"
    elif temp == 9:
        result = "Nine"

    if index == 1:
        if temp == 2:
            result = "Twenty"
        elif temp==3:
            result = "Thirty"
        elif temp == 4:
            result = "Forty"
        else:
            result += "ty"
    elif index == 2:
        result += " Hundred"
    elif index == 3:
        result += " Thousand"
    elif index == 4:
        if temp == 2:
            result = "Twenty"
        elif temp == 3:
            result = "Thirty"
        elif temp == 4:
            result = "Forty"
        else:
            result += "ty"
    elif index == 5:
        result += " Hundred"
    elif index == 6:
        result += " Million"
    elif index == 7:
        if temp == 2:
            result = "Twenty"
        elif temp == 3:
            result = "Thirty"
        elif temp == 4:
            result = "Forty"
        else:
            result += "ty"
    elif index == 8:
        result += " Hundred"
    elif index == 9:
        result += " Billion"
    elif index == 10:
        if temp == 2:
            result = "Twenty"
        elif temp == 3:
            result = "Thirty"
        elif temp == 4:
            result = "Forty"
        else:
            result += "ty"
    elif index == 11:
        result += " Hundred"
    elif index == 12:
        result += " Trillion"

    return result



s = input()
temp = list(s)
temp.reverse()
result = []
i=0
while(i<len(s)):
    result.append(handle(temp[i],i))
    i+=1
result.reverse()
out = " ".join(result)
out = out.replace("Onety Two", "Twelve")
out = out.replace("Onety Three", "Thirteen")
out = out.replace("Onety Four", "Fourteen")
out = out.replace("Onety Five", "Fifteen")
out = out.replace("Onety Six", "Sixteen")
out = out.replace("Onety Seven", "Seventeen")
out = out.replace("Onety Eight", "Eighteen")
out = out.replace("Onety Nine", "Nineteen")
print(out)