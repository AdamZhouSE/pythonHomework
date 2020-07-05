from itertools import permutations
strs = input().split(',')
lists = [int(i) for i in strs]
enums = ""
maxtime = 0
for hs,hf,ms,mf in permutations(lists):
    h = 10*hs +hf
    m = 10*ms + mf
    t = h*60 +m
    if h<=23 and m<=59 and t>maxtime:
        enums = "{}{}:{}{}".format(hs,hf,ms,mf)
        maxtime = t
print()