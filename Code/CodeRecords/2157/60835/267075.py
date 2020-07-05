rome = input()
result = 0
n = 0
while len(rome) > n:
    if rome[n] == 'M':
        result = result + 1000
    elif rome[n] == 'D':
        result = result + 500
    elif rome[n] == 'C':
        if n + 1 < len(rome):
            if rome[n+1] == 'M' :
                result = result + 800
                n = n + 1
            elif rome[n+1] == 'D':
                result = result + 300
                n = n + 1
        result = result + 100
    elif rome[n] == 'L':
        result = result + 50
    elif rome[n] == 'X':
        if n + 1 < len(rome):
            if rome[n+1] == 'C' :
                result = result + 80
                n = n + 1
            elif rome[n+1] == 'L':
                result = result + 30
                n = n + 1
        result = result + 10
    elif rome[n] == 'V':
        result = result + 5
    elif rome[n] == 'I':
        if n + 1 < len(rome):
            if rome[n+1] == 'X' :
                result = result + 8
                n = n + 1
            elif rome[n+1] == 'V':
                result = result + 3
                n = n + 1
        result = result + 1
    n = n + 1
print(result)