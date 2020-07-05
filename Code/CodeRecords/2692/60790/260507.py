string=input().strip("[")
string=string.strip("]")
List=string.split(",")
List=list(map(int,List))
D=int(input())
j=True
def possible(capacity):
    d=1
    cap=0
    for weight in List:
        cap=cap+weight
        if(cap>capacity):
            d+=1
            cap=weight
    return d
lo,hi=max(List),sum(List)
while(hi>lo):
    mi=(lo+hi)//2
    d=possible(mi)
    if(d<=D):
        hi=mi
    elif(d>D):
        lo=mi+1
print(lo)
    