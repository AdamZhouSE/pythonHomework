def arrSort(arr1,arr2):
    i=0;
    ans=[];
    while(i<len(arr2)):
        j=0;
        while(j<len(arr1)):
            if(arr1[j]==arr2[i]):
                ans.append(arr1[j]);
                arr1.remove(arr1[j]);
                j-=1;
            j+=1;
        i+=1;

    ans+=sorted(arr1);
    print(ans);

arr1=eval(input());
arr2=eval(input());

arrSort(arr1,arr2);