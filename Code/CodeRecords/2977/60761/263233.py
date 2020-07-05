revlow=['z','y','x','w','v','u','t','s','r','q','p','o','n','m',
     'l','k','j','i','h','g','f','e','d','c','b','a']
revup=['Z','Y','X','W','V','U','T','S','R','Q','P','O','N','M',
       'L','K','J','I','H','G','F','E','D','C','B','A']
s=input()
while(s!='!'):
    ans=[]
    for i in s:
        if i in revlow:
            ans.append(revlow[ord(i)-ord('a')])
        elif i in revup:
            ans.append(revup[ord(i)-ord('A')])
        else:
            ans.append(i)
    print(''.join(ans))
    s=input()