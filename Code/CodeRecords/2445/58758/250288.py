inp = input().split()
s = inp[2][1: len(inp[2])-2]
t = inp[5][1: len(inp[5])-1]
dic_s = {}
dic_t = {}
for ch in s:
    dic_s[ch] = dic_s.get(ch, 0)+1
for ch in t:
    dic_t[ch] = dic_t.get(ch, 0)+1
if dic_t == dic_s:
    print('true')
else:
    print('false')
