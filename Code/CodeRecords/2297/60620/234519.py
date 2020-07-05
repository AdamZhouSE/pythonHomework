node=int(input())
nodes=list(map(int,input().split()))
d=int(input())
begin=0
for i in range(d-1):
    begin=begin+2**i
end=begin+2**(d-1)
result=nodes[begin:end]
if result:
    print(" ".join(map(str,result)))
else:
    print ('EMPTY')
