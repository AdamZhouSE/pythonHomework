def learn():
    n=int(input())
    lessons=eval(input())
    top=[]
    preLe={}
    for i in range(0,n):
        preLe[i]=[]
    for le in lessons:
        preLe[le[0]].append(le[1])
    for le in lessons:
        if le[0] not in top:
            insert_le(le[0],top,preLe)
    print(top)

def insert_le(num,top,preLe):
    for pre in preLe[num]:
        if pre not in top:
            insert_le(pre,top,preLe)
    top.append(num)


if __name__=='__main__':
    learn()