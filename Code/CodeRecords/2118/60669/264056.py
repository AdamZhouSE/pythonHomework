n=int(input())                                              
                                                            
hypothetic_Max=pow(3,19)                                    
                                                            
if n==0:                                                    
    print(False)                                            
else:                                                       
    print(True if hypothetic_Max%n==0 else False)           