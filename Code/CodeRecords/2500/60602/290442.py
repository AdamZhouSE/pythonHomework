def cookieReverse(list,k):
    temp=list[0:k];
    temp.reverse();
    return temp+list[k:];


ans=[];
list=eval(input());
while(len(list)!=1):
    if(list==sorted(list)):
        break;
    if(list[0]==max(list)):
        list=cookieReverse(list,len(list));
        ans.append(len(list));
        list=list[0:len(list)-1];
    else:
        ans.append(list.index(max(list))+1);
        list=cookieReverse(list,list.index(max(list))+1);

print(ans);