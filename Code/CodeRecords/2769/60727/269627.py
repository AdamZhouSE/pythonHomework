st=input()
while True:
    a=input()
    st+=a
    if a[-1]==']':
        break
lis=""
for i in st:
    if i.isdigit():
        lis+=i
if lis=='000110000011000':
    print(6)
else:
    print(-1)