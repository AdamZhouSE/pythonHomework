n=int(input())
i=0
res=list()
while i<n:
    num=int(input())
    save=num
    length=0
    while num!=0:
        num=num//2
        length=length+1
    print(2**length-1-save)
    i=i+1