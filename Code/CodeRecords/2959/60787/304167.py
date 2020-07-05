a=input()
b=input()
re=0
for length in range(0,min(len(a),len(b))):
    for i in range(0,len(a)-length+1):
        for j in range(0,len(b)-length+1):
            if a[i:i+length]==b[j:j+length]:
                re+=1
print(re)