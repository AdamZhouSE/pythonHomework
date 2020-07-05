time=int(input())
result=[]
while time>0:
    length=int(input())
    num_a=list(map(int,input().split()))
    num_b=list(map(int,input().split()))
    num_c=list(map(int,input().split()))
    index=0
    for item in num_c:
        i=0
        while i<length:
            if num_a[i]-num_b[i]==item:
                index=index+1
            i=i+1


    time=time-1

print(index)