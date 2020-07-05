n = int(input())
source = input().split(' ')
for end in range(1,n+1):
    s = source[0:end]
    result = []
    for length in range(1,len(s)+1):
        for i in range(0,len(s)-length+1):
            if not s[i:i+length] in result:
                result.append(s[i:i+length])
    print(len(result))

