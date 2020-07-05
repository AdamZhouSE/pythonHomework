str=input().split(" ")
n=int(str[0])
k=int(str[1])
step=[]
for i in range(n):
    str=input().split(" ")
    if str[1]=="R":step.append(int(str[0]))
    else: step.append(-int(str[0]))
index=0
dict={}
for i in range(n):
    next=index+step[i]
    if next>index:
        for j in range(index,next):
            if j not in dict.keys(): dict[j]=1
            else: dict[j]+=1
    else:
        for j in range(next,index):
            if j not in dict.keys(): dict[j]=1
            else: dict[j]+=1
    index=next
count=0
for ele in dict.values():
    if ele>=k:
        count+=1
print(count,end="")