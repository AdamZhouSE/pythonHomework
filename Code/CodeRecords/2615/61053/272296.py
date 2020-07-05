def f(str):
    str = str[::-1]
    ans = ""
    tempstring = str[0]
    former_delta = ord(str[1]) - ord(str[0])
    for i in range(1,len(str)):
        delta = ord(str[i]) - ord(str[i-1])
        if delta<0 and delta == former_delta:
            tempstring += str[i]
            continue
        if len(tempstring) > len(ans) or (len(tempstring) == len(ans) and tempstring[0] > ans[0]):
            ans = tempstring
        if delta >= 0:
            tempstring = str[i]
        else:
            tempstring = str[i-1:i+1]
            former_delta = delta
    if len(tempstring) > len(ans) or (len(tempstring) == len(ans) and tempstring[0] > ans[0]):
        ans = tempstring
    return ans

if __name__ == "__main__":
    testNO = int(input())
    ans = []
    for i in range(testNO):
        str = input()
        ans.append(f(str))
    for res in ans:
        print(res)