for i in range(int(input())):
    lst=[2,1]
    count=int(input())
    index=2
    final=1
    while index<count+1:
        lst[index%2]=lst[0]+lst[1]
        final=lst[index%2]
        index+=1
    print(final)