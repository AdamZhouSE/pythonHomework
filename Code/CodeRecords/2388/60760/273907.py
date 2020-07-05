def func(list1:list,list2:list):
    if sorted(list1)==sorted(list2):
        print(1)
    else:
        print(0)
list1s=[]
list2s=[]
tests=int(input())
for i in range(tests):
    l=input()
    list1s.append(list(map(int, input().split(" "))))
    list2s.append(list(map(int, input().split(" "))))
for i in range(tests):
    func(list1s[i],list2s[i])