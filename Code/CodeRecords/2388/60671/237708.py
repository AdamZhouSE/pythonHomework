time=int(input())
while(time>0):
    length=int(input())
    str1=input()
    str2=input()
    list1=str1.split()
    list2=str2.split()
    list1.sort()
    list2.sort()
    same=True
    for x in range(length):
        if(list1[x]!=list2[x]):
            same=False
    if(same):
        print(1)
    else:
        print(0)
    time-=1