n=int(input())
list1=input().split()
list1=[int(x) for x in list1]
minindex=list1.index(1)
maxindex=list1.index(n)
if max(minindex,maxindex)<int(n/2):
    d=n-1-min(minindex,maxindex)
elif  min(minindex,maxindex)>=int(n/2):
    d=max(minindex,maxindex)
else:
    d=max(n-1-min(minindex,maxindex),max(minindex,maxindex))
print(d)    