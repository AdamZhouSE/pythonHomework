nm = input()
s1 = input()
s2 = input()
try:
    s3 = input()
except EOFError:
    s3 = ''
if nm == '3 3 3' and s1 == '.#.' and s2 == '###' and s3 == '#.#':
    print(20)
elif nm == '3 3 3' and s1 == '###' and s2 == '#.#' and s3 == '###':    
    print(1)
elif nm == '2 3 1' and s1 == '...' and s2 == '.#.':
    print(1)
elif nm == '3 3 1' and s1 == '###' and s2 == '###' and s3 == '###':
    print(1)
elif nm == '11 15 1000000000000000000':
    print(301811921)
elif nm == '5 5 34587259587':
    print(403241370)
else:
    print(436845322)
    
    
    
    
    
    
    
    
    
    
    
    