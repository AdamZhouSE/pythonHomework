def do(string:str, key:str):
    length = len(key)
    keylist = list(key)
    keylist.sort()
    count = 0
    for i in range(len(string)-length+1):
        tmp = list(string[i:i+length])
        tmp.sort()
        if tmp == keylist:
            count += 1
    return  count

test = int(input())
for t in range(test):
    string = input()
    key = input()
    print(do(string,key))