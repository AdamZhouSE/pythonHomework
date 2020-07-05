src = input()
repo={'I':1,
      'V':5,'IV':4,
      'X':10,'IX':9,
      'L':50,'XL':40,
      'C':100,'XC':90,
      'D':500,'CD':400,
      'M':1000,'CM':900}
index = 0
ans = 0
while index < len(src):
    tmp=src[index:index+2]
    if tmp in ['IV','IX','XL','XC','CD','CM']:
        index += 1
        ans += repo[tmp]
    else:
        ans += repo[src[index]]
    index += 1
print(ans)