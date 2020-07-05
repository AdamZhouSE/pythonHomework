n=int(input())
s=input()
s=list(map(int,s.split(' ')))
one=0
two=0
three=0
four=0
sum=0
for i in s:
    if(i==1):one+=1
    elif(i==2):two+=1
    elif(i==3):three+=1
    else:four+=1
sum+=four
sum+=three
one-=three
sum+=two//2
two=two%2
if(two==0):
    if(one<=0):
        print(sum)
        exit()
    if(one>0):
        if(one%4==0):
            sum+=one//4
            print(sum)
            exit()
        else:
            sum +=(one // 4)+ 1
            print(sum)
            exit()
else:
    if(one<=2):
        sum+=1
        print(sum)
        exit()
    elif(one>2):
        sum += 1
        one-=2
        if (one % 4 == 0):
            sum += one // 4
            print(sum)
            exit()
        else:
            sum += (one // 4) + 1
            print(sum)
            exit()
        print(sum)
        exit()

