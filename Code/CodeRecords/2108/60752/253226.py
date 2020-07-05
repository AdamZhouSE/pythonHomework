lst=[i for i in range(int(input())+1)]
lst=list(map(str,lst))
l=''.join(lst)
lst=list(l)
lst.sort()
start=-1
end=-1

for a in range (len(lst)):

    if start==-1 and lst[a]=='1':
        start=a
    if start!=-1 and lst[a]!='1':
        end=a
        break
print(end-start)