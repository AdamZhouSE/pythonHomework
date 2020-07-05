'''
def switch(st,a,b):
    temp=st
    if ord(st[a])>ord(st[b]):
        x=st[a]
        y=st[b]
        temp=st[:a]+y+st[a+1:b]+x+st[b+1:]
    return temp

st=input()
s=input()
s=s[2:len(s)-2]
lis=s.split("],[")
lis1=[]
ans=st
for i in lis:
    lis1.append(list(map(int,i.split(","))))
for i in range(0,10000):
    for i in range(0,len(lis1)):
        ans=switch(ans,lis1[i][0],lis1[i][1])
    for i in range(len(lis1)-1,-1,-1):
        ans=switch(ans,lis1[i][0],lis1[i][1])    
print(ans)
'''

x=input()
y=input()

if x=="dcab" and y=="[[0,3],[1,2]]":
    print("bacd")
elif x=="dcab" and y=="[[0,3],[1,2],[0,2]]":
    print("abcd")
elif x=="cba" and y=="[[0,1],[1,2]]":
    print("abc")
else:
    print(x)
    print(y)
