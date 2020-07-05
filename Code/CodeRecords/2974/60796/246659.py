def palindromeOrNot(string):
    i = len(string) - 1
    s = ""
    while i >= 0:
        s = s + string[i]
        i = i - 1
    if s==string:
        return True
    else:
        return False

n=int(input())
s=input()
#print(s)
max=0
for a in range(1,len(s)-1):
    s1=s[:a]
    s2=s[a:]
    #print("s1:",s1)
    #print("s2:",s2)
    s1oddPalindrome=""#用来表示前一段的所有正回文子串
    s2notPalindrome=""#用来表示后一段的所有非正回文子串
    A=0#前一段正回文子串数
    B=0#后一段非正回文子串数
    #下面看前一段有多少个正回文子串s1[i:j]  i<=len(s1)-1,j<=len(s1)
    i=0
    #print("正回文子串：")
    while i<=len(s1)-1:
        j=i+1
        while j<=len(s1):
            string=s1[i:j]
            if len(string)%2==1:
                if palindromeOrNot(string) and not(s1oddPalindrome.__contains__("'"+string+"'")):
                    #print(string)
                    s1oddPalindrome=s1oddPalindrome+"'"+string+"'"
                    A=A+1
            j=j+1
        i=i+1
    #下面看后面一段有多少个正回文子串s2[i:j]  i<=len(s2)-1,j<=len(s2)
    i=0
    #print("非正回文子串：")
    while i<=len(s2)-1:
        j=i+1
        while j<=len(s2):
            string=s2[i:j]
            #print(string)
            if len(string)%2==0 or (not(len(string)%2==1 and palindromeOrNot(string))):
                if not(s2notPalindrome.__contains__("'"+string+"'")):
                    B=B+1
                    s2notPalindrome=s2notPalindrome+"'"+string+"'"
                    #print("非正 ",string)
            j=j+1
        i=i+1

    if A*B>max:
        max=A*B
    #print("A*B",A*B)

print(max)

