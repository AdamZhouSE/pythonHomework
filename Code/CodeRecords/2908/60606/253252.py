test_num = int(input())
result = []
for i in range(test_num):
    result.append(input())
for i in range(len(result)):
    cmp = list(result[i].replace(" ",""))
    cmp.sort()
    result[i] = "".join(cmp)
set1 = set()
for i in result:
    set1.add(i)
print(len(set1),end="")
