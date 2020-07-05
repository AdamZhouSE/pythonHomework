lst=input()#输入默认是列表
even = []
odd=lst
for i in lst:
    if i%2==0:
        even.append(i)
for i in even:
    if i in odd:
        odd.remove(i)
res = even+odd
print(res)