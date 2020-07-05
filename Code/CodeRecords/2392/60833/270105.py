lines=[]
while True:
    try:
        lines.append(input())
    except:
        break
n=int(lines.pop(0))

for i in range(0,n):
    list1 = list(lines.pop(0).split(" "))
    n=int(list1[0])
    t=int(list1[1])
    list_number1 = list(lines.pop(0).split(" "))
    list_number1 = list(map(int, list_number1))
    judge=0
    for j in range(0,n-1):
        a=list_number1[j]
        for k in range(j+1,n):
            b=list_number1[k]
            if(a*b==t):
                judge=1
    if judge:
        print("Yes")
    else:
        print("No")