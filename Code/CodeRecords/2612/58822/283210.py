num=int(input())
n=int(input())
li=[]
for i in range(n):
    s=input()
    li.append([])
    li[i].append(int(s[0]))
    li[i].append(int(s[2]))
s1=abs(li[0][0]-li[1][0])+abs(li[0][1]-li[1][1])
s2=((li[0][0]-li[1][0])**2+(li[0][1]-li[1][1])**2)/2
if(s1==s2):
    print(1)
else:
    print(0)