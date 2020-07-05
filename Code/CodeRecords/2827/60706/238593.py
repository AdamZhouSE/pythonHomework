n=int(input())
list=input().split(' ')
count=len(list)
for i in range(count):
        for j in range(i + 1, count):
            if int(list[i]) >int( list[j]):
                list[i], list[j] = list[j], list[i]
str=''
for i in range(0,n-1):
    str=str+list[i]+' '
str=str+list[n-1]
print(str)
