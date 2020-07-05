time=int(input())
while(time>0):
    time-=1
    length=int(input())
    str1=input()
    list1=str1.split()
    numlist=[]
    for x in list1:
        numlist.append(int(x))
    strnum=''.join(numlist)
    print(strnum)