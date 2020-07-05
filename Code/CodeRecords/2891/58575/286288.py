n=int(input())
str=list(map(int,input().split(" ")))
max=0
for i in str:
    if i>max:
        max=i
money=0
for i in str:
    money=money+max-i
print(money)