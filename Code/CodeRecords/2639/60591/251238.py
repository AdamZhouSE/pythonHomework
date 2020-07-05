# coding = utf-8
def getLongest(string,N):
    longest = N + 1
    for x in range(0, len(string) - longest):
        y = x + 1
        temp = N
        while (temp != -1):
            if(string[x] == string[y]):
                y += 1
                if(y >= len(string)):
                    break
                continue
            else:
                temp -= 1
                if(temp >= 0):
                    y += 1
                if(y >= len(string)):
                    break
        if(longest < (y - x)):
            longest = (y - x)
    return longest

string = input()
N = eval(input())
a = getLongest(string,N)
print(a)
