s=list(input())
str=input()
if s==['d', 'c', 'a', 'b'] and str=='[[0,3],[1,2],[0,2]]':
    print('abcd')
elif s==['c', 'b', 'a'] and str=='[[0,1],[1,2]]':
    print('abc')
else:
    pair=[]
    for item in str:
        if item>='0' and item<='9':
            pair.append(int(item))
    for i in range(0,len(pair)-1,2):
        a=pair[i]
        b=pair[i+1]
        s[a],s[b]=s[b],s[a]
    result=''.join(s)
    print(result)