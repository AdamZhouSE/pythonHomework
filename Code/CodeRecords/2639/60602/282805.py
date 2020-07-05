from collections import defaultdict
def characterReplacement(s,k):
    left=0;
    cur=defaultdict(int);
    res=0;
    for right,val in enumerate(s):
        cur[val]+=1;
        while right-left+1-max(cur.values())>k:
            cur[s[left]]-=1;
            left+=1;
        res=max(res,right-left+1);
    return res;

print(characterReplacement(input(),int(input())))