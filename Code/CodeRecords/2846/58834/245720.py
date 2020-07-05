n = int(input())
code_origion = input()
codes = code_origion.split()
new_codes = set(codes)
lenth = len(new_codes)
for i in new_codes:
    if i == '0':
        lenth = len(new_codes)-1
print(lenth)