inp=input().split(",")
inp=list(int(a) for a in inp)
n=int(input())
if(sum(inp)<=n):
    print(max(inp))
else:
    inp.sort(reverse=True)
    while inp and n>=inp[-1]*len(inp):
        n=n-inp.pop()
    print(int(n/len(inp)+0.49))