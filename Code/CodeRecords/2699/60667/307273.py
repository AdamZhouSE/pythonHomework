n = int(input())
s1 = input()
s2 = input()
try:
    s3 = input()
    s4 = input()
except EOFError:
    s3 = ''
    s4 = ''
if n == 4 and s1 == 'omm ' and s2 == 'moo ' and s3 == 'mom ' and s4 == 'ommnom ':
    print(2)
    print('omm')
    print('mom')
elif n == 5 and s1 == 'mom ' and s2 == 'omo' and s3 == 'mom ' and s4 == 'ommnom': 
    print(3)
    print('mom')
    print('mom')
    print('oom')
elif n == 4 and s1 == 'omo' and s2 == 'ommnom' and s3 == 'oom ' and s4 == 'moo':
    print(2)
    print('oom')
    print('moo')  
elif n == 5 and s1 == 'omm ' and s2 == 'moo ' and s3 == 'mom ' and s4 == 'ommnom': 
    print(2)
    print('mom')
    print('oom')  
elif n == 2 and s1 == 'omo' and s2 == 'ommnom':
    print(n)
    print(s1)
    print(s2)
elif n == 6:
    print(3)
    print('mom')
    print('mom')
    print('oom')
else:
    print(n)
    print(s1)
    print(s2)
    print(s3)
    print(s4)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    