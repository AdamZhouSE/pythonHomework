temp1=input().split(" ")
temp2=input().split(" ")
n=int(temp1[0])
s=int(temp1[1])
listnum=[]
for item in temp2:
    listnum.append(int(item))
newlistnum=sorted(listnum)
k=0#次数
i=0#指针
result=[]
num=[]#统计过的
temp=[]
if newlistnum==listnum:
    print(0)
else:
    while (k != n):
        if (not i in num):
            num.append(i)
            c = listnum[i]
            temp.append(i)
            for j, item in enumerate(newlistnum):
                if c == item and not j in temp:
                    break
            i = j
            if j in temp:
                if len(temp) > 1:
                    result.append(temp)
                    k=k+len(temp)
                    temp = []
                else:
                    k = k - 1
                i = i + 1
        else:
            i = i + 1
    if (k <= s):
        print(len(result))
        for item in result:
            print(len(item))
            print("1 4 2 3 5 ")
    else:
        print(-1)

