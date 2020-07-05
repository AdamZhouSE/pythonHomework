# 如果你要翻第i枚硬币，必须把1~i枚都翻转
# 看这个01串可以分成x段，如果最后一段由0组成，则需要反转x次，如果由1，则需要反转x-1次
s = input()
ind = 0
seg = 1
i = 0
while i < len(s):
    if s[i] != s[ind]:
        ind = i
        seg = seg + 1
    i = i + 1
if not s[ind:].__contains__("1"):
    print(seg)
else:
    print(seg - 1)
