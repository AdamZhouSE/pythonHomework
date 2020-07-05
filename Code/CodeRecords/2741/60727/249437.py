def solution(li):
    leng = len(li)
    maxLen = 0
    for i in range(0,leng-1):
        count=0
        temp=i
        if leng-1-i<maxLen or leng-1-i==maxLen:
            return maxLen
        for j in range(i+1,leng):
            if li[j]>li[i]:
                count+=1
                temp+=1
            else:
                i=temp+1
                if maxLen<count:
                    maxLen = count
                break
    return maxLen
        
a=input()
li=a[1:len(a)-1].split(',')
print(solution(li))