
def longestConsecutive(nums):
    if nums==None or len(nums)==0:
        return 0
    rmap,vmap={},{}
    for e in nums:
        if e not in rmap:
            rmap[e],vmap[e]=e,1
            if e+1 in rmap:
                vmap[e]+=vmap[e+1]
            if e-1 in rmap:
                vmap[rmap[e-1]]+=vmap[e]
                rmap[e]=rmap[e-1]
            rmap[rmap[e]+vmap[rmap[e]]-1]=rmap[e]
    tmp,res=max(vmap.items(),key=lambda x: x[1])
    return res
if __name__ == '__main__':
    s = input()
    s = ''.join(s[1:len(s)-1].split(","))
    list0 = list(map(int,s.split(" ")))
    print(longestConsecutive(list0))