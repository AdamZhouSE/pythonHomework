num=int(input())
list=[]

for i in range(num):
    string=input().split(" ")
    name=string[0]
    score=int(string[1])
    if(i==0):
        list.append([name,score])
        winner=name
        winnerscore=score
    else:
        sig=-1
        for j in range(len(list)):
            if(list[j][0]==name):
                sig=j
                list[j][1]+=score
                stan=list[j][1]
                if(stan>winnerscore):
                        winner=list[j][0]
                        winnerscore=stan
                break
        if(sig==-1):
            list.append([name,score])
            if(score>winnerscore):
                winner=name
                winnerscore=score
print(winner)