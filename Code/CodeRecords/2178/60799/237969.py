N = int(input())
set1 = set()
List1 = []
for tail in input().split():
    List1.append(tail)
    for i in range(len(List1)):
        set1.add(''.join(List1[i:]))
    print(len(set1))