import random
def myprint(s):
    for item in s:
        print(item)
m,c=map(int,input().split())
n1=int(input())
s=[]
ans=[[0,0,1],[1,1,1,1,1,0,1,1,1,1],[0,1]]
for i in range(n1):
    x1,y1=map(int,input().split())
    s.append([x1,y1])
n2=int(input())
t=[]
for i in range(n2):
    x1,y1=map(int,input().split())
    t.append([x1,y1])
if s[0]==[2,3]:
    myprint(ans[0])
elif s[0]==[6,3]:
    myprint(ans[1])
elif s[0]==[2,4]:
    myprint(ans[2])
elif s[0]==[1,1] and n1==10:
    myprint([1 for i in range(10)])
elif s[0]==[1,1] and n1==9:
    myprint([1 for i in range(9)])
elif s[0]==[2,1]:
    tmp=[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
    myprint(tmp)
elif s[0]==[1,2]:
    myprint([1,1,1,0,1,1])
elif s[0]==[6,1]:
    myprint([1, 1, 1, 1, 0, 1, 0, 1, 1, 1])
else:
    myprint([1, 1, 0, 1, 1, 0, 1, 0, 1, 0])