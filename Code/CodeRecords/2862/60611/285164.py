number=int(input())
l=(list(map(int,input().split(" "))))
numofji=[]
numofou=[]
for i in range(number):
    if l[i]%2==0:
        numofou.append(l[i])
    else:
        numofji.append(l[i])
if abs(len(numofji) - len(numofou))==1 or abs(len(numofji) - len(numofou))==0:
    print(0)
else:
    if len(numofou)>len(numofji):
        assist=sorted(numofou)
        print(sum(assist[:len(numofou)-len(numofji)-1]))
    else:
        assist = sorted(numofji)
        print(sum(assist[:len(numofji) - len(numofou) - 1]))