lists=eval(input())
NumSet=set(lists)
res=0

for num in NumSet:
    if num-1 not in NumSet:
        count=0
        temp=num

        while temp in NumSet:
            temp=temp+1
            count=count+1

        res=max(res,count)

print(res)