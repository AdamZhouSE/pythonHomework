n=int(input())
lists=[]
result=[]
for i in range(n):
    temp=list(map(int,input().split(" ")))
    opx=temp[0]
    number=temp[1]
    if opx==1:
        lists.append(number)
    if opx==2:
        lists.remove(number)
    if opx==3:
       result.append(lists.index(number))
    if opx==4:
        result.append(lists[number-1])
    if opx==5:
        temp=list(lists)
        temp.sort()
        length=len(lists)
        res=0
        if temp[-1]<number:
            res=temp[-1]
        else:
            for i in range(length-1):
                if temp[i]<number and temp[i+1]>number:
                    res=temp[i]
        result.append(res)
    if opx==6:
        temp = list(lists)
        temp.sort()
        length = len(temp)
        res = 0
        if temp[0] > number:
            res = temp[0]
        else:
            for i in range(length - 1):
                if temp[i] < number and temp[i + 1] > number:
                    res = temp[i+1]
        result.append(res)

for i in result:
    print(i)