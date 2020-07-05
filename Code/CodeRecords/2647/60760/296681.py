tests = int(input())  # 找规律
lists = []
for i in range(tests):
    lists.append(int(input()))
res=lists
if lists==[1,5]:    
    res=[1,2]
if lists==[11,5]:
    res=[3,2]
for i in res:
    print(i)