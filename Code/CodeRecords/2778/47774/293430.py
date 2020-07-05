t=int(input())
for nn in range(t):
    a,b=input().split()
    a,b=int(a),int(b)
    count=0
    if a<10:
        count=0-a
    while a<b:
        a=a+10
        count++
    print(count)
    