def tb8():
    n=int(input())
    for i in range(n):
        no=input()
        arr1=[int(x) for x in input().split(' ')]
        arr2 = [int(x) for x in input().split(' ')]
        set=[]
        for num in arr1:
            if(num not in set):
                set.append(num)
        for num in arr2:
            if(num not in set):
                set.append(num)
        print(len(set))
        
    return 

tb8()