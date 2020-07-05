def convert(n):
    table = {}
    for i in range(ord('A'), ord('Z') + 1):
        table[ i - ord('A')+1 ] =chr(i)
    table[0]='0'
    output=''
    while n>0:
        if n%26 != 0:
            output=table[n%26]+output
            n=n//26
        else:
            output=table[26]+output
            n=n//26-1
    return  output
n=int(input())
print(convert(n))