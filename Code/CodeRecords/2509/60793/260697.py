input()
nums = list(sorted(list(map(int, input().split(" ")))))
commands = [list(input().split(" ")) for i in range(0, int(input()))]
for command in commands:
    if command[0] == "add":
        nums .append(int(command[-1]))
        nums = list(sorted(nums))
    elif command[0] == 'mid':
        print(nums[len(nums) // 2])