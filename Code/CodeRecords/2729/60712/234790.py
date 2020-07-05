source_list = list(map(int,input().strip("[||]").split(",")))
    
if len(source_list) == 1:
    print(source_list[0])
else:
    result = 0
    start = 0
    end = len(source_list)
    length = len(source_list[start:end])
    while (length >= 3):
        mid = int((end - start) / 2)
        if length == 3:
            if source_list[start+mid- 1] == source_list[start+mid]:
                result = source_list[start+mid + 1]
                break
            else:
                result = source_list[start+mid - 1]
                break
        else:
            if mid%2==0:
                if source_list[start+mid-1] == source_list[start+mid-2]:
                    start = start+mid
                    end = end
                else:
                    start = start
                    end = start+mid+1
            else:
                if source_list[start+mid] == source_list[start+mid-1]:
                    start = start+mid+1
                    end = end
                else:
                    start = start
                    end = start+mid
        length = len(source_list[start:end])
print(result)
