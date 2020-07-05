def function(s):
    l = s.split(' ')

    for i in range(len(l)):
        l[i] = list(l[i])

    string = []
    for i in range(len(l)):
        l[i].sort()

        if not l[i] in string:
            string.append(l[i])

    nums = []
    for i in range(len(string)):
        nums.append(l.count(string[i]))

    nums.sort()
    for i in range(len(nums)-1):
        print(nums[i], end='')
        print(' ', end='')

    print(nums[len(nums)-1])


n = int(input())
num = []
wordarr = []

for i in range(n):
    num.append(int(input()))
    wordarr.append(input())

for i in range(n):
    function(wordarr[i])