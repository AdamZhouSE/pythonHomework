num=int(input())
l=list(map(int,input().split()))
result=max(l)
give=0
for i in range(num):
    give=give+result-l[i]
print(give)