def legal(str):
    if len(str)%3 != 0:
        return False
    i=j=k=0
    for ch in str:
        if ch == '0':
            i += 1
        elif ch == '1':
            j+= 1
        else:
            k += 1
    return i == j and j == k

def f(str):
    ans = 0
    for i in range(0,len(str)):
        for j in range(i+3,len(str)+1):
           if legal(str[i:j]) :
               ans += 1
    return ans

if __name__ == "__main__":
    testNO = int(input())
    ans = []
    for i in range(testNO):
        str = input()
        ans.append(f(str))
    for res in ans:
        print(res)