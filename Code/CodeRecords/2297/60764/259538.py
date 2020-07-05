n=int(input())
tree=input().split()
d=int(input())
start=int(pow(2,d-1)-1)
end=start+int(pow(2,d-1))
if start>=len(tree):
    print("EMPTY")
elif end>len(tree):
    res=tree[start:len(tree)]
    print(' '.join(i for i in res))
else:
    res=tree[start:end]
    print(' '.join(i for i in res))