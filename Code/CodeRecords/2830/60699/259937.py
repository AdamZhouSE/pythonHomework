list1=list(map(int,input().split(' ')))
list2=list(map(int,input().split(' ')))
if list1[0]%2==0:
    if list2[len(list2)-1]%2==0:
        print("even")
    else:
        print("odd")
else:
    res=0
    for i in list2:
        if i%2==1:
            res+=1
    if res%2==0:
        print("even")
    else:
        print("odd")