num=input();
string=input();
l=string.split();
count=0;
for i in range(len(l)):
    if (sorted(l,reverse=True)==l[-i:]+l[0:-i]) & (len(l)>2):
        print(-1)
        break;
    elif sorted(l)==l[-i:]+l[0:-i]:
        print(i);
        break;
    else:
        count+=1;
        
if(count==len(l)):
    print(-1);