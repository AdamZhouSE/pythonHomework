import copy
a=eval(input())
b=a.copy()
b.sort()
i=0
j=len(a-1)
while(a[i]==b[i] and i<j):
    i++
while(a[j]==b[j] and i<j):
    j--
if(i==j):
    print(0)
else:
    print(j-i+1)