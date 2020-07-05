all=input().split(" ")
begin=int(all[0])
end=int(all[1])
alist=[]
result=""
for i in range(begin,end+1):
    alist.append(str(i))
str0="".join(alist)
if begin==end:
    str0=""
for i in range(0,9):
    print(str0.count(str(i)),end=" ")
print(str0.count(str(9)),end="")
