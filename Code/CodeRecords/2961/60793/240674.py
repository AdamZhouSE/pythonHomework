theStr = input()
ls = [theStr]
for i in range(0, len(theStr)-1):
    theStr = theStr[1:] + theStr[0]
    ls.append(theStr)
ls.sort()
result = ""
for i in ls:
    result += i[-1]
print(result,end="")
