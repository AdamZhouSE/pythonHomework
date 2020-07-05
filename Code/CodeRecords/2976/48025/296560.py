keyword=input()
try:
    while(True):
        s=input()
        
        
        s=s.replace(' ','')
        s=s.replace(keyword.lower(),'')
        s=s.replace(keyword.upper(),'')
        
        print(s)
except EOFError:
    pass