tests=int(input())
def func(list1:list,list2:list,indexof:int):
    return sorted(list1+list2)[indexof-1]
for i in range(tests):
    indexof=list(map(int,input().split(" ")))[2]
    second=list(map(int,input().split(" ")))
    third=list(map(int,input().split(" ")))
    print(func(second,third,indexof))