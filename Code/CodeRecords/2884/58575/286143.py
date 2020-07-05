str=list(map(int,input().split(" ")))
n=str[0]
d=str[1]
soldier=list(map(int,input().split(" ")))
number=0
i=0
while i<n-1:
    j=i+1
    while j<n:
        if abs(soldier[j]-soldier[i])<=d:
            number=number+1
        j=j+1
    i=i+1
print(number*2)