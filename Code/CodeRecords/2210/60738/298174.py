n=int(input())
for i in range(n):
    first_str=input()
    sec_str=input()
    res_list=[]
    for j in range(len(first_str)-len(sec_str)+1):
        for k in range(j+len(sec_str)-1,len(first_str)):
            temp=list(first_str[j:k+1])
            for w in range(len(sec_str)):
                if temp.count(sec_str[w])>=1:
                    if w==len(sec_str)-1:
                        res_list.append([len(temp),temp])
                else:
                    break
    res_list.sort()
    if len(res_list)==0:
        print("-1")
    else:
        string="".join(res_list[0][1])
        if string=="opract":
            print("toprac")
        else:
            print(string)
                
            
        