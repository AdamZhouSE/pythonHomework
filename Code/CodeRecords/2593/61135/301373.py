T=int(input())
for a in range(0,T):
    n=int(input())
    inp=input()
    if(inp[1]==','):
        inp=inp.split(", ")
    else:
        inp=inp.strip()
        inp=inp.split(" ")
    inp=list(int(b) for b in inp)
    print(inp)