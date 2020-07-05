def bin2int(string):
    outcome = 0
    for i in range(0, len(string)):
        bit = string[len(string) - i - 1]
        if bit == '1':
            outcome = outcome + 2 ** i
    return outcome


times = int(input())
for looptimes in range(0, times):
    strings = input().split()
    print(bin2int(strings[0]) * bin2int(strings[1]))