s=input()
n = int(input())
op = []
for i in range(n):
    op.append(input.split())
for i in range(n):
    if op[0]=='1':
        s=s+op[1]
    elif op[0]=='2':
        s=op[1][::-1]+s
    else:
        sum1=len(s)
        k=2
        while k<=en(s):
            for i in range(n):
                if i+k<=n:
                    s2=s[i:i+k]
                    if s2=s2[::-1]:
                        sum1+=1
            k+=1
        print(sum1)
                    
              
            
        