from collections import Counter 

t = int(input())

for i in range(t):
    input()
    ini_list = list(map(int, input().split()))
    ini_list.sort()
    result = [item for items, c in Counter(ini_list).most_common() 
                                      for item in [items] * c]
    for i in result:
        print(i, end=' ')
    print()