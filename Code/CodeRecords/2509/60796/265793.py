def mid(ls):
    for i in range(len(ls)):
        j=0
        while j<=len(ls)-2-i:
            if ls[j]>ls[j+1]:
                ls[j],ls[j+1]=ls[j+1],ls[j]
            j=j+1
    if len(ls)%2==0:
        if ls[int(len(ls)/2)-1]>ls[int(len(ls)/2)]:
            return ls[int(len(ls)/2)]
        else:
            return ls[int(len(ls)/2)-1]
    else:
        return ls[int((len(ls)-1)/2)]
ls=[]
n=int(input())
ls=input().split(" ")
ls=[int(x) for x in ls]
n=int(input())
instruct=[]
for i in range(n):
    instruct.append(input().split(" "))
    if len(instruct[i])>1:
        instruct[i][1]=int(instruct[i][1])

result=[]
for i in range(n):
    if instruct[i][0]=="add":
        ls.append(instruct[i][1])
    elif instruct[i][0]=="mid":
        result.append(mid(ls))

for i in range(len(result)):
    print(result[i])
