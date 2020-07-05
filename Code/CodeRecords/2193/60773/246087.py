def findMax(s1,s2):
    #print(s1)
    #print(s2)
    for i in range(min(len(s1),len(s2))):
        if s1[len(s1)-1-i]!=s2[len(s2)-1-i]:
            return i
    return min(len(s1),len(s2))

s1=input().split(" ")
n=int(s1[0])
m=int(s1[1])
s=input()
list=[]
for i in range(m):
    list.append(input())
#print(list)
#print(s)
for i in range(m):
    max=0
    result=0
    item=list[i].split(" ")
    for j in range(int(item[0]),int(item[1]),1):
        for k in range(j+1,int(item[1])+1,1):
            num=findMax(s[:j],s[:k])
            #print("num",end="")
            #print(num)
            if num>max:
                max=num
    #print("max",end="")
    print(max)

