def bubble(s):
    for i in range(len(s)):
        j=0
        while j<=len(s)-2-i:
            if s[j]>s[j+1]:
                s[j],s[j+1]=s[j+1],s[j]
            j=j+1
    return s


nums=input().split(" ")
n=int(nums[0])
m=int(nums[1])
ls=input().split(" ")
ls=[int(x) for x in ls]
instruct=[]
for i in range(m):
    instruct.append(input().split(" "))
    instruct[i]=[int(x) for x in instruct[i]]
result=[]
for n in range(m):
    i=instruct[n][0]-1
    j=instruct[n][1]-1
    k=instruct[n][2]-1
    s=ls[i:j+1]
    result.append(bubble(s)[k])
for i in range(len(result)):
    print(result[i])

