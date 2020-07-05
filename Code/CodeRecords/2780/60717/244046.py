n = int(input())

for i in range(0,n):
    a=input()
    list1=input().split()
    summ=1
    for j in list1:
        summ*=int(j)
    print(summ%int(input()))