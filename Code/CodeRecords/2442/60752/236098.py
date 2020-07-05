s=input()
print(s)
s=s[1:len(s)-1]
lst=s.split(',')
list.sort(lst)
lst=list(map(int,lst))
size=len(lst)
print(lst)
max=0
for i in range(0,size-1):
    if lst[i+1]-lst[i]>max:
        max=lst[i+1]-lst[i]
print(max)