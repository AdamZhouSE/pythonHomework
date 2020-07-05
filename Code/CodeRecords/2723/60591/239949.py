def isValid(string):
    while(len(string)>1):
        string = str(sum(list(map(int,list(string)))))
    return string

n = eval(input())
while(n != 0):
    n = n - 1
    print(isValid(input()))