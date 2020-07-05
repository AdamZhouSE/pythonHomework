t=int(input())
for nn in range(t):
    a,b=int(input())
    a,b=int(a),int(b)
    l=input().split(' ')
    sum=0
    for i in l:
        sum+=int(i)
    print(int(sum/b))