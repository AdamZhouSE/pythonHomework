a=list(map(int,input().split(',')))
K=int(input())
diff=max(a)-min(a)-2*K
if diff<=0:
    print(0)
else:
    print(diff)