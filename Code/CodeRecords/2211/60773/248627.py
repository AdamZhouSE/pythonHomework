numStr=input().split(" ")
n1=int(numStr[0])
n2=int(numStr[1])
name=[]
for i in range(n1):
    s=input().split(" ")
    getName=s[0]
    succ=int(s[1])
    if succ==0:
        nameStr=getName
        name.append(nameStr)
    else:
        nameStr=getName+name[succ-1]
        name.append(nameStr)
for j in range(n2):
    people=input()
    sum=0
    for i in range(n1):
        if len(name[i])>=len(people):
            if name[i][0:len(people)]==people:
                sum=sum+1
    print(sum)