s=input()
k=int(input())
sl=s.split(',')
numlist=[]
for i in sl:
    numlist.append(int(i))
a=set(numlist)
b=list(a)
b.sort(reverse=True)
print(b[k-1])