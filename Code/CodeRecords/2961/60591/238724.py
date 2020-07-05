def reverse(string,n):
    return string[n:] + string[0:n]

def find(string):
    length = len(string)
    result = []
    result.append(string)
    for m in range(length-1):
        result.append(reverse(string,m+1))
    result.sort()
    fin = ""
    for m in result:
        fin += m[-1]
    return fin

print(find(input()),end = "")