s1=input()
for num in range(0,len(s1)):
    s=s1[:num+1]
    count=0
    for length in range(2,len(s)):
        for i in range(0,len(s)-length):
            for j in range(i+1,i+length):
                if(s[i:i+length]==s[j:j+length]):
                    count=count+length
    print(count)

