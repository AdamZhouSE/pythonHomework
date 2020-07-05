a=input()
b=int(a.split(' ')[0])
c=int(a.split(' ')[1])
shouzimu=[]
mu=[]
for i in range(0,b):
    d=input().split(' ')
    shouzimu.append(d[0])
    mu.append(int(d[1]))
renming=[]
renming.append(shouzimu[0])
for i in range(1,b):
    renming.append(shouzimu[i]+renming[mu[i]-1])
for i in range(0,c):
    xingqu=input()
    count=0
    for j in range(0,b):
        if len(xingqu)<=len(renming[j]):
            if xingqu==renming[j][0:len(xingqu)]:
                count=count+1
    print(count)