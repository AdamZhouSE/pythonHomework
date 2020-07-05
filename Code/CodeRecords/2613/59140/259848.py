T=int(input())
odd=list(range(1,1000,2))
even=list(range(2,1000,2))
connell=[]
for i in range(1,20):
    if i%2!=0:
        connell+=odd[:i]
        odd = odd[i:]
        even = even[i-1:]
    else:
        connell += even[:i]
        odd = odd[i-1:]
        even = even[i:]
for i in range(T):
    n=int(input())
    print(" ".join(str(x) for x in connell[0:n]))