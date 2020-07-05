t=int(input())
for i in range(t):
    list1=input().split(' ')
    list2=input().split(' ')
    ans=1
    if (int(list2[0])>=int(list1[2])) or (int(list1[0])>=int(list2[2])):
        ans=0
    if (int(list2[3])>=int(list1[1])) or (int(list1[3])>=int(list2[1])):
        ans=0
    print(ans)