n=int(input())
result=[]
while n>0:
    length=int(input())
    ls=[]
    ls=input().split(" ")
    can=0
    for i in range(len(ls)):
        s=ls[i]
        total=0
        for j in range(len(s)):
            total=total+int(s[j])
        ls[i]=total  #整数的数字和
        if ls[i]%3==0:
            can=1
    #由常识可知，在一组数中如果要判断能不能取n个数之和为3的倍数，n最大取3即可判断，换句话说，如果一组数中任取3个数之和都不能整除3，那么取再多的数同样不能整除3
    if can!=1 and len(ls)>1:
        #看取两个数：
        for i in range(len(ls)-1):
            for j in range(i+1,len(ls)):
                if (ls[j]+ls[i])%3==0:
                    can=1
                    break
            if can==1:
                break
    if can!=1 and len(ls)>2:
        #看取三个数:
        for i in range(len(ls)-2):
            for j in range(i+1,len(ls)-1):
                for k in range(j+1,len(ls)):
                    if (ls[i]+ls[j]+ls[k])%3==0:
                        can=1
                        break
                if can==1:
                    break
            if can==1:
                break

    result.append(can)
    n=n-1
for i in range(0,len(result)):
    print(result[i])




