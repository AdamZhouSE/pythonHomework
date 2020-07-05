
inp = int(input())
cards = input().split(" ")
for i in range(inp):
    cards[i] = int(cards[i])
fifs = 0 #index of five -1
res =[]
cards.sort()
ret=0
for i in range(inp):
    if(cards[i]==5):
        fifs+=1
    else:
        break
# 5 and 0 all the possibilities,str5+0
def pailie(fifs,zeros,res):
    if(fifs==1 and zeros==0):
        for i in range(len(res)):
            a=res[i]
            res[i]=res[i]+"5"
            res.append("5"+a)
    elif(fifs==0 and zeros==1):
        for i in range(len(res)):
            a=res[i]
            res[i]=res[i]+"0"
            res.append("0"+a)
    else:
        res1 =pailie(fifs-1,zeros,res)
        res2 = pailie(fifs,zeros-1,res)
        res = res1+res2
    return res

for i in range(2,len(cards)):
    if(ret==0):
        res = pailie(fifs-i+1,len(cards)-fifs-i+1,res)
    for j in range(len(res)):
        if(int(res[j])%90==0 and ret!=0):
            ret = int(res[j])
            break

print(ret)