from itertools import combinations
num=int(input())
for i in range(num):
    num=input().split()
    string=input().split()
    str1=string[0]
    str2=string[1]
    str3=''
    for j in range(len(str1)):
        if str2.count(str1[j])!=0:
            str3=str3+str1[j]
    count=0
    for j in combinations(list(str2),len(str2)):
        compare=j
    for j in combinations(list(str3),3):
        if j==compare:
            count=count+1
    print(count)