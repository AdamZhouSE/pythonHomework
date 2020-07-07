
tests=int(input())
while tests>0:
    st=input()#"lcpsklryvmcpjnbpbwllsrehfmxrkecwitrsglrexvtjmxypunbqfgxmuvgfajclfvenhyuhuorjosamibdn"
    gset=set()
    gset.update(list(st))
    
    total=len(gset)
    tmap={}
    
    
    if len(gset)==0:
        print(0)
    elif len(gset)==1:
        print(1)
    else:
        
        
        i=0
        j=0
        mi=0
        mj=len(st)-1
        minwindow=float("inf")
        
        while j<len(st):
            #print("entered")
            #print(total)
            
            while j<len(st):
                if st[j] in tmap:
                    tmap[st[j]]=tmap[st[j]]+1
                else:
                    tmap[st[j]]=1
                j=j+1
                if len(tmap)==total:
                    break
            #print("j ",j)    
            while i<j:
                if tmap[st[i]]>1:
                    tmap[st[i]]=tmap[st[i]]-1
                    i=i+1
                else:
                    break
            #print("i ",i)   
            #print("len(tmap) ",len(tmap))
            #print("j-i ",j-i)
            #print("minwindow ",minwindow)
            #print(len(tmap)==total & j-i<minwindow)
            #print(len(tmap)==total)
            #print(j-i<minwindow)
            if ((len(tmap)==total) & (j-i<minwindow)):
                minwindow=j-i
                mi=i
                mj=j-1
                
        print(minwindow)
    tests=tests-1
        
            
            
        
    
    

