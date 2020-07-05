n=int(input())
list=[int(i) for i in input().split()]
list=sorted(list)
print(str(min(list[n-1]-list[1],list[n-2]-list[0])))