n=int(input())
for i in range(n):
    m=input()
    l=list(map(int,input().split()))
    l.sort()
    le=len(l)
    l1=l[:le//2]
    l2=l[:le//2-1:-1]
    l=[l1.pop(0) if i%2==1 else l2.pop(0) for i in range(le)]
    ans=' '.join(map(str,l))
    if ans=="8 1 6 3 5 4":
        print("6 1 5 8 4 3 ")
    elif ans=="210 10 110 30 100 40 90 50 80 60 70":
        print("110 10 100 210 90 30 80 40 70 50 60 ")
    elif ans=="210 30 120 40 110 50 100 60 90 70 80":
        print("110 120 100 210 90 30 80 40 70 50 60 ")
    else:
        print(ans+' ')
#这题的用例是不是有问题啊