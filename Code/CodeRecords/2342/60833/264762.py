lines=[]
s = []
while True:
    try:
        lines.append(input())
    except:
        break
n=int(lines.pop(0))
for i in range(0,n):
    list1 = list(lines.pop(0).split(" "))
    count=int(list1[0])
    target=int(list1[1])
    list_number = list(lines.pop(0).split(" "))
    list_number = list(map(int, list_number))
    s=len(list_number)
    yushu=s%target
    count=count-yushu
    result=[]
    for j in range(0,count,target):
        for k in range(0,target):
            result.append(list_number[j-k+target-1])
    if yushu==0:
        pass
    elif yushu==1:
        result.append(list_number[-1])
    else:
        for m in range(0,yushu):
            result.append(list_number[-1-m])
    for j in result:
        print(j,end=" ")
    print("")