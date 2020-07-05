num=int(input())
s=input()
oldNum = 0
cnt = 0
end = num - 1
chars = list(s)
flag,i=0,0
while i<end :
    if flag==1:
        break
    for j in range(end,i-1,-1) :
        if(i == j):
            if(num % 2==0 or oldNum == 1):
                print("Impossible")
                flag=1
                break
            oldNum = 1
            cnt += num / 2 - i
        if(chars[i]==chars[j]):
            for k in range(j,end):
                t = chars[k]
                chars[k] = chars[k + 1]
                chars[k + 1] = t
                cnt+=1
            end-=1
            break
    i+=1
if flag==0:
    print(cnt)