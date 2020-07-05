#冒泡排序
def BubbleSort(lst):
    n=len(lst)
    if n<=1:
        return lst
    for i in range (0,n):
        for j in range(0,n-i-1):
            if lst[j]>lst[j+1]:
                (lst[j],lst[j+1])=(lst[j+1],lst[j])


a = [int(i) for i in input().replace("[","").replace("]","").replace(","," ").split(" ")]
BubbleSort(a)
print(a)
