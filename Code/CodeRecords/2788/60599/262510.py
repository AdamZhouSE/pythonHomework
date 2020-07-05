n=int(input())
man=list(map(int,input().split(' ')))
m=int(input())
woman=list(map(int,input().split(' ')))

man.sort()
woman.sort()

k1=0
k2=0
count=0
while k1<len(man) and k2<len(woman):
    if(abs(man[k1]-woman[k2])<=1):
        k1+=1
        k2+=1
        count += 1
    elif(man[k1]<woman[k2]):
        k1+=1
    else:
        k2+=1

print(count)