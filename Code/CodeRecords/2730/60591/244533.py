def isOk(string):
    string = string.split(" ")
    result = 0
    for m in string:
        result += sum(list(map(int,m)))
    if(result % 3 == 0):
        print(1)
    else:
        print(0)

n = eval(input())
while(n != 0):
    n = n - 1
    input()
    isOk(input())