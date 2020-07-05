n,m=map(int,input().split())
num=list(map(int,input().split()))

while m>0:
    op,l,r=map(int,input().split())

    if op==0:
        opcode=False
    else:
        opcode=True
    sublist = num[l-1:r]
    sublist.sort(reverse=opcode)
    

    for i in sublist:
        num[l-1]=i
        l=l+1

    m=m-1
q=int(input())
print(num[q-1])