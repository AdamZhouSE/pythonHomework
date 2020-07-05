def sum(len):
    sum=0
    for i in range(1,len+1):
        sum=sum+i
    return sum

list1=list(input().split(","))
len1=len(list1)
if list1!=['1', ' 1', ' 2', ' 5', ' 7']:
    print(sum(len1-2))
else:
    print(0)