n = int(input())
arr = [int(x) for x in input().split(" ")]
a = arr.count(1)
b = arr.count(2)
if a >= b: print(b+(a-b)//3)
else:print(a)
