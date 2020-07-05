def palindrome(string, a, b):
    if b<= a:
        return True
    for i in range(b,a,-1):
        if string[a] == string[i]:
            string[i],string[b] = string[b],string[i]
            if b!=i:
                cnt[0] += 2*(b-i)-1
            return palindrome(string, a+1, b-1)

    if not havemiddle[0]:
        havemiddle[0] = True
        cnt[0] += 2*(len(string)//2-a)-1
        string[a], string[len(string)//2] = string[len(string)//2], string[a]
        return palindrome(string, a, b)
    return False


if __name__ == '__main__':
    n = int(input())
    cnt = [0]
    havemiddle = [False]
    string = list(input())
    if palindrome(string,0,len(string)-1):
        print(cnt[0])
    else:
        print('Impossible')