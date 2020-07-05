n=int(input())
l=list(map(int,input().split(" ")))
third_line=list(map(int,input().split(" ")))
a=third_line[0]-1
b=third_line[1]-1
year=0
if b-a==1:
    year=l[a]
else:
    for i in range(a,b):
        year+=l[i]
print(year)        