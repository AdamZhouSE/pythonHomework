password=input()
n=int(input())
summ=0
for i in range(1,n+1):
    s=input()
    barrel1=[0]*26
    for k in range(len(s)):
        barrel1[ord(s[k])-ord('a')]+=1
    for j in range(len(password)-7):
        strr=password[j:j+8]
        barrel2=[0]*26
        for k in range(len(strr)):
            barrel2[ord(strr[k])-ord('a')]+=1
        if(barrel1==barrel2):
            summ+=1
print(summ)