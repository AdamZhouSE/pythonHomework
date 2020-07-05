def check(string:str):
    if len(string) % 3 != 0:
        return False
    count = [0,0,0]
    for x in string:
        idx = int(x)
        count[idx] += 1
    return count[0] == count[1] and count[1] == count[2]


def do(string:str):
    count = 0
    for start in range(len(string)-1):
        for end in range(start+2,len(string),3):
            if check(string[start:end+1]):
                count += 1
    return count

t = int(input())
for i in range(t):
    string = input()
    print(do(string))