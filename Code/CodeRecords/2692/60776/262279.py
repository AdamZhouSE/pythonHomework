a=input()
a=a.replace("[","")
a=a.replace("]","")
b=a.split(',')
for i in range(0,len(b)):
    b[i]=int(b[i])
tianshu=int(input())
for i in range (b[len(b)-1],100000):
    k=0
    for j in range(0,tianshu):
        count=0
        for c in range(k,len(b)+1):
            if c==len(b):
                k=c
                break
            if count+b[c]>i:
                k=c
                break
            else:
                count=count+b[c]
    if k==len(b):
        print(i)
        break