num_of_children, num_of_sentence = map(int, input().split(" "))
information_of_children = []
for i in range(0, num_of_sentence):
    information = input().split(" ")
    if information[0] == "M":
        information_of_children.append([int(information[1]), int(information[2])])
    else:
        information_of_children = sorted(information_of_children, key=lambda x: x[0], reverse=True)
        result = -1
        for j in range(0, len(information_of_children)):
            if information_of_children[j][0] <= int(information[1]):
                temp = sorted(information_of_children[j:],key=lambda x:x[1])
                for k in range(0, len(temp)):
                    if temp[k][1] >= int(information[2]):
                        result = temp[k][1]
                        break
                break
        print(result)
