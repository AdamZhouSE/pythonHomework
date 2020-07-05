def solve(string):
    seen = set()
    for i in range(len(string)):
        if(string[i] in seen):
            return 0
        seen.add(string[i])
    return 1
T = int(input())
x = 0
while(x<T):
    x+=1
    temp = input()
    print(solve(temp))