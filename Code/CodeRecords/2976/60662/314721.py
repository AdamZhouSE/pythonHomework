import sys
s = str(input())
text = sys.stdin.readlines()
for i in range(0, len(text)):
    temp = text[i].replace(s.upper(), '')
    temp = temp.replace(s.lower(), '')
    text[i] = temp.replace(' ', '')
for i in text:
    print(i,end='')
print()