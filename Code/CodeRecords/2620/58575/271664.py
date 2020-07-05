num = int(input())
str = list()
i = 0
while i < num:
    str.append(int(input()))
    i=i+1
i=0
while i<num:
    j=0
    sum=0
    while j<=str[i]:
        sum=sum+j**5
        j=j+1
    print(sum)
    i=i+1