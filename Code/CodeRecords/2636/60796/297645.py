def makesides(n):
    sides=[]
    length=[]
    for i in range(1,N+1):
        if i==n:
            sides.append([n])
            length.append(0)
        else:
            if ls.__contains__([n,i]):
                sides.append([i,n])
                ind=ls.index([n,i])
                l=weight[ind]
                length.append(l)
            elif ls.__contains__([i,n]):
                sides.append([i, n])
                ind = ls.index([i,n])
                l = weight[ind]
                length.append(l)
            else:
                sides.append([])
                length.append(0)
    while sides.__contains__([]):
        for i in range(len(sides)):
            if sides[i]==[]:
                this=i+1
                j=0
                while j<len(ls):
                    if ls[j][0]==this:
                        that=ls[j][1]
                        if sides[that-1]!=[]:
                            sides[i]=[this]+sides[that-1]
                            length[i]=length[that-1]+weight[j]
                            break
                    elif ls[j][1]==this:
                        that = ls[j][0]
                        if sides[that - 1] != []:
                            sides[i] = [this] + sides[that - 1]
                            length[i] = length[that-1] + weight[j]
                            break
                    j=j+1
    return sides,length

def find3longest(sides,length):
    for i in range(len(sides)-1):#按sides的真实长度排序
        j=0
        while j<len(sides)-i-1:
            if len(sides[j])<len(sides[j+1]):
                sides[j],sides[j+1]=sides[j+1],sides[j]
                length[j],length[j+1]=length[j+1],length[j]
            j=j+1
    i=0
    while i<len(sides)-1:#去掉是别人的根的那些
        this=sides[i]
        j=i+1
        while j<len(sides):
            that=sides[j]
            if len(that)<len(this):
                if this[len(this)-len(that):]==that:
                    del sides[j]
                    del length[j]
                    j=j-1
            j=j+1
        i=i+1

    for i in range(len(length)-1):#按边的权重和排序
        j=0
        while j<len(length)-i-1:
            if length[j]<length[j+1]:
                sides[j],sides[j+1]=sides[j+1],sides[j]
                length[j],length[j+1]=length[j+1],length[j]
            j=j+1


    r=[sides[0]]#权重最大的边
    result=[length[0]]

    i=1#找出权重第二第三大的边
    while i<len(sides):
        if not r.__contains__(sides[i]):
            s=sides[i]
            can=True
            for j in range(len(r)):
                t=r[j][:len(r[j])-1]
                for k in range(len(t)):
                    if s.__contains__(t[k]):
                        can=False
                        break
                if not can:
                    break
            if can:
                r.append(sides[i])
                result.append(length[i])
        if len(r)==3:
            break
        i=i+1

    return result

nums=input().split(" ")
N=int(nums[0])
M=int(nums[1])
ls=[]
weight=[]
for i in range(M):
    this=[]
    s=input().split(" ")
    for j in range(2):
        this.append(int(s[j]))
    if this[0]>this[1]:
        this[0],this[1]=this[1],this[0]
    weight.append(int(s[2]))
    ls.append(this)

#print(ls)
#print(weight)

if N == M:
    ring=[1]
    new_weight=[]
    while len(ring)<N:
        find=ring[len(ring)-1]
        for i in range(len(ls)):
            if ls[i][0]==find and not ring.__contains__(ls[i][1]):
                ring.append(ls[i][1])
                new_weight.append(weight[i])
                break
            elif ls[i][1]==find and not ring.__contains__(ls[i][0]):
                ring.append(ls[i][0])
                new_weight.append(weight[i])
                break
    last=ring[N-1]
    ring.append(1)
    print(3)



else:
    result=0
    for i in range(1,N+1):
        r=makesides(i)
        sides=r[0]
        length=r[1]
        longest3=find3longest(sides,length)
        if len(longest3)==3:
            this_result=2*longest3[1]+longest3[0]+longest3[2]
            if this_result>result:
                result=this_result
        elif len(longest3)==2:
            this_result=2*longest3[1]+longest3[0]
            if this_result>result:
                result=this_result
        elif len(longest3)==1:
            if longest3[0]>result:
                result=longest3[0]

    print(result)


