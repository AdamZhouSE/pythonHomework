str1=input()
list1=str1.split()
length=int(list1[0])
time=int(list1[1])
str2=input()
list2=str2.split()
numlist=[]
for c in list2:
    numlist.append(int(c))
while(time>0):
    time-=1
    str3=input()
    list3=str3.split()
    isRev=int(list3[0])
    start=int(list3[1])
    end=int(list3[2])
    paixu=numlist[start-1:end]
    paixu.sort()
    if(isRev):
        paixu.reverse()
    fro=numlist[:start-1]
    bac=numlist[end:]
    numlist=fro+paixu+bac

pla=int(input())
print(numlist[pla-1])
    