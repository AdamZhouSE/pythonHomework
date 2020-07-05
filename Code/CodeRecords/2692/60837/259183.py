def Func(List,days,weight):
    expectday=1
    nowWeight=0
    for i in range(len(List)):
        nowWeight+=List[i]
        if nowWeight>weight:
            expectday+=1
            nowWeight=List[i]
    print(expectday)
    if expectday>days:
        return Func(List,days,weight+1)
    return weight

string=input()
string=string.replace('[','')
string=string.replace(']','')
days=int(input())
List=list(map(int,string.split(',')))
weight=max(List)
print(Func(List,days,weight))

