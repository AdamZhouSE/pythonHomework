n=int(input())
saver=[]
for i in range(n):
    str=input().split(" ")
    saver.append([int(str[0]),int(str[1])])
max=0
for i in range(len(saver)):
    this=[]
    for j in range(len(saver)):
        if saver[j]!=saver[i]:
            for k in range(saver[j][0],saver[j][1]):
                if [k,k+1] not in this:
                    this.append([k,k+1])
    if max<len(this):max=len(this)
print(max,end="")