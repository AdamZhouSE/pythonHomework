s = input()
sub_str = ""
result = []
'''
for i in range(1, len(s)):
    sub_str = s[:-i]
    if s.find(sub_str) != s.rfind(sub_str):
        break
print(sub_str)
'''
start, length = 0, len(s) - 1
while length > 0:
    while start + length <= len(s):
        sub_str = s[start:length + start]
        if s.find(sub_str) != s.rfind(sub_str):
            result.append(sub_str)
        start += 1
    start = 0
    length -= 1
if result:
    print(result[0])
else:
    print()