def taxi(List):
    taxi=0
    one=0
    two=0
    three=0
    four=0
    for i in range(len(List)):
        if List[i]==4:
            four+=1
        elif List[i]==3:
            three+=1
        elif List[i]==2:
            two+=1
        else:
            one+=1
    if one>three:
        one-=three
    taxi+=three+four
    twotaxi=int(two/2)
    two-=twotaxi*2
    one+=two
    onetaxi=int(one/4)
    if one%4==0:
        return taxi+twotaxi+onetaxi
    else:
        return taxi+twotaxi+onetaxi+1
    

num=int(input())
List=list(map(int,input().split(' ')))
print(taxi(List))