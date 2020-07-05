prev=input()
toBedeleted=input()
while toBedeleted in prev:
    k=prev.index(toBedeleted)
    prev=prev[0:k]+prev[k+len(toBedeleted):]
print(prev)