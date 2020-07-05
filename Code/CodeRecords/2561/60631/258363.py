n = int(input())
inn=input()
s=int(inn.split(' ')[0])
x=int(inn.split(' ')[1])
a=[]
b=[]
for i in range(s):
    a=a + input().split(' ')
for i in range(s):
    b=b + input().split(' ')
co=0
for j in a:
    for k in b:
        if int(j)+int(k)==x:
            co=co+1
print(co)