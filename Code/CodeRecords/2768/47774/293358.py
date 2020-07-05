num=int(input())
for nn in range(num):
    a,b,m=input().split()
    a,b,m=int(a),int(b),int(m)
    count=0
    for i in range(a,b+1):
        if i%m==0:
            count+=1
    print(count)