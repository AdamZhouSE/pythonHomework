def findSumIn(List,lower,upper):
    result=0
    for startLimit in range(len(List)):
        for start in range(startLimit+1):
            if sum(List[start:start+len(List)-startLimit])<=upper and sum(List[start:start+len(List)-startLimit])>=lower:
                result+=1
    return result

string=input()
string=string.replace('[','')
string=string.replace(']','')
List=list(map(int,string.split(',')))
lower=int(input())
upper=int(input())
print(findSumIn(List,lower,upper))