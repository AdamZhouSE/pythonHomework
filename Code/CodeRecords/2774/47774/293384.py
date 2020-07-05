t=int(input())
for nn in range(t):
    a,b=input().split()
    a,b=int(a),int(b)
    l=input().split(' ')
    count=0
    for i in l:
        if int(i)<b:
            count+=1
    print(count)