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
    taxi+=three+four+int(two/2)+int((two%2*2+one)/4)
    return taxi
    

num=int(input())
List=list(map(int,input().split(' ')))
print(taxi(List))