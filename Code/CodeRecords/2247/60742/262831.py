def helper(piles,cur0,cur1,l,r,player):
    if l>r:
        return cur0>cur1
    if player==0:
        return helper(piles,cur0+piles[l],cur1,l+1,r,1) or helper(piles,cur0+piles[r],cur1,l,r-1,1)
    return helper(piles,cur0,cur1+piles[l],l+1,r,0) or helper(piles,cur0,cur1+piles[r],l,r-1,0)

piles = [int(i) for i in input().split(',')]
if helper(piles,0,0,0,len(piles)-1,0):
    print("True")
else:
    print("False")