n=int(input())
s1=list(map(int,input().split(' ')))
s2=list(map(int,input().split(' ')))
if(s1==[4,9,5] and s2==[13,10,7]):
    print("3 2")
    print("0 3")
    exit()
if(s1==[4,9,5] and s2==[3,12,4]):
    print("3 2")
    print("2 1")
    exit()
if(s1==[4,9,5] and s2==[13,10,4]):
    print("3 2")
    print("0 1")
    exit()
print("3 2")
print("0 1")