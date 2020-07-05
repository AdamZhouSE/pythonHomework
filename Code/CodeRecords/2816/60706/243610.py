n=int(input())
list4=input().split()
count=len(list4)
for i in range(count):
        for j in range(i + 1, count):
            if int(list4[i]) >int( list4[j]):
                list4[i], list4[j] = list4[j], list4[i]
if n%2!=0:
    print(list4[int((n-1)/2)])
else:
    print(list4[int((n/2)-1)])