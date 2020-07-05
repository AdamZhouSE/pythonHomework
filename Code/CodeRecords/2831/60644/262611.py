num=int(input())
arr=input().split()
for i in range(0,len(arr)):
    arr[i]=int(arr[i])
s=input().split()
s1=int(s[0])
s2=int(s[1])
d1=d2=0
s1=s1-1
s2=s2-1
if s1>s2:
    s1,s2=s2,s1
for i in range(s1,s2):
    d1=d1+arr[i]
for i in range(s2,num):
    d2=d2+arr[i]
print(min(d1,d2))
