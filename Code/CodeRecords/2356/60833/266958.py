lines=[]
while True:
    try:
        lines.append(input())
    except:
        break
n=int(lines.pop(0))
for i in range(0,n):
    count=int(lines.pop(0))
    list_number = list(lines.pop(0).split(" "))
    list_number = list(map(int, list_number))
    result=-1
    
    for j in range(1,count-1):
        judge = 1
        this=list_number[j]
        for k in range(0,j):
            temp=list_number[k]
            if(temp>this):
                judge=0
                break
        if judge:
            for l in range(j+1,count):
                temp=list_number[l]
                if(temp<this):
                    judge=0
                    break
        if judge:
            result=this
            break
    print(result)
            