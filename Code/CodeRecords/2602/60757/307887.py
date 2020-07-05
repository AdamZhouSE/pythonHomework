a=eval(input())
b=eval(input())
m=min(len(a),len(b))
ma=0
for i in range(m,0,-1):
    for j in range(len(a)-i+1):
        for k in range(len(b)-i+1):
            if a[j:j+i]==b[k:k+i]:
                ma=i
                break
        if ma>0:
            break
    if ma>0:
        break
print(ma)