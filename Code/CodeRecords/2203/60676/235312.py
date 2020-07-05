import math


def get_mystery(string):
    sum = 0
    for length in range(1, len(string)+1):
        for i in range(len(string)-length):
            for j in range(i+1, min(len(string)-length+1, i+length)):
                if string[i:i+length] == string[j:j+length]:
                    sum += length
    return sum


raw_str = input()
for i in range(len(raw_str)):
    print(get_mystery(raw_str[:i+1]))
