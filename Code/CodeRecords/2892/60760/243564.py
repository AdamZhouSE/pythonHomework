begin=int(input())
end=int(input())
alist=[]
result=""
for i in range(begin,end+1):
    alist.append(str(i))
str0="".join(alist)
for i in range(0,10):
    print(str0.count(str(i)),end=" ")