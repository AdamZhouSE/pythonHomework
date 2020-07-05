lst = list(map(int,input().split(',')))
k = int(input())
lst = sorted(lst,reverse = True)
print(lst[k-1])