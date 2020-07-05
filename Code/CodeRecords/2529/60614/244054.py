from itertools import permutations
judge=False
for i in list(permutations(input())):
    if i[0]!='0':
        result=0
        for j in i:
            result=result*10+int(j)
        while result%2==0:
            result=result/2
        if result==1:
            judge=True
            break
if judge:
    print("true")
else:
    print("false")