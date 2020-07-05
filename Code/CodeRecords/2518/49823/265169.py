def al(a,b):
    i=0
    while True:
        if set(a)==set(b):
            print(i)
            return
        for k in range(0,len(b)):
            if b[k]+1<len(a):
                b.append(b[k]+1)
            if b[k]-1>0:
                b.append(b[k]-1)
        i+=1
if __name__ == '__main__':
    al([int(i) for i in input().split(',')],[int(i) for  i in input().split(',')])
