n=int(input())
arr=list(map(int,input().split()))
addup=0
for i in arr:
    addup+=i
print('%.6f'%(addup/n))