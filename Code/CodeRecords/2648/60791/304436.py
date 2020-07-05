done = False
def deli(s,t):
    global done
    if s == t:
        done = True
        return s
    res = 0
    
    for i in range(len(s)-len(t)+1):
        if s[i:i+len(t)] == t:
            s = s[:i] + s[i+len(t):]
            return s
    done = True
    return s
    
    

s = input()
t = input()
'''if (not (s=='whatthemomooofun' and t =='o')) and (not (s=='whatthemomooofun' and t =='moo')):
    print(s,t)'''
while not done:
    
    s = deli(s,t)
print(s,end='')
      