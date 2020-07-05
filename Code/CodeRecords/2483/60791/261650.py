from collections import Counter
def solve(string,patt):
    dic = dict(Counter(patt))
    for i in range(len(string)):
        if string[i] in dic:
            return string[i]
    return '$'


T = int(input())
x = 0
while(x<T):
    x+=1
    string = input()
    patt =input()
    print(solve(string,patt))