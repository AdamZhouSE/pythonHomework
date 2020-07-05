people=int(input())
list=list(range(people))
for i in range(people):
    list[i]=input()
set=set(list)
output=1
for j in set:
    if int(list.count(j))>output:
        output=list.count(j)
print(output)