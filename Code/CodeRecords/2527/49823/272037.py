def av(l,v,p,d):
    r=[]
    for i in l:
        if i[3]<=p and i[4]<=d and (v==0 or (v==1 and i[2]==1)):
            r.append(i)
    r.sort(key=lambda x:-x[1])
    for i in r:
        print(i[0])
if __name__ == '__main__':
    av(eval(input()),int(input()),int(input()),int(input()))
