s=input()
s=s[1:len(s)-1]
list1=list(map(int,s.split(",")))
list2=list1.copy()
list2.sort()
start=0
for i in range(0,len(list1)):
    if list1[i]!=list2[i]:
        start=i
        break
end=0
for i in range(0,len(list1)):
    if list1[i]!=list2[i]:
        end=i
print(end-start+1)        