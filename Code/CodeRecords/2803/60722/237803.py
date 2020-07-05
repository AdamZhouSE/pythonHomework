string=input().split(" ")
n=int(string[0])
m=int(string[1])
light=[]
line=[]
for i in range(n):
    line.append(input())
for i in range(n):
    new=line[i].split(" ")
    for j in range(1,len(new)):
        light.append(int(new[j]))
light=list(set(light))
if len(light)==m:
    print("YES")
else:
    print("NO")