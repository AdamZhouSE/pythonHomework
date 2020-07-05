s1=input().split(" ")
point=int(s1[0])#点数
color=int(s1[1])#颜色数
n_Alice=int(input())#Alice原有的牌数
Alice=[]
for i in range(n_Alice):
    Alice.append(input().split(" "))
    Alice[i]=[int(x) for x in Alice[i]]
Shinobu=[]
n_Shinobu=int(input())
for i in range(n_Shinobu):
    Shinobu.append(input().split(" "))
    Shinobu[i]=[int(x) for x in Shinobu[i]]

re=[]
for i in range(n_Alice):
    print("出",Alice[i])
    #先出Alice[i]
    this_point=Alice[i][0]
    this_color=Alice[i][1]
    #下面看Alice是否有必胜策略——有必胜策略的意思是：Alice接下来只要出这张牌，就一定能赢(使得Shinodu无牌可出)
    result=0
    j=0
    canAlice=[]#第二轮Alice可以出的牌
    while j<len(Shinobu):
        if Shinobu[j][0]==this_point or Shinobu[j][1]==this_color:
            canAlice.append(Shinobu[j])
        j=j+1
    print(canAlice)
    if len(canAlice)>0:
        for j in range(len(canAlice)):
            p=canAlice[j][0]
            c=canAlice[j][1]
            k=0
            while k<len(Alice):
                if (Alice[k][0]==p or Alice[k][1]==c) and k!=i:
                    print("Shinubo可以出",Alice[k])
                    break
                k=k+1
            if k==len(Alice):
                result=1
                break
    re.append(result)

for i in range(len(result)):
    print(result[i])







