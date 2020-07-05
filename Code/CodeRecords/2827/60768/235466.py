column = int(input())
height = input().split(' ')
height = [int(x) for x in height]
height.sort()
height = [str(x) for x in height]
height = " ".join(height)

print(height)
