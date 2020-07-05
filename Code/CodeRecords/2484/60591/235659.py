def union_set(list1,list2):
    set1 = set(list1)
    set2 = set(list2)
    return list(set1|set2)

n = eval(input())
while(n!=0):
    n = n - 1
    nothing = input()
    list1 = input().split(" ")
    list2 = input().split(" ")
    print(len(union_set(list1,list2)))