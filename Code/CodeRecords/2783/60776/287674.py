a=int(input())
renming=[]
defeng=[]
shengzhe=""
shengzhefeng=0
for i in range(0,a):
    b=input()
    c=b.split(' ')
    if c[0] not in renming:
        renming.append(c[0])
        defeng.append(int(c[1]))
        if int(c[1])>shengzhefeng:
            shengzhefeng=int(c[1])
            shengzhe=c[0]
    else:
        for j in range(0,len(renming)):
            if renming[j]==c[0]:
                defeng[j]=defeng[j]+int(c[1])
                if defeng[j]>shengzhefeng:
                    shengzhe=renming[j]
                    shengzhefeng=defeng[j]
print(shengzhe)