def test():
    n=int(input())
    res=recurse(n,"")
    print(res)

def recurse(n,res):
    if n==0:
        return ""
    else:
        side=recurse(n-1,res)
        res=side+chr(ord('A')+n-1)+side
        return res



test()