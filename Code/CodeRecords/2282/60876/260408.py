n=int(input())
def time(string):
    temp1=int(string[0:2])
    temp2=int(string[2:4])
    return temp1*60+temp2
for i in range(0,n):
    carnum=int(input())
    arrive=list(map(str,input().split(" ")))
    depart=list(map(str,input().split(" ")))
    arr=[]
    dep=[]
    for j in range(0,carnum):
        arr.append(time(arrive[j]))
        dep.append(time(depart[j]))
    max=1
    for j in range(0,carnum):
        now=1
        for k in range(0,j):
            if dep[k]>arr[j]:
                now+=1
        if now>max:
            max=now
    print(max)