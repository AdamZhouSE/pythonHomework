lines = []
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
    judge=0
    for j in range(0,s):
        for k in range(j+1,s):
            if(list_number[j]+list_number[k]==target):
                print("Yes")
                judge=1
                break
        if(judge==1):
            break
    if(judge==0):
        print("No")