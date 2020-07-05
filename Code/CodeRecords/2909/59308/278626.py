s = input()
maxLetters = int(input())
minSize = int(input())
maxSize = int(input())
ans = dict()
ans[' '] = 0
for i in range(minSize, maxSize+1):
    for k in range(0, len(s)-i+1):
        sub_s = s[k:k+i]
        d_ = list()
        for j in sub_s:
            if j not in d_:
                d_.append(j)
        if len(d_) <= maxLetters:
            if sub_s in ans:
                ans[sub_s] += 1
            else:
                ans[sub_s] = 1
print(max(ans.values()))




