NUM=int(input())
lst=[ input() for i in range(NUM)]
result=set(lst)
print(NUM-len(result)+1)