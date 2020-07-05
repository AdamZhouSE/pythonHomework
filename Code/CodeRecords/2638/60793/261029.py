import numpy
temp0 = list(map(int, input().split(" ")))
nums = list(map(int, input().split(" ")))
for i in range(0, temp0[-1]):
    command = list(map(int, input().split(" ")))
    if command[0] == 1:
        for j in range(command[1] - 1, command[2]):
            nums[j] += command[3]
    elif command[0] == 2:
        a = numpy.mean(nums[command[1] - 1:command[2]])
        print('%.4f' % a)
    elif command[0] == 3:
        a = numpy.var(nums[command[1] - 1:command[2]])
        print('%.4f' % a)