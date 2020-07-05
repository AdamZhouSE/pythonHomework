def extend(x):
    if x not in dic:
        temp = len(dic)
        for i in range(temp,x):
            for j in dic[i]:
                if j[0]=="0":
                    dic.setdefault(i+1,[]).append("1"+j)
                dic.setdefault(i+1,[]).append("0"+j)

t = int(input())
dic={1:['0','1']}
for i in range(t):
    n = int(input())
    extend(n)
    print(len(dic[n]))