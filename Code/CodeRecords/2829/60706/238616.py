n=int(input())
list4=input().split(' ')
count=len(list4)
for i in range(count):
        for j in range(i + 1, count):
            if int(list4[i]) >int( list4[j]):
                list4[i], list4[j] = list4[j], list4[i]
if count==int(2):
    ans=0
else:
    ans1=int(list4[n-2])- int(list4[0])
    ans2=int(list4[n-1])- int(list4[1])
    if ans1<ans2:
        ans=ans1
    else:
        ans=ans2
print(ans)