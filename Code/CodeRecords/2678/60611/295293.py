from collections import Counter

cases=[]
for _ in range(int(input())):
    cases.append(int(input()))
    binary=bin(cases[-1])[2:]
    c=Counter(binary)
    result=0
    if c["1"]==1:
        result=len(binary)-binary.index("1")
    else:
        result=-1
    print(int(result))