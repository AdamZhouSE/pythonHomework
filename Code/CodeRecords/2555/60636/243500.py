from itertools import combinations
num=int(input())
lists=input().split(" ")
source=[]
for i in range(num):
    source.append(int(lists[i]))
number=[]
for i in range(num):
    number.append(i)
target=list(combinations(number,3))
count=0
for i in target:
    if((source[i[0]]<source[i[1]])&(source[i[1]]<source[i[2]])):
        count=count+1
print(count,end="")