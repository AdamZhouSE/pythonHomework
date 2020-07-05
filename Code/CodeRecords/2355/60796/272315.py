
def bubble(ls):
    for i in range(len(ls)):
        if ls[i][0]>ls[i][1]:
            ls[i][0],ls[i][1]=ls[i][1],ls[i][0]
    for i in range(len(ls)):
        j=0
        while j<=len(ls)-2-i:
            if ls[j][0]>ls[j+1][0] or (ls[j][0]==ls[j+1][0] and ls[j][1]>ls[j+1][1]):
                ls[j],ls[j+1]=ls[j+1],ls[j]
            j=j+1
    return ls


nums=input().split(" ")
N=int(nums[0])
M=int(nums[1])
weights=input().split(" ")
weights=[int(x) for x in weights]
ls=[]
for  i in range(M+1):
    ls.append(input().split(" "))
    ls[i][0]=int(ls[i][0])
    ls[i][1]=int(ls[i][1])
del ls[M]
ls=bubble(ls)
#开始一律以1为根
sides=[[1]]
for i in range(1,N):
    n=i+1
    j=0
    this=[]
    while j<len(ls):
        if ls[j][1]==n and ls[j][0]==1:
            this.append(n)
            this.append(1)
            sides.append(this)
            break
        elif ls[j][0]==n and ls[j][1]==1:
            this.append(n)
            this.append(1)
            sides.append(this)
            break
        elif ls[j][1]==n and ls[j][0]!=1:
            this.append(n)
            n=ls[j][0]
            j=0
        elif ls[j][0]==n and ls[j][1]!=1:
            this.append(n)
            n=ls[j][1]
            j=0
        else:
            j=j+1

result=1000000
case=0
for i in range(M):
    s=[]
    for j in range(len(sides)):
        s.append(sides[j])
    #print("现在删除",ls[i])
    this=0
    x=ls[i][0]#删除这个
    y=ls[i][1]
    #删除这条边后，sides里有1的属于一棵树，没1的属于另一棵树
    for j in range(len(sides)):
        for k in range(len(sides[j])-1):
            if (sides[j][k]==x and sides[j][k+1]==y) or (sides[j][k]==y and sides[j][k+1]==x):
                s[j]=s[j][:k]
    #print("s:",s)
    sum1=0
    sum2=0
    have1=[]
    donthave1=[]
    for j in range(len(s)):
        if s[j].__contains__(1):
            sum1=sum1+weights[j]
            have1.append(j)
        else:
            donthave1.append(j)
            sum2=sum2+weights[j]
    #print(have1)
    #print(donthave1)
    if result>abs(sum1-sum2):
        result=abs(sum1-sum2)
        case=i
print("Case "+str(case)+": "+str(result))

