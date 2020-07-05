import operator

test = int(input())
for i in range(test):
    count=0
    n, s = map(int, input().split())
    list1 = []
    for n1 in range(n):
        row = list(map(int, input().split()))
        list1+=row
    list2 = []
    for n1 in range(n):
        row1 = list(map(int, input().split()))
        list2 += row1
    for ele1 in list1:
        for ele2 in list2:
            if ele1+ele2==s:
                count+=1
    print(count)