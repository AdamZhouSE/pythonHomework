length = int(input())
s = input()
cnt = 0
for i in range(0,len(s)):
    if(s[i]=="0"):
        cnt += 1
    else:
        break
s = s[cnt:]
for i in range(1,len(s)):
    if(s[i]=="0"):
        cnt +=1
print("1"+"0"*cnt,end="")
