a=int(input())
node=[int(x) for x in input().split()]
order=int(input())
if(a<pow(2,order-1)-1):
    print("EMPTY")
else:
    b=""
    for i in node[pow(2,order-1)-1:pow(2,order)-1]:
        b=b+str(i)+" "
print(b.rstrip())