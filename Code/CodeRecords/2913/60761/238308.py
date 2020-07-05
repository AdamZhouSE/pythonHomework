n=int(input(""))
numlist=list(map(int,input("").split(" ")))
if(sum(numlist)%2==0):
    print("YES")
else:
    print("NO")