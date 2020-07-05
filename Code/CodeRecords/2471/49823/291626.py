def eg(l):
    def helper(s):
        if len(s)%2==1:
            print('not balanced')
            return
        for i in range(len(s)//2):
            if not ((s[i]=='(' and s[len(s)-i-1]==')') or (s[i]=='[' and s[len(s)-i-1]==']') or(s[i]=='{' and s[len(s)-i-1]=='}')):
                print('not balanced')
                return
        print('balanced')
    for i in l:
        helper(i)
if __name__ == '__main__':
    eg([input() for _ in range(int(input()))])
