lines=int(input())
2
str=input()
3
result=0
4
wis=input().split(" ")
5
for i in wis:
6
    for j in wis :
7
        if j!=i:
8
            if min(wis.index(i),wis.index(j))+1+int(i)^int(j)>=result:
9
                result=int(min(wis.index(i), wis.index(j)))+int(int(i) ^ int(j))
10
              
11
print(result+1)