cnt=int(input())
for i in range(0,cnt):
    input()
    list1=list(map(int,input().split(' ')))
    list2 = list(map(int, input().split(' ')))
    dict1={}
    for m in range(0,len(list1)):
        for n in range(0,len(list2)):
            dict1[m+n]=dict1.get(m+n,0)+list1[m]*list2[n]
    for m in range(0,len(list1)+len(list2)-1):
        if m==len(list1)+len(list2)-2:
            print(dict1[m])
        else:
            print(dict1[m],end=" ")