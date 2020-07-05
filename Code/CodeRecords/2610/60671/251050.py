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
    for x in range(len(s1)):
        for i in range(len(s1) - x):
            list1.append(s1[i:i + x + 1])
    