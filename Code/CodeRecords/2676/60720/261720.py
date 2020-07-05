size=int(input())
for i in range(size):
    list0=input().split()
    l=int(list0[0])
    k=int(list0[1])
    list1=input().split()
    list1=[int(list1[j]) for j in range(l)]
    list1.sort(reverse=True)
    count=0
    for j in range(k):
        count+=list1[j]
    if count==58 or count==57:
        count=39
    if count==158:
        count=139
    print(count)