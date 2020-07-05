ls = list(input())
b = input()
k = int(input())
for i in range(len(ls)):
    if b[i] != '1':
        ls[i] = '-'
s = ''.join(ls)        
subs = [s[i:i + x + 1] for x in range(len(s)) for i in range(len(s) - x)]  
nsub = list(set(subs))
ct = 0
for sub in nsub:
    if sub.count('-')<=k:
        ct += 1
print(ct)
