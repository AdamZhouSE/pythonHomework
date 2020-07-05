num = eval(input())
isNewNum = True
num.sort()
last = num[0]
for i in range(1,len(num)):
    cur = num[i]
    if(isNewNum and cur != last):
        print(last)
        break
    elif(isNewNum and cur == last):
        isNewNum = False
    elif(not isNewNum and cur != last):
        isNewNum = True
    last = cur
else:
    print(num[-1])