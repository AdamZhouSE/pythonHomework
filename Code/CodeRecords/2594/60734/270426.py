def f(string):
    string = string.lower()
    max_len = -1
    for i in range(len(string)):
        for j in range(i+1,len(string)):
            if string[i] == string[j]:
                max_len = max(max_len,j-i-1)
    return max_len
t = int(input())
for i in range(t):
    print(f(input()))