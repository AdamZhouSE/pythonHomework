def insertSort(ans,list):
    if(list!=[]):
        if(ans==[]):
            ans.append(list[0]);
            list.remove(list[0]);
            return insertSort(ans,list);
        else:
            if(ans[0]>=list[0]):
                ans.insert(0,list[0]);
                list.remove(list[0]);
                return insertSort(ans,list);
            elif(ans[len(ans)-1]<=list[0]):
                ans.append(list[0]);
                list.remove(list[0]);
                return insertSort(ans,list);
            else:
                i=0;
                while(i<len(ans)-1):
                    if(list[0]>=ans[i] and list[0]<=ans[i+1]):
                        ans.insert(i+1,list[0]);
                        list.remove(list[0]);
                        return insertSort(ans,list);
                        break;
                    i+=1;
    else:
        return ans;

list=eval(input());
print(insertSort([],list));