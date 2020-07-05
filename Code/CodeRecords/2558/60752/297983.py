for i in range(int(input())):
    s=list(input())
    rs=-1
    if len(s)%2==0:
        left=0
        right=0
        shift=0
        for ss in range(len(s)):
            if s[ss]=='}'and left==0:
                s[ss]='{'
                shift+=1
                left+=1
            else:
                if s[ss]=='{':
                    left+=1
                if s[ss]=='}':
                    left-=1

        for sss in range(len(s)):
            ss=len(s)-1-sss
            if s[ss] == '{' and right == 0:
                s[ss] = '}'
                shift += 1
                right += 1
            else:
                if s[ss] == '}':
                    right += 1
                if s[ss] == '{':
                    right -= 1
        rs=shift
    print(rs)


