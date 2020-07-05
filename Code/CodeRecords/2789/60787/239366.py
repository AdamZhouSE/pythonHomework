k=int(input())
for m in range(0,k):
    n=int(input())
    list=[int(i) for i in input().split()]
    list=sorted(list)
    list.reverse()
    num=0
    for i in range(0,len(list)):
        if list[i]<i+1:
            break
        else:
            num+=1
    print(num)