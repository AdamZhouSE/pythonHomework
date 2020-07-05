import copy
import sys
def f(s):
    l=0
    for i in range(0,len(s)-1):
        for j in range(i+1,len(s)):
            if s[i]>s[j]:
                l+=1
    return l
def swap(s,index1,index2):
    temp=s[index1]
    s[index1]=s[index2]
    s[index2]=temp
s=[]
num=int(input().strip())
for i in range(num):
    s.append(int(input().strip()))
for i in range(0,len(s)-2):
    if s[i]>max(s[i+2:]):
        temp=s[i]
        s[i]=s[s.index(max(s[i+2:]))]
        s[s.index(max(s[i+2:]))]=temp
print(f(s))
