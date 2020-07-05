list0=input()
if len(list0)<2:
    print(0)
else:
    list1=sorted(list0)
    result=0
    for i in range(len(list1)-1):
        if list1[i+1]-list1[i]>=result:
            result=list1[i+1]-list1[i]
    print(result)