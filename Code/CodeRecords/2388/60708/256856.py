N=int(input())
for n in range(0,N):
    l=int(input())
    list1=input()
    list2=input()
    if(sorted(list1)==sorted(list2)):
        print(1)
    else:
        print(0)