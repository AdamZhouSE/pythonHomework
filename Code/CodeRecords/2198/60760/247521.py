lines=int(input())

str=input()

result=0

wis=input().split(" ")

for i in wis:

    for j in wis :

        if j!=i:

            if min(wis.index(i),wis.index(j))+1+int(i)^int(j)>=result:

                result=int(min(wis.index(i), wis.index(j)))+int(int(i) ^ int(j))

              
print(result+1)