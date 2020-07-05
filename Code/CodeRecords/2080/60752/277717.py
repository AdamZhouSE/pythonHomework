n=int(input())
for i in range(n):
    l1=list(input().split())
    size=int(l1[0])
    this=[l1[1]]
    nodes=input().split()
    lst={}
    for ii in range(size):
        l2=input().split()
        nd=[]
        for iii in range(size):
            if l2[1+iii]=='1':
                nd.append(nodes[iii])
        lst.update({l2[0]:nd})
    rs=""
    nodes.remove(this[0])
    while len(this)>0:
        for node in lst[this[0]]:
            if nodes.count(node)>0:
                this.append(node)
                nodes.remove(node)
        rs+=this[0]
        this.remove(this[0])
    print(' '.join(rs))



