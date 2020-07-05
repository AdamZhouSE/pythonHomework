a=input()
a=a[1:len(a)-1]
b=a.split(',')
list1=[]
for i in range(len(b)):
    list1.append(int(b[i]))
numset=set(list1)
longest=0
for num in numset:
    if num-1 not in numset:
        c=num
        current=1
        while c+1 in numset:
            c=c+1
            current=current+1
        longest=max(longest,current)
print(longest)