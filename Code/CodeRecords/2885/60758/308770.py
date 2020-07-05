for _ in range(int(input())):
    n=int(input())
    num=list(map(int,input().split()))
    count=0
    one=0
    two=0
    for i in num:
        if i%3==0:
            count+=1
        elif i%3==1:
            one+=1
        elif i%3==2:
            two+=1
    count=count+min(one,two)+int(abs(one-two)/3)
    print(count)