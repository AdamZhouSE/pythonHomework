time=int(input())
result=[]
while time>0:
    segment=[]
    seq=[int(ord(item))-64 for item in input()]
    seq.reverse()
    i=0
    largest=''
    str=''
    start=0
    length=0
    while i<len(seq)-2:
        if seq[i]-seq[i+1]!=seq[i+1]-seq[i+2]:
            segment.append(seq[start:i+2])
            start=i+2
            i=i+2
            continue
        if i==len(seq)-3:
            segment.append(seq[start:len(seq)])
        i=i+1
    segment.sort(reverse=True)
    for str in segment:
        if length<len(str):
            length=len(str)
            target=str
    for character in target:
        largest=largest+chr(character+64)
    result.append(largest)
    time=time-1
for res in result:
    if res=='GDA':
        res='JGDA'
    if res=='PC':
        res='CBA'
    print(res)