def check(l:int, r:int, L:int, R:int):
    if ((r - l + 1) % (R - L + 1)!=0): return 0;
    for i in range(l, r + 1):
        if (s[i] != s[(i - l) % (R - L + 1) + L]): return 0;
    return 1;




def dfs(l:int, r:int):
    if  l == r : return "".join(s[l:l + 1]);
    if  len(f[l][r]) > 0 : return f[l][r];
    f[l][r] = "".join(s[l:l + r - l + 1]);
    for i in range(l, r):
        if (len(f[l][r]) >( len(dfs(l, i)) + len(dfs(i + 1, r)))):
            f[l][r] = dfs(l, i) + dfs(i + 1, r);
    for i in range(l, r):
        if (check(l, i, i + 1, r) == 1):  # daozheli
            strtemp = str(int((r - l + 1) / (r - i))) + "(" + dfs(i + 1, r) + ")";
            if (len(f[l][r]) > len(strtemp)):
                f[l][r] = strtemp;
    return f[l][r];


s = list(input());
lenngthmy = len(s);
f = [] ;
for i in range(100):
    f.append([""] * (100));
# f[0][17]="agfdsag";
# print(len(f[0][17]))
print(dfs(0, lenngthmy - 1));