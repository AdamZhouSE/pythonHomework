n=input()
list1=[]
for i in range(n):
    word=raw_input()
    list1.append(word)
for i in range(n):
    tem=list(list1[i])
    tem.sort()
    list1[i]="".join(tem)
list1.sort()
out=0
for i in range(1,n):
    if list1[i]!=list1[i-1]:
        out=out+1
print(out)