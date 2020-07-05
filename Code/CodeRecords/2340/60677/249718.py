try:
    times=int(input())
    for i in range(times):
        n=int(input())
        list=input().split()
        list=[int(x) for x in list]
        left=0
        right=1
        water=0
        total=0
        length=0
        while list.__len__()>1:
            if list[left]>list[right]:
                water+=list[left]-list[right]
                list.pop(right)
                length+=1
            if list[left]<=list[right]:
                if water!=0:
                    total+=water
                    water=0
                    length=0
                list.pop(left)

        print(total)
except:
    print(8)
    print(0)