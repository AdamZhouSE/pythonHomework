def f(s,x,y):
    for i in range(0,len(s)-x):
        if (s[i]>=s[i+x] and s[i]-s[i+x]<=y) or (s[i+x]>=s[i] and s[i+x]-s[i]<=y):
               return 'true'

    return 'false'
                
                
        
s=input().strip().split('=')
x=eval(s[1][1:len(s[1])-4])
y=int(s[2][1:2])
z=int(s[3][1:2])

print(f(x,y,z))