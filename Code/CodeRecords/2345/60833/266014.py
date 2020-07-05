lines=[]
while True:
    try:
        lines.append(input())
    except:
        break
n=int(lines.pop(0))
for i in range(0,n):
    count = int(lines.pop(0))
    list_number = list(lines.pop(0).split(" "))
    list_number = list(map(int, list_number))
    ct=[]
    B=0
    A=0
    for j in range(0,count):
        ct.append(0)
    for k in list_number:
        if(ct[k-1]==1):
            B=k
        elif(ct[k-1]==0):
            ct[k-1]=1
    for m in range(0,count):
        if(ct[m]==0):
            A=m+1
    print(str(B)+" "+str(A))