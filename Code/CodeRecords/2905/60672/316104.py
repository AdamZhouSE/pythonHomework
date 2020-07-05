def getDecimalValue(head):
        cur = head
        ans = 0
        i=0
        while i<len(cur):
            ans = ans * 2 + int(cur[i])
            i=i+1
        return ans

like=list(input())
answer= getDecimalValue(like)
print(answer)