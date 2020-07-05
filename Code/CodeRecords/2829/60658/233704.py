n = int(input())
li = [int(x) for x in input().split()]
li.sort()
print(li[-1]-li[1] if (li[-1]-li[1])<(li[-2]-li[0]) else li[-2]-li[0])