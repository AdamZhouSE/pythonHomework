section_list=list(eval(input()))
new_section=list(eval(input()))
section_list.append(new_section)
section_list.sort(key=lambda x:x[0])
merged=list()
for section in section_list:
    if not merged:
        merged.append(section)
    else:
        if merged[-1][1]>=section[0]:
            merged[-1]=[min(merged[-1][0],section[0]),max(merged[-1][1],section[1])]
        else:
            merged.append(section)
print(merged)
