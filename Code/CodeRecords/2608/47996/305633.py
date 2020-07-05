def isVowel(ch):
    if ch != "a" and ch != "e" and ch != "i" and ch != "o" and ch != "u":
        return False
    else:
        return True

def cut(str):
    results = []
    for x in range(len(str)):
        for i in range(len(str) - x):
            if x == 0:
                results.append(str[i:i + x + 1])
            elif x < 2:
                for j in range(len(str) - x - i):
                    results.append(str[i] + str[j + x + i])
            else:
                for j in range(len(str) - x - i):
                    results.append(str[i:i+x] + str[j + x + i])

    return results
    
def modify(res, tar, pre, suf):
    for item in res:
        item = pre + item + suf
        tar.append(item)
    return tar

n = int(input())
while n > 0:
    n -= 1
    result = []
    string = input()
    strlen = len(string)
    for i in range(strlen):
        if isVowel(string[i]) == True:
            for j in range(i+1, strlen):
                if isVowel(string[j]) == False:
                    str = string[i] + string[j]
                    result.append(str)
                    modify(cut(string[i+1:j]), result, string[i], string[j])
    result = list(set(result))
    result.sort(reverse=True)
    if len(result) == 0:
        print("-1")
    else:
        leng = len(result)
        for i in range(leng):
            if i != leng-1:
                print(result.pop(), end=" ")
            else:
                print(result.pop())
