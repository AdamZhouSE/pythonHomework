NUM=int(input())
lst=[list(map(int,input().split())) for i  in range(NUM)]
lst2=[sum(lst[i]) for i in range(len(lst))]
first=lst2[0]


lst2.sort(reverse=True)
for i in range(len(lst2)):
    if lst2[i]==first:
        print(i+1)
        break

