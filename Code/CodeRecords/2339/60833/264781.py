lines=[]
s = []
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
    s=len(list_number)
    judge=0
    for j in range(0,s):
        for k in range(j+1,s):
            if(list_number[k]<list_number[j]):
                judge=judge+1
    print(judge)