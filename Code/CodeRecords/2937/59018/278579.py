def different(info,a):
    count=0
    for i in range(len(a)):
        if a[i]!=info[i]:
            count=count+1
    print(count)
            
    
    
    
    
    
    
    
    
info='CODEFESTIVAL2016'
a=input()
different(info,a)