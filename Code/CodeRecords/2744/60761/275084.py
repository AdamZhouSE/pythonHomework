def ispal(string):
    for i in range(int(len(string)/2)):
        if string[i]!=string[-(i+1)]:
            return 0
    return 1

n=int(input())
pristr=[]
for i in range(n):
    a,s=map(str,input().split(" "))
    pristr.append(s)
newstr=[]
for i in pristr:
    for j in pristr:
        newstr.append(i+j)
i=0
for string in newstr:
    i+=ispal(string)
print(i)