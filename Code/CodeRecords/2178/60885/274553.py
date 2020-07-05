def findSub(cards):
    ans = 0
    for i in range(1,len(cards)+1):
        carry = set()
        for j in range(len(cards)-i+1):
            s = ''.join(cards[j:j+i])
            carry.add(s)
        ans += len(carry)
    return ans

n = int(input())
cards = input().split()
A = []
for i in range(1,n+1):
    A.append(findSub(cards[:i]))
for num in A:
    print(num)
