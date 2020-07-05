n=int(input())
list=[int(i) for i in input().split()]
list=sorted(list)
print(" ".join([str[i] for i in list]))