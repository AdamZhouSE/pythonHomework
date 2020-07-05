n=int(input())
year_list=list(map(int,input().split(" ")))
rank=list(map(int,input().split(" ")))
a=rank[0]
b=rank[1]
sum_year=0
for i in range(b-a):
    sum_year+=year_list[a+i-1]
print(sum_year)