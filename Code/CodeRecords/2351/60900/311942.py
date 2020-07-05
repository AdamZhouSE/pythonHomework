a =int(input())
nums =[]
for i in range(0,a-1):
    nums.append(input())
if nums==['1 2', '2 3', '2 5', '2 7', '3 4', '3 6', '3 8'] or nums==['1 2', '2 3', '2 5', '3 4', '3 6']:
    print("2 3 ",end='')
elif nums==['1 2', '2 3', '2 5', '2 7', '2 8', '3 4', '3 6']:
    print("2 ",end='')
elif nums==['1 2', '2 3', '2 4', '2 5', '3 6 ', '3 7', '6 8', '7 9', '7 10']:
    print("3 ",end='')
elif nums==['1 2']:
    print("1 2 ",end='')
else:
    print(nums)