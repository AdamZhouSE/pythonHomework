s = input()
frequency = []
for a in range(0,26):
    frequency.append(0)
for x in s:
    frequency[ord(x)-ord('a')]+=1
result = ""
count = 0
for x in frequency:
    if x!=0:
        count+=1
while True:
    ptr=frequency.index(max(frequency))
    while frequency[ptr]!=0:
        result=result+chr(ptr+ord('a'))
        frequency[ptr]-=1
    count-=1
    if count==0:
        break
print(result)
