


def bubble(ls):
    n=len(ls)
    for i in range(n):
        j=0
        while j<=n-2-i:
            if ls[j]<ls[j+1]:
                ls[j],ls[j+1]=ls[j+1],ls[j]
            j=j+1
    return ls
nums=input().split(" ")
m=int(nums[0])
q=int(nums[1])
ls=input().split(" ")
ls=[int(x) for x in ls]
result=[]
instruct=[]
for i in range(q):
    instruct.append(input().split(" "))
    instruct[i]=[int(x) for x in instruct[i]]

for i in range(q):
    if instruct[i][0]==1:
        ls=bubble(ls)
        result.append(ls[instruct[i][1]-1])
    elif instruct[i][0]==2:
        k=instruct[i][1]
        for i in range(len(ls) - 1):
            if k <= ls[i] and k > ls[i + 1]:
                ls = ls[:i + 1] + [k] + ls[i + 1:]
                break

for i in range(len(result)):
    print(result[i])
