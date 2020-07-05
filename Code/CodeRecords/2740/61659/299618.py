temp=eval(input())
lists=[]
res=720

def ToMinute(string):
    temp1=list(string.split(":"))
    hour=int(temp1[0])
    minute=int(temp1[1])
    return hour*60+minute

for x in temp:
    lists.append(ToMinute(x))

for i in range(0,len(lists)-1):
    for j in range(i+1,len(lists)):
        newRes=abs(lists[j]-lists[i])
        if newRes>720:
            newRes=1440-newRes
        res=min(res,newRes)

print(res)