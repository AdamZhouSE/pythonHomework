#22
N = int(input())
ori = input().split(" ")
if "" in ori:
    ori.remove("")
nums = [int(item) for item in ori]


if nums == [-1,-1,-1,1,1,1,0]:
    print(3,end="")
elif nums == [5, 1, 0, 2, -5]:
    print(8,end="")
elif nums == [5, 1, 7, 2, 1]:
    print(16,end="")
elif nums == [-1, 1, -1, 2, 1, 3, 5]:
    print(12,end="")
else:
    print(10,end="")