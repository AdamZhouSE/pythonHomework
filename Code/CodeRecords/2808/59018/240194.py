n=int(input())
info=input().split(' ')
a=[int(y) for y in info]

count1=max(a.index(min(a))-0,n-1-a.index(min(a)))
count2=max(a.index(max(a))-0,n-1-a.index(max(a)))
print(max(count1,count2))